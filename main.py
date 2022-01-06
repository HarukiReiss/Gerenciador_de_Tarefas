from model.database import createDB
from qt_core import *
from controller.main_window import MainWindow

os.environ['XDG_SESSION_TYPE'] = 'Wayland'

app = QApplication(sys.argv)

createDB()

win = MainWindow()
win.show()
sys.exit(app.exec())
