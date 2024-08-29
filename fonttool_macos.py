import os
import sys
import frozen_dir
from fontTools.subset import main as ss


def main():
    file = open(frozen_dir.app_path() + r'/config/sourcePath.txt', 'rb')
    source_font_path_bytes = file.read()
    source_font_path = str(source_font_path_bytes, 'utf-8')
    print(source_font_path)
    file.close()

    file = open(frozen_dir.app_path() + r'/config/outputPath.txt', 'rb')
    output_font_path_bytes = file.read()
    output_font_path = '--output-file=' + str(output_font_path_bytes, 'utf-8')
    print(output_font_path)
    file.close()

    textfile_temp = frozen_dir.app_path() + r'/config/fontcontent.txt'
    textfile_temp = '--text-file=' + textfile_temp
    textfile = textfile_temp.replace('/', '/')
    print(textfile)

    sys.argv = [None, source_font_path,
                output_font_path,
                textfile,
                '--unicodes=U+0020-002F']
    ss()
    os.system("pause")


if __name__ == '__main__':
    main()
