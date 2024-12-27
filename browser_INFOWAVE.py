# Importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

# Creating main window class
class MainWindow(QMainWindow):

    # Constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Creating a QWebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))

        # Adding actions when URL gets changed
        self.browser.urlChanged.connect(self.update_urlbar)

        # Adding actions when loading is finished
        self.browser.loadFinished.connect(self.update_title)

        # Set this browser as central widget of the main window
        self.setCentralWidget(self.browser)

        # Creating a status bar object
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # Creating QToolBar for navigation
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        # Adding actions to the tool bar
        # Back button
        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        # Forward button
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        # Reload button
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # Home button
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # Adding a separator in the tool bar
        navtb.addSeparator()

        # Creating a line edit for the URL
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        # Stop button
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # Set the window icon (replace 'icon.png' with the path to your icon)
        self.setWindowIcon(QIcon('InfoWave Logo.jpeg'))

        # Showing all the components
        self.show()

    # Method for updating the title of the window
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(f"{title} - InfoWave")

    # Method called by the home action
    def navigate_home(self):
        self.browser.setUrl(QUrl("InfoWave Logo.jpeg"))

    # Method called by the line edit when return key is pressed
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())

        # Set URL scheme to http if it is blank
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    # Method for updating the URL
    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

# Creating a PyQt5 application
app = QApplication(sys.argv)
app.setApplicationName("InfoWave")

# Creating a main window object
window = MainWindow()

# Loop
sys.exit(app.exec_())
