def count(text):
    u = sum(1 for ch in text if ch.isupper())
    l = sum(1 for ch in text if ch.islower())
    return u, l

u, l = count("HeLLo")
print(u, l)