import orb
import pre_processing
import process_gabarito
import correction

import sys

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
parser.add_argument('res_path', type=str,
                  help="Enter destination for aligned img")

args = parser.parse_args()



sys.argv = ['orb.py', args.ans_path,"../img/im_filtered/filteredA1.jpg"]
execfile('orb.py')

#subprocess.call(['./orb.py', ans_path,"../img/im_filtered/filteredA1.jpg"])
#python orb.py "../img/pi_cam/testA1.png" "../img/im_filtered/filteredA1.jpg"

sys.argv = ['pre_processing.py', "filteredA1.jpg","../img/ROI/img_roiA1.jpg"]
execfile('pre_processing.py')

#subprocess.call(['pre_processing.py', "../img/im_filtered/filteredA1.jpg","../img/ROI/img_roiA1.jpg"])
#python pre_processing.py "../img/im_filtered/filteredA1.jpg" "../img/ROI/img_roiA1.jpg"


sys.argv = ['process_gabarito.py', "../img/ROI/img_roiA1.jpg", "../answers/answersA1.csv"]
execfile('process_gabarito.py')

#subprocess.call(['process_gabarito.py', "../img/ROI/img_roiA1.jpg", "../answers/answersA1.csv"])
#python process_gabarito.py "../img/ROI/img_roiA1.jpg" "../answers/answersA1.csv"

sys.argv = ['correction.py', '../answers/answersA1.csv', '../gabarito/answers.csv']
execfile('correction.py')

#subprocess.call(['correction.py', '../answers/answersA1.csv', '../gabarito/answers.csv'])
#python correction.py '../answers/answersA1.csv' '../gabarito/answers.csv'
