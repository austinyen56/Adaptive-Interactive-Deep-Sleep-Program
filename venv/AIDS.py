"""
ADAPTIVE INTERACTIVE DEEP SLEEP ALARM
1/19/2020


AUSTIN YEN
TED IKEHARA
CARL VINCENT CUYOS
"""
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pafy
import pygame
import shutil
from tkinter.filedialog import askdirectory
import random
from tkinter import *
import time
from os import path
from PIL import ImageTk, Image

def addSong(): #Experimental as of rn
    x = input('Do you want to add a new song? (Type y/n)')
    if x == 'y':
        song_url = input('Enter song url:')
        v = pafy.new(song_url)
        print(v.title)
        s = v.getbestaudio()
        s.download(filepath=r"C:\Users\Austin\Desktop\Wake Up Carl\venv\download")
        print("Size is %s" % s.get_filesize())
        print('Successfully downloaded {}.webm'.format(v.title))
        destination = input('Where do you wanna move this file to?')

        orig = r'C:\Users\Austin\Desktop\Wake Up Carl\venv\download'
        if destination == 1:
            copyTo = r'C:\Users\Austin\Desktop\Wake Up Carl\Playlist\1'
        if destination == 2:
            copyTo = r'C:\Users\Austin\Desktop\Wake Up Carl\Playlist\2'
        if destination == 3:
            copyTo = r'C:\Users\Austin\Desktop\Wake Up Carl\Playlist\3'
        if destination == 4:
            copyTo = r'C:\Users\Austin\Desktop\Wake Up Carl\Playlist\4'
        print(copyTo)
        for root, subdirs, files, in os.walk(orig):
            print(files)
            for file in files:
                path = os.path.join(root, file)
                shutil.move(path, copyTo)
    if x == 'n':
        print('Oke')


addSong()

def entertext():
    global hour
    global min

    global wakeHour
    wakeHour = int(hour.get())
    global wakeMin
    wakeMin = int(min.get())

    global sleep1
    global sleep2
    global sleep3
    global sleep4
    global sleep5
    global sleep6

    global stage
    stage = 0

    global propCT
    global propWT

    global propSleep1
    global propSleep2
    global propSleep3
    global propSleep4
    global propSleep5
    global propSleep6

    global amountCycle

    global ct
    global wt

    ct = int(time.time())
    wt = (wakeHour * 3600) + (wakeMin * 60) + ct
    amountCycle = (wt - ct) / 6000

    if amountCycle >= 1:
        sleep1 = ct + 6000
        if amountCycle >= 2:
            sleep2 = sleep1 + 6000
            if amountCycle >= 3:
                sleep3 = sleep2 + 6000
                if amountCycle >= 4:
                    sleep4 = sleep3 + 6000
                    if amountCycle >= 5:
                        sleep5 = sleep4 + 6000
                        if amountCycle >= 6:
                            sleep6 = sleep5 + 6000
                        else:
                            sleep6 = 0
                    else:
                        sleep5 = 0
                        sleep6 = 0

                else:
                    sleep4 = 0
                    sleep5 = 0
                    sleep6 = 0

            else:
                sleep3 = 0
                sleep4 = 0
                sleep5 = 0
                sleep6 = 0
        else:
            sleep2 = 0
            sleep3 = 0
            sleep4 = 0
            sleep5 = 0
            sleep6 = 0
    else:
        sleep1 = 0
        sleep2 = 0
        sleep3 = 0
        sleep4 = 0
        sleep5 = 0
        sleep6 = 0

    propCT = time.localtime(ct)
    propWT = time.localtime(wt)

    propSleep1 = time.localtime(sleep1)
    propSleep2 = time.localtime(sleep2)
    propSleep3 = time.localtime(sleep3)
    propSleep4 = time.localtime(sleep4)
    propSleep5 = time.localtime(sleep5)
    propSleep6 = time.localtime(sleep6)

    initial = int(((wt - ct) / amountCycle) * 4)
    sleepstage = int(initial / amountCycle)

    #print(sleepstage)

    if sleepstage <= ((wt - ct) / amountCycle):
        stage = 1
    if ((wt - ct) / amountCycle) < sleepstage < ((wt - ct) / amountCycle)*2:
        stage = 2
    if ((wt - ct) / amountCycle)*2 < sleepstage < ((wt - ct) / amountCycle)*3:
        stage = 3
    if ((wt - ct) / amountCycle)*3 < sleepstage <= ((wt - ct) / amountCycle)*4:
        stage = 4

    root.destroy()


root = Tk()

root.title('Adaptive Interactive Deep Sleep Alarm')

text = Label(root, text="In how many hours do you want to wake up?")
text.pack()

text = Label(root, text="What minute of the hour do you want to wake up?")
text.pack()

hour = Entry(root)
hour.pack(side='left')
hour.focus_set()
hr_txt = Label(root, text='<-- Hours')
hr_txt.pack(side='left')

min = Entry(root)
min.pack(side='left')
min.focus_set()
min_text = Label(root, text='<-- Minutes')
min_text.pack(side='left')

b = Button(root, text='Okay', command=entertext)
b.pack(side='bottom')

root.mainloop()

str1 = "The amount of sleep cycles you will go through: " + str(int(amountCycle))
str2 = "Current time is: " + time.strftime("%I:%M:%S %p", propCT)
str3 = "Waking time is: " + time.strftime("%I:%M:%S %p", propWT)
#str4 = "The current seconds is: " + str(ct)
#str5 = "The waking seconds is: " + str(wt) + '\n'
str6 = "You are recommended to wake up at these times: "
divider = "-----------------------------------------------------------"
str7 = "Sleep cycle 1: " + time.strftime("%I:%M:%S %p", propSleep1)
str8 = "Sleep cycle 2: " + time.strftime("%I:%M:%S %p", propSleep2)
str9 = "Sleep cycle 3: " + time.strftime("%I:%M:%S %p", propSleep3)
str10 = "Sleep cycle 4: " + time.strftime("%I:%M:%S %p", propSleep4)
str11 = "Sleep cycle 5: " + time.strftime("%I:%M:%S %p", propSleep5)
str12 = "Sleep cycle 6: " + time.strftime("%I:%M:%S %p", propSleep6)

str13 = "You will wake up at sleep stage: " + str(stage)
str14 = "Your level of music:"

str15 = "Level 1: Calm music will be played"
str16 = "Level 2: Energetic music will be played"
str17 = "Level 3: Loud and forceful music will be played"
str18 = "WARNING: This is a bad time to wake up"
str19 = "Level 4: Ear rape will be played **CAUTION: May cause ear bleeding"

root2 = Tk()

root2.title('Adaptive Interactive Deep Sleep Alarm')

sec = time.time()
localtime = time.localtime(sec)

#str0 = "The Current local time is: " + time.strftime("%I:%M:%S %p", localtime)

#text0 = Label(root2, text=str0)
text1 = Label(root2, text=str1)
text2 = Label(root2, text=str2)
text3 = Label(root2, text=str3)
#text4 = Label(root2, text=str4)
#text5 = Label(root2, text=str5)
text6 = Label(root2, text=str6)
linetext = Label(root2, text= divider)

#text0.pack()
text1.pack()
text2.pack()
text3.pack()
#text4.pack()
#text5.pack()
text6.pack()
linetext.pack()


if sleep1 != 0:
    text7 = Label(root2, text=str7)
    text7.pack()
if sleep2 != 0:
    text8 = Label(root2, text=str8)
    text8.pack()
if sleep3 != 0:
    text9 = Label(root2, text=str9)
    text9.pack()
if sleep4 != 0:
    text10 = Label(root2, text=str10)
    text10.pack()
if sleep5 != 0:
    text11 = Label(root2, text=str11)
    text11.pack()
if sleep6 != 0:
    text12 = Label(root2, text=str12)
    text12.pack()

text13 = Label(root2, text=str13)
text14 = Label(root2, text=str14)

text13.pack()
text14.pack()
if stage == 0:
    text15 = Label(root2, text=str15)
    text15.pack()
if stage == 1:
    text15 = Label(root2, text=str15)
    text15.pack()
if stage == 2:
    text16 = Label(root2, text=str16)
    text16.pack()
if stage == 3:
    text17 = Label(root2, text=str17)
    text17.pack()
if stage == 4:
    text18 = Label(root2, text=str18)
    text19 = Label(root2, text=str19)
    text18.pack()
    text19.pack()

next = Button(root2, text='Click here to start', fg="blue",command=root2.destroy)
next.pack(side='bottom')

root2.mainloop()

root3 = Tk()
root3.title('Adaptive Interactive Deep Sleep Alarm')
root3.minsize(0,0)
time1 = ''
clock = Label(root3, font=('times', 40, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)
current = time.localtime()

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

count = 0
def counter():
    global count
    while count < (wt - ct):
        root3.update()  # allow window to catch up
        time.sleep(1)
        print(count,'/',wt-ct,'(',abs(count-(wt-ct)),'seconds left)')
        count += 1

counter()
print(count)

"""
input the functions for playing music here
"""

listofsongs = []
index = random.randrange(5)
#needed for directorychooser()
if stage == 0 or stage == 1:
    pl = r'C:\Users\Austin\Desktop\Wake Up Carl\Playlist\1'
if stage == 2:
    pl = r'C:\Users\Austin\Desktop\Wake Up Carl\Playlist\2'
if stage == 3:
    pl = r'C:\Users\Austin\Desktop\Wake Up Carl\Playlist\3'
if stage == 4:
    pl = r'C:\Users\Austin\Desktop\Wake Up Carl\Playlist\4'

def directorychooser():
    directory = pl
    os.chdir(directory)
    print(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    print('Currently Playing:',listofsongs[index])
directorychooser()


#root3.minsize(500,500)
songPlaying = '【Currently Playing:】 ' + listofsongs[index]
photo = PhotoImage(file=r"C:\Users\Austin\Desktop\Wake Up Carl\venv\banane slug.png")
#photoimage = photo.subsample(2, 2)
Label(root3, text='', image=photo,compound=CENTER).pack(side=TOP)

endText = Label(root3, fg="red",font=('times', 30, 'bold'), text= '【WAKE UP NOW!!!!!!】')
endText.pack(side ='top')

terminate = Button(root3, text='EXIT', fg="red", command=root3.destroy)
terminate.pack(side='bottom')

currentSong = Label(root3,font=('times', 15),text = songPlaying)
currentSong.pack(side= 'bottom')


def buttonPress(event):
    global running
    running = True
    print("幹你娘趕快起來啦")

def buttonRelease(event):
    global running
    print("幹你娘趕快起來啦")
    running = False

button = Button(root3, text ="")
button.pack(side=LEFT)
button.bind('<ButtonPress-1>',buttonPress)
button.bind('<ButtonRelease-1>',buttonRelease)

#print(current)
#print(propWT)

root3.update()
tick()
root3.mainloop()
