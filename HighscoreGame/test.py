

file = lambda x: open("storage.bin",f"{x}b")
print(file("r"))

file = (lambda: open("storage.txt","a"))()
print(file.write("HELLO"))


k = lambda x: print(f"{x}clown")

k("kappa")