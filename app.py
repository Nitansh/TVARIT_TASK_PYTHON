# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13...19
# inclusive -- then that value counts as 0, except 15 and 16 do not count as a teen. The input is passed as
# command line arguments and output is to be printed on screen
import sys

from constant import ACTUAL_TEEN_LIST, ERROR_MSG_INVALID_INPUT, ERROR_MSG_INVALID_COUNT_ARGS, ARGS_ALLOWED
from validation import validate_arguments_length, get_converted_args
from logic import calculate_sum

if __name__ == "__main__":
  args = sys.argv
  actual_args = args[ 1: ] #ARGS also include the filename of python file
  if validate_arguments_length( actual_args, ARGS_ALLOWED ):
    if get_converted_args( actual_args ):
      print( calculate_sum( get_converted_args( actual_args ), ACTUAL_TEEN_LIST ) )
    else :
      print ( ERROR_MSG_INVALID_INPUT )
  else:
    print( ERROR_MSG_INVALID_COUNT_ARGS )
