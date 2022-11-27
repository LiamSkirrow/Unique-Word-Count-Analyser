# read in a text file and analyse the word composition... get unique word count for txt files

# TODO: sort the words by frequency in the dictionary and display...

fileName = 'HP&PhilStone-ES.txt'
stripChars = "‘,.-—?!»«0123456789()"

if __name__ == "__main__":
    wordFreqPairDict = {}
    print("Opening file: '" + fileName + "' for analysis...")
    with open(fileName, 'r') as f:
        for line in f.readlines():
            for word in line.split():
                ret = wordFreqPairDict.get(word.lower().strip(stripChars), 'EMPTY')
                # if no key equal to 'word' is available, set to 1
                if(ret == 'EMPTY'):
                    wordFreqPairDict.update({word.lower().strip(stripChars) : 1})
                # otherwise increment value by 1 and store back
                else:
                    ret += 1
                    wordFreqPairDict.update({word.lower().strip(stripChars) : ret})
    
    print(wordFreqPairDict.items())
    print('\n')
    print("Total unique word count: " + str(len(wordFreqPairDict.items())))
    print("Total non-unique word count: " + str(sum(wordFreqPairDict.values())))