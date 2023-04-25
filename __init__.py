# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *


class FetchPronunciationWindow(QMainWindow):
     def __init__(self):
        super().__init__()

        self.setWindowTitle("fetchPronunciation")
        e1 = QLineEdit("Enter language of deck.")
        e1.setMaxLength(20)
        e1.setAlignment(Qt.AlignLeft)
        e1.setFont(QFont("Arial",14))
        #e1.editingFinished.connect(self.enterPress)
        
        # deckName, done2 = QInputDialog.getText(
        #     self, 'Input Dialog', 'Enter your desired deck name: ')

        continueButton = QPushButton("Continue.")
        # redoButton = QPushButton("Re-enter.")
        # Set the central widget of the Window. Need to learn to put this in bottom right
        flo = QFormLayout()
        flo.addRow("Language of Deck: ", e1)
        # flo.addButton(continueButton)
        #self.setLayout(flo)
        # self.setCentralWidget(continueButton)

def fetchPronunciation():
    mw.myWidget = widget = FetchPronunciationWindow()
    widget.show()








# create a new menu item, "fetchPronouciationForSet"
action = QAction("fetchPronouciationForSet", mw)

# set it to call fetchPronouciationForSet when it's clicked
qconnect(action.triggered, fetchPronouciation)

# and add it to the tools menu
mw.form.menuTools.addAction(action)