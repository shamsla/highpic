import requests,sys,os,shutil
from pynput.keyboard import Key,Listener
from random import randrange
def io_f():
    if os.path.isfile('appSLI.confs') == False:
        if os.path.isdir("appSLI.confs") == True:
            if os.path.isdir('dist') == True:
                shutil.rmtree('dist')
            os.mkdir('dist')
            shutil.copytree('appSLI.confs','dist/application')
            shutil.rmtree('appSLI.confs')
        open('appSLI.confs','a').close
io_f()
def check_dir(address):
    if os.path.isdir(rf"{address}") == True:
        return True
    return False


def changeDIR(string):
    while True:
        n_dir = input(f"\n{string}")
        if n_dir == '.e':
            sys.exit("Program Ended...\n")
        if check_dir(n_dir) == True:
            io_f()
            with open("appSLI.confs",'w') as f:
                f.write(rf"{n_dir}")
            break
        else:
            print("\n\tInvalid Directory!")
            continue
    
def identifier():
    io_f()
    with open("appSLI.confs",'r') as f:
        data = f.read()
        if len(data) == 0:
            changeDIR("Enter directory for storing images:")
            data = f.read()
        if check_dir(data) == False:
            print("\n\tStored Directory is not valid!")
            changeDIR('Enter directory again:')
identifier()

integer = 0
def on_press(k):
    global integer
    if k == Key.enter:
        integer = 1
        return False
    if k != Key.enter:
        integer = 2
        return False

terminator = 1
def exitNot(string):
    global terminator
    if terminator != 0:
        while True:
            userInput = input(string)
            store = 0
            if userInput == ".ls":
                print("\n\tYou can use these commands in any INPUT.\n\t.change : change directory\n\t.res : restart program\n\t.e : end program\n\t(Example: **  Enter Width:.e  **)\n")
                continue
            elif userInput == ".gs":
                print("\n\tMust Read\n**  Width and Height must be greater or equal to 20.\n**  (Best Dimesions: 100x100, 500x500, 1600x900, 1920x1080, 3840x2160)\n\n**  Main Keyword can be a collection of many Sub Keywords.\n**  (Example: Main Keyword:nature - Sub Keyword:water)\n\n**  or You can make different manipulations Like:\n**  (Main Keyword:car - Sub Keyword:car)\n**  (Main Keyword:house - Sub Keyword:cat)\n**  (Main Keyword:car - Sub Keyword:jaguar)\n  At the end of program you can press any button to exit program\n")
                continue
            elif userInput == ".e":
                sys.exit("Program Ended...\n")
            elif userInput == ".change":
                changeDIR('Enter new directory:')
                print()
                continue
            elif userInput == ".res":
                terminator = 0
                print()
                break
            try:
                if string[-4] == 'r':
                    return userInput
                elif string[-4] == 'a':
                    return int(userInput)
                else:
                    store += int(userInput)
            except:
                print("\n\tInvalid Input!\n")
                continue
            if store >= 20:
                return store
            else:
                print(f"\n\t{string[6:-1]} must be GREATER or EQUAL to 20!\n")
def getter():
    io_f()
    identifier()
    with open('appSLI.confs','r') as f:
        return f.read()

print("\n\tshamasgujjar7861@gmail.com\n\tEnter .ls to show all COMMANDS\n\tEnter .gs for GUIDELINES\n")
while True:
    terminator = 1
    width= exitNot("Enter Width :")
    height = exitNot("Enter Height :")
    key1 = exitNot("Enter Main Keyword :")
    key2 = exitNot("Enter Sub Keyword :")
    iteration = exitNot("How Many Images You Want To Download :")
    if terminator == 0:
        continue
    try:
        for i in range(1,iteration+1):
            print(f"\n\tDownloading Image-{i}...",end="\n\n")
            data = requests.get(f"https://source.unsplash.com/{width}x{height}/?{key1},{key2}")
            if os.path.isdir(f"{getter()}\\HighPic-Images") == False:
                os.mkdir(f"{getter()}\\HighPic-Images")
            with open(f"{getter()}\\HighPic-Images\\{key1.capitalize()}-{key2.capitalize()}-HighPic_{randrange(1213,100000000000000)}.jpg","wb") as image:
                image.write(data.content)
            print(f"Image-{i} Downloaded Successfuly.")
    except:
        print("\n\tAn Unknown Error Occured!\n\tCheck Your Internet Connection ???")
        identifier()

    print("\n\tPress ENTER to run again:",end="")
    with Listener(on_press=on_press) as listener:
        listener.join()
    if integer == 1:
        input("\n")
        continue
    else:
        print("\nProgram Ended...\n")
        break
