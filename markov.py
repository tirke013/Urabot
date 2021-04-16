import markovify

def doTheMarkov(path, state):
    readParsed = open(path+"\parsed.txt", "r", encoding="utf-8")
    appendParsed = open(path+"\parsed.txt", "a", encoding="utf-8")
    text = readParsed.read()
    generatedString = list()

    text_model = markovify.NewlineText(text, state_size = state)

    for i in range(5):
        stri = text_model.make_sentence()
        generatedString.append(stri)
        print(str(i) + ".", end=" ")
        print(stri)

    for i in range(3):
        stri = text_model.make_short_sentence(280)
        generatedString.append(stri)
        print(str(i + 5) + ".", end=" ")
        print(stri)

    inp = input("\nIndexes to keep:\n")
    if inp!="x":
        splitInput = inp.split(",")
        for ind in splitInput:
            appendParsed.write("\n"+generatedString[int(ind)] + "\n")

    queueReader = open(path+"\publishQueue.txt", "r", encoding="utf-8")
    queueText = queueReader.readlines()
    queueWriter = open(path+"\publishQueue.txt", "w", encoding="utf-8")
    if len(queueText)==0:
        queueText.append("0")

    inp = input("\nIndexes to publish\n")
    if inp!="x":
        splitInput = inp.split(",")
        for ind in splitInput:
            queueText.append("\n"+generatedString[int(ind)])
        if queueText[0]=="0":
            queueText[0] = "1"

    queueWriter.writelines(queueText)
