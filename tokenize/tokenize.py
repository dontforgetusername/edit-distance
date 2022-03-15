import re

dictionaryFiles = ["", "one.txt", "two.txt", "three.txt", "four.txt", "five.txt", "six.txt", "seven.txt", "eight.txt", "nine.txt"]
output = "output.txt"

def readFile(filename):
    f = open(filename, "r", encoding="utf8")
    x = f.read()
    return x

#check if item[position]...item[position + num_syllables - 1] is in dictionary
def isInDictionary(num_syllables, position, *sentence):
    word = sentence[0][position]
    for i in range(num_syllables - 1):
        word = word + ' ' + sentence[0][position + i + 1]
    with open(dictionaryFiles[num_syllables], 'r', encoding='utf8') as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        if word in lines:
            return True
        else:
            return False



def tokenize(text):
    #split sentence with regex
    sentencesList = re.split(r'(?<![A-Z]{2}[a-z]\.)(?<![A-Z][a-z][A-Z]\.)(?<![A-Z]{3}\.)(?<![A-Z]{2}\.)(?<=\.|\?|\!)\s', text)
    
    #visit each sentence
    for sentence in sentencesList:
        #eliminate ending punctuation
        punctuation = ''
        if sentence[len(sentence) - 1] == '.' or sentence[len(sentence) - 1] == '?' or sentence[len(sentence) - 1] == '!':
            punctuation = sentence[len(sentence) - 1]
            sentence = sentence[:-1]

        #split sentence by space
        queue = sentence.split()
        position = 0

        #visit till the end of the sentence
        while True:
            #add ending mark to the end of sentence
            if len(queue) == 0:
                with open(output, 'a', encoding='utf8') as f:
                    f.write("%s\n" % punctuation)
                break
            elif len(queue) == 1:
                word = queue.pop(0) + ' ' + punctuation
                with open(output, 'a', encoding='utf8') as f:
                    f.write("%s\n" % word)
                break

            #max syllables from begining of the queue
            num_syllables = 9
            if len(queue) < 9:
                num_syllables = len(queue)
            
            #while loop check if string exists in 9-8-...-2 dictionary 
            while num_syllables > 1:
                if isInDictionary(num_syllables, position, queue):
                    word = queue.pop(0)
                    for i in range(num_syllables - 1):
                        word = word + '_' + queue.pop(0)

                    word = word + ' '
                    with open(output, 'a', encoding='utf8') as f:
                        f.write("%s" % word)
                    break
                
                else:
                    num_syllables = num_syllables - 1

            #if string not in 9-...-2
            if num_syllables == 1:
                word = queue.pop(0) + ' '
                with open(output, 'a', encoding='utf8') as f:
                    f.write("%s" % word)






#input.txt
input_file = input("Nhap file input: ")
text = readFile(input_file)
tokenize(text)

        