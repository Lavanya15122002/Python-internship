import os
import shutil
path = r"D:/ct/Level3/"
file = os.listdir(path)
folder = ['Excel Files', 'Image Files', 'Ppt Files', 'Text Files', 'Word Files']
for i in range(0, len(folder)):
    if not os.path.exists(path + folder[i]):
        print(path + folder[i])
        os.makedirs(path + folder[i])
for i in file:
    if ".xlsx" in i and not os.path.exists(path + "Excel Files/" + i):
        shutil.move(path+i, path + "Excel Files")
    elif ".png" in i and not os.path.exists(path + "Image Files/" + i):
        shutil.move(path+i, path + "Image Files")
    elif ".ppt" in i and not os.path.exists(path + "Ppt Files/" + i):
        shutil.move(path+i, path + "Ppt Files")
    elif ".txt" in i and not os.path.exists(path + "Text Files/" + i):
        shutil.move(path+i,path + "Text Files")
    elif ".doc" in i and not os.path.exists(path + "Word Files/" + i):
        shutil.move(path+i, path + "Word Files")
    else:
        print("No more files to move")