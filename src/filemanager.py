import os
from os import listdir
from os.path import isfile, join

import argparse
#instantiate the parser
parser = argparse.ArgumentParser(description=
                              "autocorrection, \
                              arg1 = gabarito path, \
                              arg2 = answers imgs path") #, \
                              #arg3 = result path")

parser.add_argument('gab_path', type=str,
                  help='Enter the file path')
parser.add_argument('ans_path', type=str,
                  help="Enter destination for aligned img")

args = parser.parse_args()


# reading path images
path = args.ans_path
print path
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print onlyfiles

gab = str(args.gab_path)
print gab

os.chdir("/home/pi/git/TCC/autocorrectionMCQ/src/")
for _file in onlyfiles:
    _file = path + str(_file)
    gab = "/home/pi/git/TCC/autocorrectionMCQ/gabarito/answers.csv"
    print _file
    os.system("./test.sh gab _file")
    print("Processing")
    

