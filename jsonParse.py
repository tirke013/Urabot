import json

def parse(name, path):
    with open(path+"\message_1.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    pisanje = open(path+"\parsed.txt", "a+", encoding="utf-8")

    newdict = data["messages"]

    '''probaj dekodiranje i jednog i drugog pa vidi jel mozes da dobijes jedno od drugog'''
    for line in newdict:
        if line["sender_name"].encode("latin-1").decode("unicode-escape") == name.encode("utf-8").decode("unicode-escape") and line["type"] == "Generic" and "content" in line:
            if line["content"] != "Liked a message":
                print(line["content"])
                pisanje.write(line["content"]+"\n")
    pisanje.close()
    readLower = open(path+"\parsed.txt", "r", encoding="utf-8")
    text = readLower.read()
    writeLower = open(path+"\parsed.txt", "w", encoding="utf-8")
    for line in text:
        sentence = line.lower()
        writeLower.write(sentence)
