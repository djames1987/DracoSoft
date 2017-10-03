import sqlite3

# Create SQLite vars
conn = sqlite3.connect('C:\DragonSoft\Game_Server_Manager\data_base.db')
c = conn.cursor()

# Create table if it does not exist
def mk_table():
    c.execute('CREATE TABLE IF NOT EXISTS game_servers(game_name VARCHAR(2048), app_id INTEGER, game_location VARCHAR(2048), gamesave_location VARCHAR(2048))')
    c.execute('CREATE TABLE IF NOT EXISTS servers(server_name VARCHAR(240), local_ip INTEGER, ext_ip INTEGER, host_name VARCHAR(240), running_os VARCHAR(240))')
    conn.commit()


def add_to_db( type, args):
    if type == 'server':
        servername = args[0]
        loc_ip = args[1]
        e_ip = args[2]
        host_names = args[3]

        c.execute('INSERT INTO servers(server_name, local_ip, ext_ip, host_name) VALUES (?,?,?,?)', (servername, loc_ip, e_ip, host_names))
        conn.commit()

    elif type == 'game':
        gname = args[0]
        appid = args[1]

        c.execute('INSERT INTO game_servers(game_name, app_id) VALUES (?,?)', (gname, appid))
        conn.commit()

    else:
        print('Unkown type')


def remove_game_server(arg1, arg2):
    if arg1 == 'game':
        query = "delete from game_servers where game_name = '%s' " %arg2
        c.execute(query)
        conn.commit()

    elif arg1 == 'server':
        query = "delete from servers where server_name = '%s' " %arg2
        c.execute(query)
        conn.commit()

    else:
        print('Unknown type')


def change_game_data(arg1, arg2, arg3):
    gname = arg1

    if arg2 == 'gamesave path':
        c.execute('UPDATE game_servers SET gamesave_location=? WHERE game_name=?', (arg3,gname))
        conn.commit()

    elif arg2 == 'game path':
        c.execute('UPDATE game_servers SET game_location=? Where game_name=?', (arg3,gname))
        conn.commit()

    else:
        print("No option selected, either gamesave path or game path")


def close_conn():
    conn.close()
        


# This Closes the SQLite Database Connection and must be at the end of the file

