import os
import jsonParse
import markov
import igbot
dir_path = os.path.dirname(os.path.realpath(__file__))

entry = True
while(entry):
    choice = input('''
1. Enter new username, password and image name
2. Import chat log (JSON)
3. Generate captions
4. Publish next caption
Press any other key to exit
''')

    if choice=="1":
        username = input("Enter the username:\n")
        password = input("Enter the password:\n")
        image = input("Enter the name with extension of the image you want to upload every time (optional, press x to skip)\n")
        config = open(dir_path+"\config.txt", "w+", encoding="utf-8")
        if image!='x':
            config.writelines([username+"\n", password+"\n", image])
        else:
            config.writelines([username+"\n", password])
        config.close()
    elif choice=="2":
        name = input("Enter the name from the JSON file (Enter letter x for help)\n")
        if name == "x":
            print("You can open the JSON file by right clicking on it and opening it in notepad. You will see a huge text which represents the conversation between you and the other person. Copy the name from the 'Name' field and paste it here\n")
            name = input()
        jsonParse.parse(name, dir_path)
    elif choice=="3":
        stateStr = input("Enter the state size (Number of words the probability of a next word depends on). Recommended: 2 or 3\n")
        state = int(stateStr)
        markov.doTheMarkov(dir_path, state)
    elif choice=="4":
        readConfig = open(dir_path+"\config.txt", "r", encoding="utf-8")
        cred = readConfig.readlines()
        if len(cred)==3:
            imgName = cred[2]
        else:
            imgName = input("Enter the name of an image you want to upload (with the file extension):\n")
        igbot.postIt(cred[0], cred[1], imgName, dir_path)
    else:
        entry = False
