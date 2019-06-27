python orb.py "../img/pi_cam/testA1.png" "../img/im_filtered/filteredA1.jpg"

python pre_processing.py "../img/im_filtered/filteredA1.jpg" "../img/ROI/img_roiA1.jpg"

python process_gabarito.py "../img/ROI/img_roiA1.jpg" "../answers/answersA1.csv"

python correction.py '../answers/answersA1.csv' '../gabarito/answers.csv'





python orb.py "../img/pi_cam/testC1.png" "../img/im_filtered/filteredC1.jpg"

python pre_processing.py "../img/im_filtered/filteredC1.jpg" "../img/ROI/img_roiC1.jpg"

python process_gabarito.py "../img/ROI/img_roiC1.jpg" "../answers/answersC1.csv"

python correction.py '../answers/answersC1.csv' '../gabarito/answers.csv'




python orb.py "../img/pi_cam/testC2.png" "../img/im_filtered/filteredC2.jpg"

python pre_processing.py "../img/im_filtered/filteredC2.jpg" "../img/ROI/img_roiC2.jpg"

python process_gabarito.py "../img/ROI/img_roiC2.jpg" "../answers/answersC2.csv"

python correction.py '../answers/answersC2.csv' '../gabarito/answers.csv'

