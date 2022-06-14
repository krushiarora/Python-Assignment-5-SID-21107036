#Define empty list
word_list = []

#Ask user for number of inputs they want in list
list_elements = int(input("Enter total words you want to have in list: "))


#Ask user for the words and add them in list
for num in range (list_elements):
    word_inp = input("Enter word: ")
    #Append list with each word
    word_list.append(word_inp)
    

#Ask the user for the word for which they want number of occurrences

check_word = input("Enter the word to be checked: ")

#Assign variable to occurance of the input word and print
occurance = word_list.count(check_word)
print(check_word, "occurs", occurance, "times")
