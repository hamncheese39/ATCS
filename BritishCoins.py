total = 0
for ones in range(201):
  sumn = 1*ones
  for twos in range(int((200-sumn)/2)+1):
    sumn = 1*ones + 2*twos
    for fives in range(int((200-sumn)/5)+1):
      sumn = 1*ones + 2*twos + 5*fives
      for tens in range(int((200-sumn)/10)+1):
        sumn = 1*ones + 2*twos + 5*fives + 10*tens
        for twenties in range(int((200-sumn)/20)+1):
          sumn = 1*ones + 2*twos + 5*fives + 10*tens + 20*twenties
          for fifties in range(int((200-sumn)/50)+1):
            sumn = 1*ones + 2*twos + 5*fives + 10*tens + 20*twenties + 50*fifties
            for pounds in range(int((200-sumn)/100)+1):
              sumn = 1*ones + 2*twos + 5*fives + 10*tens + 20*twenties + 50*fifties + 100*pounds
              #print(sumn, ones, twos, fives, tens, twenties, fifties, pounds)
              if sumn == 200:
                total += 1
                if total % 1000 == 0:
                  print("good!", ones, twos, fives, tens, twenties, fifties, pounds)

total += 1 #for the one with just two pounds              
print("total amount =", total)
