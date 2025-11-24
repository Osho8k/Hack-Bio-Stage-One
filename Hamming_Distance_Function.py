slack_username = "Aseghiemhe"
twitter_handle = "_Oshoreame"


def hamming_distance_calculator():
  hamming_distance = sum(slack != twitter for slack, twitter  in zip(slack_username, twitter_handle))

  #Slack and twitter are used as the variable names representing slack_username and twitter_handle to avoid repitition.
  return(hamming_distance)


print(f"Hamming distance between '{slack_username}' and '{twitter_handle}' is: {hamming_distance}")
