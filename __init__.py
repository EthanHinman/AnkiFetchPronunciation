# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

from anki import decks

from forvoAPIKey import forvoAPIKeyVariable

from anki.collection import Collection

import os
#############################################
# This is your forvo API key. 
class FetchPronunciationWindow(QMainWindow):
     def __init__(self):
        super().__init__()

        self.setWindowTitle("fetchPronunciation")
        
        # Fetch all decks by name and add them to the dropdown bar for the user to select.
        allDecksByName = mw.col.decks.all_names() # maybe I should get by id as well. What happens if the user has decks of the same name? Users fault.
        userDecksComboBox = QComboBox(objectName="userDecksComboBox")
        userDecksComboBox.setPlaceholderText("Select deck from options below.")
        for deck in allDecksByName:
         userDecksComboBox.addItem(str(deck))

        # A dropdown bar that lets the user select which side of the flashcard deck to modify.
        whichCardSide = QComboBox(objectName="whichCardSide")
        whichCardSide.setPlaceholderText("Select Front or Back.")
        whichCardSide.addItem("Front")
        whichCardSide.addItem("Back")
        
        # An input box where the user will enter the language of the cards to-be-modified. 
        languageInputWidget = QLineEdit("Enter language of deck as 2 letters. See forvo api demo. https://api.forvo.com/demo",objectName="languageInput")
        languageInputWidget.setMaxLength(100)

        # Add all widgets into one central widget. We also add a continue button.
        layout = QVBoxLayout()
        layout.addWidget(userDecksComboBox)
        layout.addWidget(whichCardSide)
        layout.addWidget(languageInputWidget)        
        continueButton = QPushButton("Continue.")
        layout.addWidget(continueButton)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # When the continue button is clicked, checkAllFieldsEntered is called to make sure all input is valid.
        continueButton.clicked.connect(lambda: checkAllFieldsEntered(userDecksComboBox, whichCardSide, languageInputWidget))

# INPUT: A widget where the user inputted deckName, cardSide, and languageOfDeck.
# RETURN: Bool that dictates if the the input is valid.
# FUNCTIONALITY: This function will check the inputted widget to make sure that all input into it is valid.
#   Valid input for a deckName is considered non-placeholder-text.
#   Valid input for cardSide is non-placeholder-text.
#   Valid input for language is a 2 char string that matches a language.
def checkAllFieldsEntered(userDecksComboBox: QComboBox, whichCardSide :QComboBox, languageInputWidget:QLineEdit)-> bool: 
   # TODO: This is erroring and stating that userDecksComboBox is NoneType. Need to figure out how to check the input.
   # Grab the three widgets that the user must input.
  inputValid = True
  if userDecksComboBox.currentText() == "":
    showInfo("Please select a deck.")
    inputValid = False
  if whichCardSide.currentText() == "":
    showInfo("Please select a side of the deck to modify.")
    inputValid = False
  if len(languageInputWidget.text()) != 2:
    showInfo("Please enter a 2 digit language input for the desired pronouciation.")
    inputValid = False
  if inputValid:
    # everything is entered correctly. close the widget and get all pronunciations/
    showInfo("All input is valid. We are obtaining pronouciation.")

    # open up the deck by name and iterate over all cards.
    deckManagerObject = decks.DeckManager(mw.col)
    listCardId = deckManagerObject.cids(mw.col.decks.by_name(userDecksComboBox.currentText())['id'])
    for cardId in listCardId:
       fetchPronunciationForCard(cardId, languageInputWidget.text().lower(), whichCardSide.currentText() )
    return

# INPUT: A card from a deck.
# RETURN: Bool that dictates if an error occured fetching the pronouciation.
# FUNCTIONALITY: This function will contact the forvo api with a word. The function will
#   then modify the card and update it with the pronouciation, if it exists. Otherwise it will showInfo and return false.
def fetchPronunciationForCard(cardId: int, language: str, cardSide: str)-> bool:
  # Fetch the word from the side of the card that the user specifies
  card = mw.col.get_card(cardId)
  word = ""
  if cardSide == "Front":
    word = card.note().items()[0][1]
    showInfo(str(word))
  else:
    word = card.note().items()[1][1]
    showInfo(str(word))
  
  # contact the forvo api to see if a pronouciation exists.
  # https://api.forvo.com/documentation/standard-pronunciation/
  formattedRequestString = "https://apifree.forvo.com/key/" + forvoAPIKeyVariable + "/format/json/action/standard-pronunciation/word/" + word + "/language/" + language
  # showInfo(formattedRequestString)
  # audioLink = requests.get(formattedRequestString)

    # if the pronouciation exists, download it and add it to the card. Delete the downloaded pronouciation after it is applied to the card.
    # if the pronouciation DOES NOT exist, then use showinfo(word) stating that we ran into an error fetching this pronouciation
  pass

# INPUT: NONE.
# RETURN: NONE.
# FUNCTIONALITY: 
def fetchPronunciation():
    mw.myWidget = widget = FetchPronunciationWindow()
    widget.show()








# create a new menu item under addOns, "fetchPronunciationForSet"
action = QAction("fetchPronunciationForSet", mw)

# set it to call fetchPronouciationForSet when it's clicked
qconnect(action.triggered, fetchPronunciation)

# and add it to the tools menu.
mw.form.menuTools.addAction(action)