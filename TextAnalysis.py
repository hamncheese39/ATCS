import urllib.request
import matplotlib.pyplot as plt
import numpy as np

#directories of every book in my computer
doll = "/Users/haharrell/Documents/ATCS/TextAnalysisBooks/a_dolls_house.txt"
frankenstein = "/Users/haharrell/Documents/ATCS/TextAnalysisBooks/frankenstein.txt"
scarlett = "/Users/haharrell/Documents/ATCS/TextAnalysisBooks/scarlett_letter.txt"
meta = "/Users/haharrell/Documents/ATCS/TextAnalysisBooks/metamorphosis.txt"
pride = "/Users/haharrell/Documents/ATCS/TextAnalysisBooks/pride_and_prejudice.txt"

def remove_items(list, item): 
      
    # using list comprehension to perform the task 
  res = [i for i in list if i != item] 
  
  return res

def get_dictionary():
    dic = []
    for a in open("/Users/haharrell/Documents/ATCompSci/dictionary.txt").readlines():
        dic.append(a.strip())
    return(dic)

#Gets the list of words ranked in order of commonality in the list of [WORD, integer of appearances in all books]
def get_ranks():
    string = get_text_url("http://norvig.com/google-books-common-words.txt")
    ranks = []
    splitted = string.splitlines()
    for rank in splitted:
        
        ranks.append(rank.lower().split('\t'))
    return ranks

    
#Goes through the whole .txt file and compiles every word (with punctuation and everything still)
def get_words(directory):
    with open(directory, encoding = "utf-8") as a:
        words = []
        for line in a:
            for word in line.split():
                words.append(word)
    return words

#Returns the given word with only the letters, put into lowercase
def clean_word(word):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cleanedWord = ""
    for letter in word:
        if letter.lower() in alphabet:
            cleanedWord += letter.lower()
    return cleanedWord

#Takes list of words and cleans every one of them, returning the cleaned list        
def clean_words(words):
    cleanedWords = []
    for i in range(len(words)):
        #In The Scarlet Letter, there would be words written on both sides of a dash so I had to split those into two separate words
        if "—" in words[i]:
            splitted = words[i].split('—')
            cleanedWords.append(clean_word(splitted[0]))
            cleanedWords.append(clean_word(splitted[1]))
        elif "-" in words[i]:
            splitted = words[i].split('-')
            cleanedWords.append(clean_word(splitted[0]))
            cleanedWords.append(clean_word(splitted[1]))
        else:
            cleanedWords.append(clean_word(words[i]))
    return remove_items(cleanedWords, "")
            


def get_text_url(url):
    file = urllib. request. urlopen(url)
    encoded_text = file.read()
    decoded_text = encoded_text.decode("utf-8")
    return decoded_text

#I decided not to use many functions because I like the linearity of coding in this way
def main():
    dic = get_dictionary()
    ranks = get_ranks()
    #gets just the words in the correct order of commonality
    rankWords = []
    for rank in ranks:
        rankWords.append(rank[0])
    

    books = [frankenstein, pride, scarlett, doll, meta]
    avgIndY = []
    obscPerY = []
    for book in books:
        dirtyWords = get_words(book)
        words = clean_words(dirtyWords)

        #will have the sum of the index of every word in the ranks list
        indexSum = 0
        #number of words which are in ranks
        count = 0
        #number of words which aren't in ranks
        strangeCount = 0
        for word in words:
            if word in rankWords:
                indexSum += rankWords.index(word)
                count += 1
            else:
                strangeCount += 1
                
        print(book[-1*book[::-1].index("/"):])

        avgIndY.append(indexSum/count)
        obscPerY.append(strangeCount/len(words)*100)
        print("average index =", indexSum/count)
        print("obscure word % =", strangeCount/len(words)*100)


    x = ["Frankenstein", "Pride and Prejudice", "The Scarlett Letter", "A Doll's House", "Metamorphosis"]
    x_pos = range(5)
    
    plt.bar(x_pos, avgIndY, color='b', align='center', label = "average index")
    plt.xticks(range(5), x)
    plt.xlabel("Book")
    plt.ylabel("Average index in list of top ~100,000 most common words")
    plt.title("Average commonality of words in Top 5 most common .txt file books (higher is more obscure)")
    plt.show()

    plt.bar(x_pos, obscPerY, color = 'g', label = "percent of words not in 100,000 most common of Google Books")
    plt.xticks(range(5), x)
    plt.xlabel("Book")
    plt.ylabel("Percent of words not in top 100,000 most common (%)")
    plt.title("Percent of words in Top 5 most common .txt file books which are not in the top 100,000 most common words in Google Books")
    plt.show()
        
print(get_ranks()[1950:1958])
#main()






