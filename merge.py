import os
import glob
directory = r"C:\djangostuff\NTP\*.log"
files = glob.glob(directory)

for path in glob.glob(directory):
    dirname, filename = os.path.split(path)
    filedatetime = filename[-14:-4]
    print(filedatetime)
    with open(path) as fp:
        line = fp.readline()
        cnt =1
        while line:
            resultline = "{};{}".format(filedatetime, line.strip())

            with open('result.csv', 'a') as f1:
                if cnt == 1:
                    print('Proccesing '+ filename)
                else:
                    f1.write(resultline + os.linesep)
            line = fp.readline()
            cnt = cnt+1


