import string
with open("Day6\\poem.txt","r")as f:
    word_count={}
    #copied some of this off google mental note to read on it
    for line in f:
        # remove punctuations off string
        line = "".join(char for char in line if char not in string.punctuation)
        str_list = line.split()

        for word in str_list:
            if word not in word_count:
                word_count[word] =1
            else:  word_count[word] = word_count[word]+1       

#list only the word count
listed_count = list(word_count.values())
max_word = max(listed_count)
print(max_word)
# print all the words with max number
for word,count in word_count.items():
    if count == max_word:
        print('This word "%s" occurred %s times .It had the maximum occurrence' % (word,count))
