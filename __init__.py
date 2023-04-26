# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

from anki import decks

class FetchPronunciationWindow(QMainWindow):
     def __init__(self):
        super().__init__()

        self.setWindowTitle("fetchPronunciation")
        
        # Fetch all decks by name and add them to the dropdown bar for the user to select.
        allDecksByName = mw.col.decks.all_names() # maybe I should get by id as well. What happens if the user has decks of the same name? Users fault.
        userDecksComboBox = QComboBox()
        userDecksComboBox.setPlaceholderText("Select deck from options below.")
        for deck in allDecksByName:
         userDecksComboBox.addItem(str(deck))

        whichCardSide = QComboBox()
        whichCardSide.setPlaceholderText("Select Front or Back.")
        whichCardSide.addItem("Front")
        whichCardSide.addItem("Back")
        
        e1 = QLineEdit("Enter language of deck as 2 letters. See forvo api demo. https://api.forvo.com/demo")
        e1.setMaxLength(100)
        #e1.setAlignment(Qt.AlignLeft)
        #e1.editingFinished.connect(self.enterPress)
        
        # deckName, done2 = QInputDialog.getText(
        #     self, 'Input Dialog', 'Enter your desired deck name: ')


        # redoButton = QPushButton("Re-enter.")
        # Set the central widget of the Window. Need to learn to put this in bottom right
        # flo = QFormLayout()
        # flo.addRow("Language of Deck: ", e1)
        # flo.addButton(continueButton)
        #self.setLayout(flo)
        # self.setCentralWidget(continueButton)

        layout = QVBoxLayout()
        layout.addWidget(userDecksComboBox)
        layout.addWidget(whichCardSide)
        layout.addWidget(e1)        
        continueButton = QPushButton("Continue.")
        
        layout.addWidget(continueButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        continueButton.clicked.connect(checkAllFieldsEntered(layout))
        
def checkAllFieldsEntered(layout: QVBoxLayout):
   if True:
     showInfo(str(layout[QComboBox]))
   elif layout[QComboBox][0]:
    showInfo("button is working.")
   elif layout[QComboBox][1]:
    pass
   elif True:
    pass
   elif True:
    pass
   elif True:
    pass
   else:
    # everything is entered correctly. close the widget and get all pronunciations/
    showinfo("Please select a deck.")
    return
   

def fetchPronunciation():
    mw.myWidget = widget = FetchPronunciationWindow()
    widget.show()








# create a new menu item, "fetchPronunciationForSet"
action = QAction("fetchPronunciationForSet", mw)

# set it to call fetchPronouciationForSet when it's clicked
qconnect(action.triggered, fetchPronunciation)

# and add it to the tools menu
mw.form.menuTools.addAction(action)