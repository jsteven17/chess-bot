##########################################
#--------------interface.py--------------#
##########################################

#-------------Description----------------#
# Takes algebraic chess notation ex: be4 and passes it in the
# correct notation to the chess engine so the game state can be updated.
# Returns the computer's move also in the form of algebraic chess
# notation.

#-----------Input Arguments--------------#
# 1. Algebraic chess notation ex: be4 as a string

#-----------Output Arguments-------------#
# 1. Algebraic chess notation ex: be4 as a string

#----------Implementation Map------------#
# The first step to implementing this part of the program is
# determining all of the possible inputs to the chess engine (Arena Chess
# using Stockfish). When a string is entered, the program will determine whether
# any string interpolation is necessary, and if so perform it. This process may
# have to be based on the current game state in which case a separate class will
# need to be created to contain said information. Finaly, the program will inject
# the move via command line script to the engine and scan for the output move or
# resulting error. This information will then become the output argument.
