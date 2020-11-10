total = 0
for one in range(200):
  for two in range(100):
    for five in range(40):
      for ten in range(20):
        for twenty in range(10):
          for fifty in range(4):
            for pound in range(2):
              for twoPound in range(1):
                sumn = one + 2*two + 5*five + 10*ten + 20*twenty + 50*fifty + 100*pound + 200*twoPound
                if sumn == 200:
                  total += 1
                  print(one, two, five, ten, twenty, fifty, pound, twoPound)
print("total amount =", total)
