import os
#create a file and write the following details:
f =  open("details.txt", "w")
f.write("orena\n")
f.write("tel aviv\n")
f.write("israel\n")
f.close()
# read file and print the content
f =  open("details.txt", "r")
print(os.path.abspath(f.name))
lines = f.read()
for line in lines:
    print(line.strip())
f.close()

with open("details.txt", "r") as f:
    lines = f.read()
    for line in lines:
        print(line.strip())
