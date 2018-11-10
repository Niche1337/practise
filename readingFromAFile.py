with open('listOfNames.txt', 'r') as open_file:
    all_text = open_file.read()

names = all_text.split()

d = {x:names.count(x) for x in names}
print(d)