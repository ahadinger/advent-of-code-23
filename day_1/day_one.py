file = open('input.txt', 'r')
lines = file.readlines()

total = 0

for line in lines:
    charList = list(line)
    print(charList)
    temp_list = [""]*2
    counter = 0
    for c in charList:
        if(c.isnumeric() == True and counter == 0):
            temp_list[counter] = c
            temp_list[counter+1] = c
            counter = 1
        elif(c.isnumeric() == True):
            temp_list[counter] = c

    print(temp_list)
    inner_total = int(temp_list[0]+ temp_list[1])
    total += int(inner_total)

print(total)