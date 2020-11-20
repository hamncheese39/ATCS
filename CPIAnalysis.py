url = "http://nancymcohen.com/csci133/cpiai.txt"
import urllib.request

def get_text(url):
	file = urllib. request. urlopen(url)
	encoded_text = file.read()
	decoded_text = encoded_text.decode("utf-8")
	return decoded_text

def get_data():
  return get_text(url)[1129:]

data = get_data()
years = {}

for line in data.split("\n"):
  splitted = line.split()
  floats = []
  for val in splitted[1:13]:
    floats.append(float(val))
  if splitted != []:
    years[int(splitted[0])] = floats

print("What year and months would you like to find")

ask = []
for n in input().split():
  ask.append(int(n))
  
if len(ask) == 1:
  string = ""
  for monthVal in years[ask[0]]:
    string += str(monthVal) + " "
  print(string)
  print("average =", sum(years[ask[0]])/12)
else:
  total = 0
  string = ""
  for month in ask[1:]:
    string += str(years[ask[0]][month-1]) + " "
    total += years[ask[0]][month-1]
  print(string)
  print(total/(len(ask)-1))
  

