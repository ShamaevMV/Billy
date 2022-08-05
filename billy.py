x = open("billy.txt", "r")
y = open("billy.sh", "w")

lines = x.readlines()
timeold = 0
for line in lines:
    if line[0].isdigit():
        timenew = int(line[0])*60 + int(line[2:4])
        y.write(f"sleep {timenew - timeold}\n")
        timeold = timenew
    if line[0].isalpha():
        line1 = line[0:-1]
        y.write(f"figlet \"{line1}\" \n")

x.close()
y.close()
