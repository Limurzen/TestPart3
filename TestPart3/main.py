
d = {
    "привет" : "hello",
    "пока" : "bye",
    "урок" : "lesson"
}
print(d.keys())
for i in d:
    a = input(f"Как будет '{i}' на англиском?\n ")
    if a.lower() == d.get(i):
        print("Молодец, давай дальше")
    else:
        print(f"Это слово переводится как '{d.get(i)}'")

