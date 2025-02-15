# Unique-Word-Count-Analyser
A script that looks through a *.txt file and determines the total number of unique words.

## TODO
- make the file passable via the command line rather than being hardcoded in the program itself
- maybe allow for the reading of pdf files natively? Rather than having to manually convert to txt
- parse a supplied Anki deck (somehow?) and figure out how many unique words are in a supplied text that do *not* appear
  in the Anki deck. In other words... given this/these Anki deck(s) what is my level of vocab coverage in the supplied text?
- print out the unique words in the supplied text that are not present in the Anki deck(s) and...
  - ...stretch task: autogenerate an Anki deck consisting of these unfamiliar unique words
  
### Dev Notes
- install AnkiConnect
- access Anki over HTTP API via Python methods
- the Anki part of the program should run as follows:
  - do 'deckNames' to get the names of all the decks available, displaying all to the screen, user enters a number to select the deck
  - do 'findCards' to get the card IDs in the user-selected deck, internally store in a list
  - do 'cardsInfo' to get the actual card front/back vocabulary information. Add to internally stored dict (therefore storing front+back information)
  - can finally cross check between the Anki and supplied text vocab
  
