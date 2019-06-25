python orb.py "../img/pi_cam/cam7.png" "../img/im_filtered/filtered4.jpg"

python pre_processing.py "../img/im_filtered/filtered4.jpg" "../img/ROI/img_roi4.jpg"

python process_gabarito.py "../img/ROI/img_roi4.jpg" "../answers/answers4.csv"

python correction.py '../answers/answers4.csv' '../gabarito/answers4.csv'
