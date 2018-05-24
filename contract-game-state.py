##########################################
#-------------game-state.py--------------#
##########################################

#-------------Description----------------#
# Keeps a copy of the current state of the chess game in
# the form of an 8x8 matrix containing the charachters 'B', 'W',
# and 'N' for black piece, white piece, and 

#-----------Input Arguments--------------#
# 1. 300 ms worth of image captures from the imaging hardware
#    roughly 5 images.

#-----------Output Arguments-------------#
# 1. The corner coordinates in a plain text document
#    one tuple per line separated by new lines.
#    EX: (1,45)
#        (5,56)
#        (102, 320)
#        (233, 456)

#-----------Design Phase 1---------------#
# Create the coordinate mapping algorithm using 3 sets of 5 test images
# (not actually live polling with the imaging hardware)

#-----------Design Phase 2---------------#
# Add in code that poles the desired amount of times within 300 ms.

#----------Implementation Map------------#
# This is the second hardest part of the back end part of the
# Python side of the project. A reliable algorithm needs to be found and
# Implemented using OpenCV to detect and plot the lines on the chessboard
# without erroneously adding false lines or missing actual lines. In order
# to accomplish this, a combination of edge detection, corner detection, and
# software prediction based on the fact that once certain lines are identified,
# other lines on the chessboard will likely exist in other locations. In essence,
# the algorithm will know that the end plot will have 18 evenly spaced lines
# thus it only needs to map this idealized model onto the actual image.
# Good places to start on this are with the Shi Tomasi and Harris corner
# detection algorithms.
