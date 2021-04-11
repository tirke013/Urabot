from instabot import Bot
import pathlib

def postIt(u, p, i, path):
    bot = Bot()
    bot.login(username = u.strip(), password = p.strip(), use_cookie=False)

    fileReader = open(path+"\publishQueue.txt", "r", encoding = "utf-8")
    captions = fileReader.readlines()

    fileWriter = open(path+"\publishQueue.txt", "w", encoding = "utf-8")
    index = int(captions[0])
    if(index!=0):
        newcaption = captions[index]
        index = index + 1
        captions[0] = index
        for c in captions:
            fileWriter.write(str(c))
            if isinstance(c, int):
                fileWriter.write("\n")
    else:
        newcaption = None

    bot.upload_photo(path+ "\\" + i, caption = newcaption, options={"rename":False})
    #pathForRenaming = path + "\\" + i + ".REMOVE_ME"
    #os.rename(path + "\\" + i + ".REMOVE_ME", path + "\\" + i)
