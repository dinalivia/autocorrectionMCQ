GAB=$1
ANS=$2


python orb.py "$ANS" "../img/im_filtered/filteredA1.jpg"

python pre_processing.py "../img/im_filtered/filteredA1.jpg" "../img/ROI/img_roiA1.jpg"

python process_gabarito.py "../img/ROI/img_roiA1.jpg" "../answers/answersA1.csv"

python correction.py "../answers/answersA1.csv" "$GAB"x
