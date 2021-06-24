# Sem 1
# raw = open("raw_sem1.txt")
# for line in raw:
#     prep = line.split("|")
#     print(prep[0].center(8,' '),prep[1].center(30,' '),prep[4].center(3,' '),prep[11])

# Sem 2
# raw = open("raw_sem2.txt")
# for line in raw:
    # prep = line.split("|")
    # print(prep[0].center(8,' '),prep[1].center(30,' '),prep[4].center(3,' '),prep[13])

# Sem 3
# raw = open("raw_sem3.txt")
# for line in raw:
#     prep = line.split("|")
#     print(prep[0].center(8,' '),prep[1].center(42,' '),prep[4].center(3,' '),prep[13])

# Sem 4
# raw = open("raw_sem4.txt")
# prev = []
# for line in raw:
    # prep = line.split("|")
    # if prep[0] == "":
        # prep[0] = prev[-1]
    # else:
        # prev.append(prep[0])
    
    # #if prep[0].startswith("704722"):
        # #if(prep[4] == " PR "):
    # print(prep[0].center(8,' '),prep[1].center(42,' '),prep[4].center(3,' '),prep[13])

# Sem 5
# raw = open("raw_sem5.txt")
# prev = []
# for line in raw:
#     prep = line.split("|")
#     if prep[0] == "":
#         prep[0] = prev[-1]
#     else:
#         prev.append(prep[0])
#     if prep[0].startswith("70473"):
#         if (prep[4] == " PR "):
#             print(prep[0].center(8,' '),prep[1].center(75,' '),prep[4].center(3,' '),prep[13])

raw = open("raw_sem6.txt")
prev = []
for line in raw:
    prep = line.split("|")
    if prep[0] == "":
        prep[0] = prev[-1]
    else:
        prev.append(prep[0])
    if prep[0].startswith("704732") and prep[4] == " PR ":
        print(prep[0].center(8,' '),prep[1].center(75,' '),prep[4].center(3,' '),prep[13])