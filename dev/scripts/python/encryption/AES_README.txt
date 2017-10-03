encrypt_file use:

encrypt_file('Key-Made-Up', 'test.txt', 'test.enc')

Key:
 A password you need to both encrypt and decrypt the file

in_filename:
 Name of the input filesize

out_filename:
 If None, '<in_filename>.enc' will be used

chunksize:
 Sets the Size of the chunk which the function uses
 to read and encrypt the file. Larger chunk sizes
 can be faster for some files and machines.
 chunksize must be divisible be 16

 decrypt_file use:

 decrypt_file('Key-Made-Up', 'test.enc', 'test.txt')

Decrypts a file using AES (CBC mode) with the given key.
Parameters are similar to encrypt_data, with one
difference: out_filename, if not supplied will be
in_filename without its last extension
(i.e. if in_filename is 'aaa.zip.enc' then out_filename
will be 'aaa.zip')
