from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

#maghimo_main_window
def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(500, 100, 200, 300)
    window.setWindowTitle("Practice GUI")

    label = QLabel(window)
    label.setText("hello world")
    label.setFont(QFont("Arial", 16))
    label.move(3, 3)

    label_1 = QLabel(window)
    label_1.setText("my new world")
    label_1.setFont(QFont("Arial", 16))
    label_1.move(3, 30)

#maghimog_layout
    # layout = QVBoxLayout()
    # label = QLabel("press the box below")


#mag_create_push_button
    #button = QPushButton("Press here")


    #widget_sa_button_ug_layout
    # layout.addWidget(label)
    # layout.addWidget(button)

    #window.setLayout(layout)




    window.show()
    app.exec()

if __name__ == '__main__':
    main()