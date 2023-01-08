from mongoApi import newProject

def openWindow(self, targetWindow):
    self.window = Qtwidgets.QMainWindow()
    self.ui = targetWindow
    self.ui.setupUi(self.window)
    self.window.show()

def closeWindow(window):
    window.close()

def createProject(window, title, abbv, code):
    newProject(title, abbv, code)
    window.close()