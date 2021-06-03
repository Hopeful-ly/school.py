import json
import webbrowser as wb
import time
import pyperclip as pc
import datetime
from datetime import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
import threading
import sys
import os


def dayDefiner(day):
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    elif day == 6:
        return "Sunday"
    else:
        return "Not Defined"


class mainWindowUi(object):
    def __init__(self, mainWindow):
        mainWindow.setObjectName("MainWindow")
        mainWindow.resize(531, 331)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet("background-color: #343233;")

        # setting Up the Central QtWidgets
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # the vertical Layout Widgets Creation
        self.vlw = QtWidgets.QWidget(self.centralWidget)
        self.vlw.setGeometry(QtCore.QRect(310, 20, 181, 211))
        self.vlw.setObjectName("vlw")

        # the vertical Layout Creation
        self.vl = QtWidgets.QVBoxLayout(self.vlw)
        self.vl.setContentsMargins(0, 0, 0, 0)
        self.vl.setObjectName("vl")

        # setting up the Fonts
        font = QtGui.QFont()
        font.setFamily(
            "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,"
            "Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(37)

        # creating the Label
        self.A1 = QtWidgets.QLabel(self.vlw)
        self.A1.setFont(font)

        # styling the 'Today Is Monday' Text
        self.A1.setStyleSheet("    font: 25px/1.5 normal normal;\n"
                              "font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Helvetica, Arial, "
                              "sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\";\n "
                              "    font-weight: 300;\n"
                              "    color: #efdab9;\n"
                              "    background-color: #343233;\n"
                              "text-align: center;")
        self.A1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.A1.setObjectName("A1")
        self.vl.addWidget(self.A1)

        # creating the clock label
        self.A2 = QtWidgets.QLabel(self.vlw)

        # styling the clock label
        self.A2.setStyleSheet("    font: 25px/1.5 normal normal;\n"
                              "font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Helvetica, Arial, "
                              "sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\";\n "
                              "    font-weight: 300;\n"
                              "    color: #efdab9;\n"
                              "    background-color: #343233;\n"
                              "text-align: center;")
        self.A2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.A2.setObjectName("A2")
        self.vl.addWidget(self.A2)

        # creating the Editing Button
        self.Edit = QtWidgets.QPushButton(self.vlw)

        # styling the Button
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue,Helvetica,arial,freesans,clean,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(62)
        font.setStrikeOut(False)
        self.Edit.setFont(font)
        self.Edit.setStyleSheet("background-color: rgb(253, 219, 58);\n"
                                "font: 25px/1.7 normal normal;\n"
                                "font-family: \"Helvetica Neue\", Helvetica, arial, freesans, clean, sans-serif;\n"
                                "display: inline-block;\n"
                                "padding: .5em 1em;\n"
                                "line-height: inherit;\n"
                                "font-size: inherit;\n"
                                "font-weight: 500;\n"
                                "text-decoration: none;\n"
                                "border-radius: 5px;\n"
                                "color: #343233;\n"
                                "background-color: #ffd152;\n"
                                "")
        self.Edit.setObjectName("Edit")
        self.vl.addWidget(self.Edit)

        # creating the second vertical Layout Widget
        self.vlw_2 = QtWidgets.QWidget(self.centralWidget)
        self.vlw_2.setGeometry(QtCore.QRect(40, 20, 219, 211))
        self.vlw_2.setObjectName("vlw_2")
        self.vl_2 = QtWidgets.QVBoxLayout(self.vlw_2)
        self.vl_2.setContentsMargins(0, 0, 0, 0)
        self.vl_2.setObjectName("vl_2")

        # creating the 'Next lesson is' label
        self.A3 = QtWidgets.QLabel(self.vlw_2)

        # styling the label
        font = QtGui.QFont()
        font.setFamily(
            "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,"
            "Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(37)
        self.A3.setFont(font)
        self.A3.setStyleSheet("    font: 25px/1.5 normal normal;\n"
                              "font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Helvetica, Arial, "
                              "sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\";\n "
                              "    font-weight: 300;\n"
                              "    color: #efdab9;\n"
                              "    background-color: #343233;\n"
                              "text-align: center;")
        self.A3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.A3.setObjectName("A3")
        self.vl_2.addWidget(self.A3)

        # creating the 'Starts In' label
        self.A4 = QtWidgets.QLabel(self.vlw_2)
        self.A4.setMaximumSize(QtCore.QSize(16777198, 16777215))

        # styling the label
        font = QtGui.QFont()
        font.setFamily(
            "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,"
            "Segoe UI Symbol")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(37)
        self.A4.setFont(font)
        self.A4.setStyleSheet("    font: 25px/1.5 normal normal;\n"
                              "font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Helvetica, Arial, "
                              "sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\";\n "
                              "    font-weight: 300;\n"
                              "    color: #efdab9;\n"
                              "    background-color: #343233;\n"
                              "text-align: center;")
        self.A4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.A4.setObjectName("A4")
        self.vl_2.addWidget(self.A4)

        # creating the (time left) label
        self.timeLeft = QtWidgets.QLabel(self.vlw_2)

        # styling the label
        self.timeLeft.setStyleSheet("    font: 25px/1.5 normal normal;\n"
                                    "font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Helvetica, Arial, "
                                    "sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\";\n "
                                    "    font-weight: 300;\n"
                                    "    color: #efdab9;\n"
                                    "    background-color: #343233;\n"
                                    "text-align: center;")
        self.timeLeft.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeLeft.setObjectName("timeLeft")
        self.vl_2.addWidget(self.timeLeft)

        # creating the reminder label
        self.remind = QtWidgets.QLabel(self.centralWidget)
        self.remind.setGeometry(QtCore.QRect(20, 270, 241, 21))

        # styling the label
        self.remind.setStyleSheet("    font: 10px/1.5 normal normal;\n"
                                  "font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Helvetica, Arial, "
                                  "sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\";\n "
                                  "    font-weight: 300;\n"
                                  "    color: #efdab9;\n"
                                  "    background-color: #343233;\n"
                                  "text-align: center;")
        self.remind.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.remind.setObjectName("remind")
        mainWindow.setCentralWidget(self.centralWidget)

        # creating the MenuBar
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menuBar.setObjectName("menuBar")
        mainWindow.setMenuBar(self.menuBar)

        # creating the StatusBar
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)

        # calling the translate Ui
        self.translateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def translateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("MainWindow", "Timer"))
        self.A1.setText(_translate("MainWindow", "Monday"))
        self.A2.setText(_translate("MainWindow", "Not Set"))
        self.Edit.setText(_translate("MainWindow", "Edit"))
        self.A3.setText(_translate("MainWindow", "Next Lesson"))
        self.A4.setText(_translate("MainWindow", "Starts"))
        self.timeLeft.setText(_translate("MainWindow", "In Few Minutes?"))

        self.Edit.clicked.connect(lambda: os.startfile('C:/Users/himas/PycharmProjects/School.Py/data.json'))

    def setTime(self, Time):
        self.A2.setText(Time)

    def setDay(self, Day):
        self.A1.setText(f"{Day}")

    def setNoLeft(self):
        self.A3.setText("")
        self.A4.setText("No Lessons :D")
        self.timeLeft.setText("")

    def setTimeLeft(self, Time, Hours):
        now = datetime.now()
        hour = now.strftime("%H")
        minutes = now.strftime("%M")
        if hour[0:1] == '0':
            hour = hour[1:2]
        if minutes[0:1] == '0':
            minutes = minutes[1:2]
        hour = int(hour)
        minutes = int(minutes)

        if Hours == hour and Time > minutes:
            self.A3.setText("Next Lesson")
            self.A4.setText("Starts")
            self.timeLeft.setText(f'in {Time - minutes} Minutes')

        elif Time == minutes and Hours == hour:
            self.A3.setText("Next Lesson")
            self.A4.setText("Starts")
            self.timeLeft.setText("Right Now")

        elif Hours > hour and Time > minutes:
            self.A3.setText("Next Lesson")
            self.A4.setText("Starts")
            self.timeLeft.setText(f'in {Hours - hour}h and {Time - minutes}m')

        elif Hours > hour and Time == minutes:
            self.A3.setText("Next Lesson")
            self.A4.setText("Starts")
            self.timeLeft.setText(f'in {Hours - hour} Hours')

        elif Hours == hour + 1 and Time < minutes:
            self.A3.setText("Next Lesson")
            self.A4.setText("Starts")
            self.timeLeft.setText(f'in {abs(Time + 60 - minutes)} Minutes')

        elif Hours > hour and Time < minutes:
            self.A3.setText("Next Lesson")
            self.A4.setText("Starts")
            self.timeLeft.setText(f'in {Hours - hour - 1}h and {abs(Time + 60 - minutes)}m')

        elif Hours < hour:
            pass

        elif Hours == hour and Time < minutes:
            pass

        else:
            print("Something's Wrong with setTimeLeft()")

    def signIn(self, meetingLink):
        wb.open(meetingLink)
        pc.copy(meetingLink)
        self.A3.setText("")
        self.A4.setText("Link Copied!")
        self.timeLeft.setText("")
        time.sleep(2)
        self.A3.setText("Next Lesson")
        self.A4.setText("Starts")

    def scheduler(self):
        while True:
            with open('C:/Users/himas/PycharmProjects/School.Py/data.json', 'r') as json_file:
                today = str(datetime.today().weekday())
                data = json.load(json_file)
                now = datetime.now()
                exact_time = str(now.strftime("%H:%M"))
                for i in data['days'][today]:
                    if exact_time == i:
                        meeting_link = (data['days'][today][exact_time])
                        self.signIn(meeting_link)
                        time.sleep(60)
                if stop_threads:
                    break
                time.sleep(1)

    def timerdisplay(self):
        while True:
            now = datetime.now()
            exact_time = str(now.strftime("%H:%M:%S"))
            self.setTime(exact_time)
            time.sleep(1)
            global stop_threads
            if stop_threads:
                break

    def timeLeftDefiner(self):
        while True:
            with open('C:/Users/himas/PycharmProjects/School.Py/data.json', 'r') as json_file:
                data = json.load(json_file)
                today = str(datetime.today().weekday())
                now = datetime.now()
                f_lessons = []
                hours = now.strftime("%H")
                minutes = now.strftime("%M")
                if hours[0:1] == '0':
                    hours = hours[1:2]
                if minutes[0:1] == '0':
                    minutes = minutes[1:2]
                hours = int(hours)
                minutes = int(minutes)

                for i in data['days'][today]:
                    x_hours = i[0:2]
                    x_minutes = i[3:5]
                    if x_hours[0:1] == 0:
                        x_hours = x_hours[1:2]
                    if x_minutes[0:1] == 0:
                        x_minutes = x_minutes[1:2]
                    x_hours = int(x_hours)
                    x_minutes = int(x_minutes)

                    if x_hours == hours and x_minutes == minutes:
                        self.setTimeLeft(0, 0)
                    elif x_hours < hours:
                        pass
                    elif x_hours >= hours:
                        if x_hours == hours and x_minutes >= minutes:
                            f_lessons.append(i)
                        elif x_hours == hours and x_minutes < minutes:
                            pass
                        elif x_hours > hours:
                            f_lessons.append(i)
                        else:
                            print('Something is wrong in timeLeftDefiner()')
                smallest = f_lessons[0] if f_lessons else None
                for x in f_lessons:
                    x_hours = x[0:2]
                    x_minutes = x[3:5]
                    smallest_hour = smallest[0:2]
                    smallest_minute = smallest[3:5]
                    if smallest_hour[0:1] == 0:
                        smallest_hour = smallest_hour[1:2]
                    if smallest_minute[0:1] == 0:
                        smallest_minute = smallest_minute[1:2]
                    if x_hours[0:1] == 0:
                        x_hours = x_hours[1:2]
                    if x_minutes[0:1] == 0:
                        x_minutes = x_minutes[1:2]
                    x_hours = int(x_hours)
                    x_minutes = int(x_minutes)
                    smallest_hour = int(smallest_hour)
                    smallest_minute = int(smallest_minute)
                    if x_hours < smallest_hour:
                        smallest = x
                    elif x_hours == smallest_hour:
                        if x_minutes < smallest_minute:
                            smallest = x
                        else:
                            pass
                    else:
                        pass
                try:
                    if not f_lessons:
                        self.setNoLeft()
                    else:
                        final_hour = smallest[0:2]
                        final_minute = smallest[3:5]
                        if final_hour[0:1] == 0:
                            final_hour = final_hour[1:2]
                        if final_minute[0:1] == 0:
                            final_minute = final_minute[1:2]
                        final_hour = int(final_hour)
                        final_minute = int(final_minute)
                        self.setTimeLeft(final_minute, final_hour)
                except Exception as Ex:
                    print(Ex)
                if stop_threads:
                    break
                time.sleep(1)

    def daySetter(self):
        today = int(datetime.today().weekday())
        day = dayDefiner(today)
        self.setDay(day)


if __name__ == '__main__':
    # and here I run everything...
    stop_threads = False
    app = QtWidgets.QApplication(sys.argv)
    app_icon = QtGui.QIcon()
    app_icon.addFile('Bcon.png')
    app.setWindowIcon(app_icon)

    MainWindow = QtWidgets.QMainWindow()
    ui = mainWindowUi(MainWindow)
    ui.daySetter()
    timer = threading.Thread(target=ui.timerdisplay)
    timer.start()
    schedul = threading.Thread(target=ui.scheduler)
    schedul.start()
    lefttimer = threading.Thread(target=ui.timeLeftDefiner)
    lefttimer.start()
    MainWindow.show()
    ret = app.exec_()
    stop_threads = True
    sys.exit(ret)
