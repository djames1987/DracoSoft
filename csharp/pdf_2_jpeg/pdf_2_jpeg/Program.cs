using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using System.Drawing;
using System.IO;

namespace pdf_2_jpeg
{
    class Program
    {
        public static void PdfToJpg(string ghostScriptPath, string input, string output)
        {
            String ars = "-q -dBATCH -dNOPAUSE -sDEVICE=pngalpha -dFirstPage=1 -dLastPage=1 -r300 -sOutputFile=" + output + "-%d.png " + "-f " + input;
            Process proc = new Process();
            proc.StartInfo.FileName = ghostScriptPath;
            proc.StartInfo.Arguments = ars;
            proc.StartInfo.CreateNoWindow = true;
            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.Start();
            proc.WaitForExit();
        }

        public static void resizeImage(string imageFile, string outputFile, double scaleFactor)
        {
            using (var srcImage = Image.FromFile(imageFile))
            {
                var newWidth = (int)(srcImage.Width * scaleFactor);
                var newHeight = (int)(srcImage.Height * scaleFactor);
                using (var newImage = new Bitmap(newWidth, newHeight))
                using (var graphics = Graphics.FromImage(newImage))
                {
                    graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
                    graphics.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                    graphics.PixelOffsetMode = System.Drawing.Drawing2D.PixelOffsetMode.HighQuality;
                    graphics.DrawImage(srcImage, new Rectangle(0, 0, newWidth, newHeight));
                    newImage.Save(outputFile);
                }

            }
        }

        static void Main(string[] args)
        {
            string ghostScriptPath = @"D:\GhostScript\x64\gs\gs9.22\bin\gswin64.exe";
            string inputFileName = @"D:\csharp\pdf_2_jpeg\pdf_test\test.pdf";
            string outputFileName = @"D:\csharp\pdf_2_jpeg\pdf_test\new";
            string imageInputFileName = @"D:\csharp\pdf_2_jpeg\pdf_test\new-1.png";
            string imageOutputFileName = @"D:\csharp\pdf_2_jpeg\pdf_test\done.png";

            PdfToJpg(ghostScriptPath, inputFileName, outputFileName);
            resizeImage(imageInputFileName, imageOutputFileName, 0.05);
            File.Delete(imageInputFileName);
        }
    }
}
