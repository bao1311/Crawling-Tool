import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# library needed to print a text box
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# Added GUI
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Please insert your web you want me to crawl for you'
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(200,20)
        self.textbox.resize(200,40)
        
        # Create show text button in the window
        self.button = QPushButton('Enter url', self)
        self.button.move(250,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        url = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + url, QMessageBox.Ok, QMessageBox.Ok)
        self.homepage = url
        self.textbox.setText("")
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    # Start the GUI
    app.exec_()

    #Using GUI to enter a text box

    HOMEPAGE = ex.homepage
    PROJECT_NAME = get_project_name(HOMEPAGE)
    DOMAIN_NAME = get_domain_name(HOMEPAGE)
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    NUMBER_OF_THREADS = 8
    queue = Queue()
    Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# # Create worker threads (will die when main exits)
# def create_workers():
#     for _ in range(NUMBER_OF_THREADS):
#         t = threading.Thread(target=work)
#         t.daemon = True
#         t.start()


# # Do the next job in the queue
# def work():
#     while True:
#         url = queue.get()
#         Spider.crawl_page(threading.current_thread().name, url)
#         queue.task_done()


# # Each queued link is a new job
# def create_jobs():
#     for link in file_to_set(QUEUE_FILE):
#         queue.put(link)
#     queue.join()
#     crawl()


# # Check if there are items in the queue, if so crawl them
# def crawl():
#     queued_links = file_to_set(QUEUE_FILE)
#     if len(queued_links) > 0:
#         print(str(len(queued_links)) + ' links in the queue')
#         create_jobs()


# create_workers()
# crawl()
