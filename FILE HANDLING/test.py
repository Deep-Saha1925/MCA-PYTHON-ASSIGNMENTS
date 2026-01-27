file = open("learn.txt", "r")
# print(file)
# file.write("\nI love sports.")
# print(file.read())

txt = file.readline()
print(txt)
file.close()