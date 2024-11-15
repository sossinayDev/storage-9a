from json import load, loads
from os import listdir
from pyperclip import copy
from time import sleep

melodies = []
notes = load(open("namehz.json"))

triggerchars = "NCTS"

possiblesongs = listdir("songs")

i=1
print("\n\n\nSongs:")
for item in possiblesongs:
    print(str(i)+": "+item)
    i+=1
ans = 0
while not ans:
    try:
        ans = int(input("Enter number of song:\n"))
        if ans > len(possiblesongs):
            1/0
        if ans < 1:
            1/0
    except:
        print("Invalid.")
        ans = 0
    else:
        pass

song_name = False
song_composer = False
tl = [3,4]
speed = 100
song = possiblesongs[ans-1]
print("Importing song...")
for line in open("songs/"+song).readlines():
    if line[0] == "N":
        song_name = line.removeprefix("N ").strip()
    elif line[0] == "C":
        song_composer = line.removeprefix("C ").strip()
    elif line[0] == "T":
        tl = line.replace("T ", "").split("/")
        beat = [int(tl[0]), int(tl[1])]
    elif line[0] == "S":
        speed = int(line.replace("S ", "0"))

for e in range(50):
    print()

if not song_name:
    song_name = song.removesuffix(".sng")
if not song_composer:
    song_composer = "Unknown"
print("\nSelcted song: "+song_name)
print("== BY "+song_composer.upper()+" ==")

player_speed_val = 1

print("\n\nProcessing...\n")
sleep(1)
for line in open("songs/"+song).readlines():
    if not line.strip() == "":
        if line[0] == "#":
            pass
        elif line[0] in triggerchars:
            pass
        elif line[0] == "I":
            print("INSTRUMENT SWITCH!")
        else:
            mel = []
            last_elem = "-"
            i = 0
            done = False
            while not done:
                char = line[i].upper()
                if char == "-":
                    mel.append(0)
                    last_elem = "-"
                elif char == "_":
                    mel.append(last_elem)
                elif char == ":" or i >= len(line)-1:
                    done = True
                else:
                    if i < len(line)-1:
                        if line.upper()[i]+line.upper()[i+1] in list(notes.keys()):
                            freq = notes[line[i].upper()+line[i+1].upper()]
                            mel.append(freq)
                            mel.append(freq)
                            last_elem = freq
                i += 1
            melodies.append(mel)

i = ""
for item in melodies:
    copy(f"m{i} = {item}")
    print(f"Export complete. Copied part {i} to clipboard")
    if i == "":
        i=2
    else:
        i+=1
    input()