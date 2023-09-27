# 2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
from sys import argv
from futils.cooke import filer
from futils.rename import renamer

if len(argv)==8:
    dir = argv[1]
    start = int(argv[3])
    stop = int(argv[4])
    digs = int(argv[6])
    print(*filer(avi=digs, jpg=digs, txt=digs, dir=dir), sep="\n")
    print(*renamer(dir, argv[2], start, stop, argv[5], digs, argv[7]), sep='\n')
else:
    print(f"Usage: python3 {argv[0]} dir src-ext src-start src-end dst-name dig-amount dst-ext")
    print("ARGS: dir - directory name\n\
      src-ext - source extension\n\
      src-start - first charset of source file name that goes to suffix\n\
      src-end - last charset of source file that goes to suffix\n\
      dst-name - destination file name prefix\n\
      dig-amount - number of digits in file counting after prefix\n\
      dst-ext - extension for destination files")
    print(f"Example: python3 {argv[0]} tmp txt 2 4 new 2 md")



