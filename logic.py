def calculate_sum( args, ACTUAL_TEEN_LIST ):
  # check the input list and filter out non teen values in the list and return the sum
  return sum( [ item for item in args if item not in ACTUAL_TEEN_LIST ] )
