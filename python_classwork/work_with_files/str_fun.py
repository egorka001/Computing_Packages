file = open("from.txt")

#reverse str
a = file.readline()
print(a, end = "")
a = a[len(a) - 2::-1]
print(a)
print()

#find "substr"
a = file.readline()
print(a, end = "")
beg = a.find("\"") + 1
end = a.rfind("\"")
a = a[beg:end]
print(a)
print()

#double number
a = file.readline()
print(a, end = "")
a = int(a)
a += a
print(a)
print()

#login from email
a = file.readline()
print(a, end = "")
a = a[:a.find("@")]
print(a)
print()

#phone number
a = file.readline()
print(a, end = "")
b = "+"
for sym in a:
    if sym.isdigit():
        b += sym
print(b)
print()

#palyndorme
a = file.readline()
print(a, end = "")
a = a[:len(a) - 1].lower()
a.strip()
b = a[len(a) - 1::-1]
if a == b:
    print("Yes!\n")
else:
    print("No!\n")

#petya
print("Before:")
a = ""
for i in range(1, 124):
    a += str(i)
print(a)
print("After:")
a = a.replace('9', '')
print(a)
print()

#armstrong
print("Armstorng numbers:")
for i in range(100, 1000):
    if i == int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3:
        print(i)
print()

#automorfic
N = input("Automorphic numbers!\nInput N: ")
for i in range(1, int(N) + 1):
    if str(i) == str(i ** 2)[len(str(i**2)) - len(str(i)):]:
        print(i)
print()

#last
print("Last!")
count = 0;
for i in range(0, 14):
    for j in range(0, 14):
        for k in range(0, 14):
            if i * 15 + j * 17 + k * 21 == 185:
                count += 1
                print(f"{i} - 15kg, {j} - 17 kg, {k} - 21kg")
print(f"Amount of different variants: {count}")

file.close()
