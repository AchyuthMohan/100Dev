
from PyQt5.QtWidgets import QApplication
import os
import webbrowser

os.system('cls ')


def take_screenshot():
    os.system('tree ')
    app = QApplication([])
    screen = app.primaryScreen()
    screenshot = screen.grabWindow(QApplication.desktop().winId())
    screenshot.save('screenshot.png')


def generate_doc():
    directories = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
    print("\n\n\n\n ********")
    os.system('pdoc --html beyound ')
    # for directory in directories:
    #     if directory not in ['.git', 'html']:
    #         print("pdoc --html"+directory)

    #         break
    # files = [d for d in os.listdir(os.getcwd()) if os.path.isfile(d)]
    # os.system('pdoc --html '+directories[2])
    # for file in files:
    #     if file not in ['.env', '.gitignore']:
    #         os.system('pdoc --html '+file)
    #         break


def add_img_to_doc():
    file_path = "html/a/index.html"

    with open(file_path) as f:
        s = f.read()

    img_tag = "<img src='../../screenshot.png' />"

    s = s.replace('<h2 class="section-title" id="header-submodules">',
                  img_tag+'<h2 class="section-title" id="header-submodules">')
    with open(file_path, "w") as f:
        f.write(s)


def main():
    take_screenshot()
    generate_doc()
    add_img_to_doc()
    webbrowser.open("http://127.0.0.1:5500/html/a/index.html")


main()
