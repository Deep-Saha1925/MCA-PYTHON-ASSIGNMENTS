# file = open("learn.txt", "r")
# print(file)
# file.write("\nI love sports.")
# print(file.read())

# txt = file.readline()
# print(txt)
# file.close()

with open("learn.txt", "r") as f:
    for t in f:
        
        print(t)