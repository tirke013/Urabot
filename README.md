# NAME

Basically, the name Urabot is an internal joke which I chose to actually keep as the name of the project. No secret messages or whatever.

# WHAT DOES URABOT DO?

Urabot allows you to parse the text from a chat with your friend (works for exported Instagram chat and Facebook if I remember correctly), generate random sentences
using the parsed chat as data input (Thanks to markovify library) and then post them to your Instagram account with a picture you choose. 

# HOW TO USE?

You will need to download Python 3 (obviously) and install markovify (https://pypi.org/project/markovify/) and instabot (https://pypi.org/project/instabot/#description) modules. After you have them installed, simply run Urabot.py and that's basically it! 

# ABOUT PARSING

Instagram, Facebook and WhatsApp (probably other apps too, but I don't really use them) allow you to export the chat with a specific person (or with all of them). You should
choose JSON option and then you either get a fileName.json (WhatsApp) or zip full of the personName folders with message_1.json files. To be able to parse the data using
Urabot, if your .json file is not named message_1, rename it and put it in the folder you run Urabot from. After that, just run Urabot and choose the 2nd option. It will 
ask you about the person's name, which you can find by opening .json file with notepad. When you open it you will see something like:

...
"participants": [
    {
      "name": "Name of the first person"
    },
    {
      "name": "Name of the second person"
    }
...

Just copy the name of person whose messages you want to use and paste it into Urabot and press enter. After that, Urabot will parse all messages from that person and store
them in a file named parsed.txt. If you want to add more messages, running Urabot with another file will not overwrite the file, so feel free to run it multiple times.

My suggestion is to read the parsed.txt file and delete all the "hahahahah" and similar useless messages. It will definitely help you to get a better output. Also, another
suggestion is to delete all the dots, commas, question marks, emojis etc. Maybe I should add all that stuff in the next version?

# ABOUT GENERATED CAPTIONS

So you have already parsed your data and you run the option "generate captions". What you get are eight randomly generated sentences based on the input (parsed.txt). To read
more about how it works and stuff: https://github.com/jsvine/markovify
The output is definitely not perfect so you will have to manually choose the captions you keep. Urabot will ask you which of the captions you want to KEEP and after you
answer it will ask you which of the captions you want to PUBLISH. KEEP = "The sentence is good or gramatically correct, I want to keep it and add it to my input". This way
your input file grows and positively affect your chances to randomly generate sentences that make sense. PUBLISH = "I like this sentence and I want it to be a caption of
some of my next IG posts". The sentence will be written to publishQueue.txt file.
IMPORTANT: if you want to keep or publish for example sentences number 0, 5 and 7, your answer in both cases should be 0,5,7
If your formatting is bad, Urabot will crash. So its number,number,number with no white spaces or whatever.

# ABOUT POSTING ON IG

Right now, Urabot takes the picture you want and reads the next caption from publishQueue.txt and posts it together on IG. In publishQueue.txt file you will see a number
written as the first line. That number is the number of the next caption in queue that will be posted. You can freely change the order of the sentences in the queue,
just dont delete any and be sure that the number in the first line is not bigger than the number of sentences in the file. 

# ABOUT CONFIG

The first option when you use Urabot allows you to enter your IG username and password (dont worry its only stored on your local machine). Username and password are REQUIRED
for Urabot to work, without them you cant post on IG. You can also enter the name of the picture, if you want to always post the same one. If you dont want to post the same
one all the time, enter x as the image name when and Urabot will ask you for the name of the picture every time you run the fourth option (posting on IG).

# OTHER

The image you want to post should be in the folder you run Urabot from. Only .jpg extension is tested, should work for .png too but I dont guarantee that. If your exported
chat is in your own local script (cyrillic or chinese letters for example), Urabot will probably be in trouble. To fix that you would have to play with encodings in
jsonParse.py file.

# CREDITS

jsvine - Markovify
bruvv - Instabot
