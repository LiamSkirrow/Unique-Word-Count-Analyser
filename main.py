# read in a text file and analyse the word composition... get unique word count for txt files

from ankiaccess import invoke
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, required=True)
parser.add_argument("-d", "--dump",       nargs="?", default=False, const=True, required=False)
parser.add_argument("-p", "--printdecks", nargs="?", default=False, const=True, required=False
                    , help="leave blank for list of available decks")
parser.add_argument("-c", "--compare",  type=str, required=False
                    , help="Name of Anki deck to be compared")

args = parser.parse_args()
filename     = args.filename
dump         = args.dump
compare      = args.compare
printdecks   = args.printdecks

# TODO: somehow check if filename was read correctly more elegantly than just failing the open()

# chars to strip out of the words before processing
stripChars = "‘,.-—?!»«0123456789()"

if __name__ == "__main__":
    wordFreqPairDict = {}
    print("Opening file: '" + filename + "' for analysis...")
    with open(filename, 'r') as f:
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
    
    # TODO: make this dump a bit prettier in the terminal, maybe one line per dict entry
    if(dump):
        print(wordFreqPairDict.items())
    print('\n')
    print("Total unique word count: " + str(len(wordFreqPairDict.items())))
    print("Total non-unique word count: " + str(sum(wordFreqPairDict.values())))

    # check if we're printing out the available deck names
    if(printdecks):
        result = invoke('deckNames')
        print(*result, sep='\n')
    # check if we're comparing the supplied file with the Anki deck
    # FIXME: currently this is only for one card, need to iterate over each card in the deck
    #        and splice out the front+back entries and add to a dict. Then do the cross check
    if(compare):
        print("\nFetching deck " + compare + "...")
        # form the dictionary required containing the deck name
        deckNameDict = { 'query' : 'deck:'+compare }
        # perform a findCards operation using the given deck name
        foundCardsIds = invoke('findCards', query='deck:current')
        print(foundCardsIds[0])
        cardsInfo = invoke('cardsInfo', cards=[foundCardsIds[0]])
        print(str(cardsInfo))


# TODO:
# - figure out how to pass the deck name through the command line rather than relying on 
#   deck:current
