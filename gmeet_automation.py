import webbrowser
import schedule
import pyautogui
import time
from datetime import datetime

meeting_time = "12:03:00"


def alert_msg():
    date_format = "%H:%M:%S"
    meet_time = str(meeting_time)
    current_time = str(datetime.now().strftime("%H:%M:%S"))
    diff = datetime.strptime(meet_time, date_format) - \
        datetime.strptime(current_time, date_format)
    print(meet_time, current_time)
    result = diff.seconds
    print(result)
    if result <= 60:
        pyautogui.alert(text='The meeting would start in a minute',
                        title='Info')


def join_meeting():

    meetingID = "sgs-jjpk-svk"
    webbrowser.open_new_tab('https://meet.google.com/?authser=0')

    pyautogui.press('enter', interval=0.5)
    time.sleep(3)

    pyautogui.click(250, 520)
    time.sleep(1)
    pyautogui.typewrite(meetingID, interval=0.2)
    time.sleep(1)
    pyautogui.press('enter', interval=0.2)
    time.sleep(2)

    pyautogui.click(400, 570)
    time.sleep(2)
    pyautogui.click(500, 570)
    time.sleep(2)

    pyautogui.alert(text='Entering the meeting', title='Info', button='OK')
    time.sleep(1)
    pyautogui.click(990, 440)
    print("Asked to join")


schedule.every().day.at(meeting_time).do(join_meeting)
alert_msg()
while True:

    schedule.run_pending()
    time.sleep(1)
