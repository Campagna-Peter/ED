import array as arr
import numpy as np

def ED(word1, word2):
    if word1 == "":
        return len(word2)
    if word2 == "":
        return len(word1)
    if word1[-1] == word2[-1]:
        cost = 0
    else:
        cost = 1
        
    totalED = min([ED(word1[:-1], word2)+1,
                ED(word1, word2[:-1])+1, 
                ED(word1[:-1], word2[:-1]) + cost])

    return totalED

def main(misspelled, threshold):
    file=open("dictionary.txt","r")
    words = file.read().splitlines() #puts the file into an array
    file.close()
    arr = []
    smallest = []
    final = []

    for i in range(len(words)):
        if(len(misspelled) > len(words[i])):
            arr.append(ED(words[i], misspelled)) 
        else:
            arr.append(ED(misspelled, words[i]))

    arr2 = np.array(arr)
    arr3 = np.argpartition(arr2,5)

#threshold
    for i in range(5):
        temp = arr3[i]
        if(arr[temp] <= threshold):
            smallest.append(arr3[i])

    for i in range(len(smallest)):
        temp = smallest[i]
        final.append(words[temp])

    return final



print(main("catz", 2))
print(ED("watrmelon", "watermelon"))
