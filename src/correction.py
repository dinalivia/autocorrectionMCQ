# -------------------------------------
# Answersheet autocorrection
# --
#
# Developed by Dina Livia - 10.06.2019
# --------------------------------------

#!/usr/bin/python

# Standard imports
import csv
import argparse
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox

#instantiate the parser
parser = argparse.ArgumentParser(description=
                              "extract answers app, \
                              arg1 = answers csv, \
                              arg2 = keyanswer csv")

parser.add_argument('ans_path', type=str,
                  help='Enter the file path')
parser.add_argument('key_path', type=str,
                  help="Enter destination for ROI img")
args = parser.parse_args()

f1 = open(args.ans_path, 'r')
f2 = open(args.key_path,'r')
f3 = open('results.csv', 'w')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

masterlist = list(c2)

row = 1
correct_answers = 0
wrong_answers = 0

for hosts_row in c1:
    found = False
    for (master_row) in masterlist:
        results_row = hosts_row
        if row == 1:
            results_row.append('STATUS')
            found = True
            row = row + 1
            break

        elif hosts_row == master_row:
            results_row.append('CORRECT (row ' + str(row) + ')')
            found = True
            correct_answers += 1
            break
        row = row + 1
    if not found:
        results_row.append('WRONG')
        wrong_answers += 1
    c3.writerow(results_row)

#check_duplicateds(f3)

print("Correct answers = " + str(correct_answers))
print("Wrong answers = " + str(wrong_answers))
blanks = 20-(correct_answers+wrong_answers)
print("blanks = " + str(blanks))
    
f1.close()
f2.close()
f3.close()


tkMessageBox.showinfo("Informacao","Correcao finalizada com sucesso! \n\n Respostas corretas: " + str(correct_answers) + "\n Respostas incorretas: " + str(wrong_answers) + "\n Respostas em branco: " + str(blanks))
