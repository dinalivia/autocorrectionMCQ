# -------------------------------------
# Answersheet autocorrection
# --
#
# Developed by Dina Livia - 10.06.2019
# --------------------------------------

#!/usr/bin/python

# Standard imports
import csv


f1 = open('../answers/answers.csv', 'r')
f2 = open('../gabarito/answers.csv','r')
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

print("Correct answers = " + str(correct_answers))
print("Wrong answers = " + str(wrong_answers))
    
f1.close()
f2.close()
f3.close()
