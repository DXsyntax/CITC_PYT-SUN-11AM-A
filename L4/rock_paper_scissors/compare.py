def is_draw(p_guess, c_guess):
  if p_guess == c_guess:
    # print(f'computer and player drew the same {p_guess} & {c_guess}')
    return True 
  else:
    return False 

def player_is_winner(p_guess, c_guess):
  if p_guess == "rock" and c_guess == "scissors":
    # this line works
    # print(f'player drew {p_guess}, computer drew {c_guess}')
    return True 
  elif p_guess == "paper" and c_guess == "rock":
    return True
  elif p_guess == "scissors" and c_guess == "paper":
    return True 
  else: 
    # this line works as well
    # print(f'player drew {p_guess}, computer drew {c_guess}')
    # print(f'most likely draw')
    return False
    



