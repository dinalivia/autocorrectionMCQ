python otsu.py "../img/pi_cam/scan2.jpg" "../img/im_filtered/filtered1.jpg"

python pre_processing.py "../img/im_filtered/filtered1.jpg" "../img/ROI/img_roi1.jpg"

python process_gabarito.py "../img/ROI/img_roi1.jpg" "../answers/answers1.csv"

python correction.py '../answers/answers1.csv' '../gabarito/answers.csv'