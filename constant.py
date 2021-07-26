# CONSTANTS
TEEN_LIST = range( 13, 20 ) #range function need end value with addition of 1
NON_TEEN_LIST = [ 15, 16 ]
ACTUAL_TEEN_LIST = list( set( TEEN_LIST ) - set( NON_TEEN_LIST ) )
ERROR_MSG_INVALID_COUNT_ARGS = 'Exactly 3 numbers are required'
ERROR_MSG_INVALID_INPUT = 'All inputs must be numeric'
ARGS_ALLOWED = 3
