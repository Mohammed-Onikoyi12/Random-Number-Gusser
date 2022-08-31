import random
numtoguess= random.randint(0, 100)
gueesd = int(input('Guess a number'))
while numtoguess != gueesd:
 gueesd=int(input('Guess a number'))
 if gueesd == numtoguess:
  print('Nice')
 else :
  print('wrong try again')
