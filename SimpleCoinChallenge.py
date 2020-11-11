
for goal in range(20):
  total = 0
  for ones in range(goal+1):
    for twos in range(int(goal/2)+1):
      for fives in range(int(goal/5)+1):
        for tens in range(int(goal/10)+1):
          sumn = ones + twos*2 + fives*5
          if sumn == goal:
            total += 1
            #print(ones, twos, fives)
  print(str(goal) + "p can be done in " + str(total) + " ways")
