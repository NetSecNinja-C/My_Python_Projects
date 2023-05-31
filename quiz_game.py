print("Welcome To My Computer Quiz,")

playing = input("Do you want to Play ? ")

if playing.lower() == "no":
    quit("good bye")

if playing.lower() == "yes":
    print("ok, let's play , I wish Good Luck, You have 10 Quiz to face")
    score = 0

#1
answer = input("What country has the highest life expectancy? ")
if answer.lower() == "hong kong":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")

#2
answer = input("Where would you be if you were standing on the Spanish Steps? ")
if answer.lower() == "rome":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")

#3
answer = input("Which language has the more native speakers: English or Spanish? ")
if answer.lower() == "spanish":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")

#4
answer = input("What is the most common surname in the United States? ? ")
if answer.lower() == "smith":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")

#5
answer = input("What disease commonly spread on pirate ships? ")
if answer.lower() == "scurvy":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")

#6
answer = input("Who was the Ancient Greek God of the Sun? ")
if answer.lower() == "apollo":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")

#7
answer = input("How many minutes are in a full week? ")
if answer.lower() == "10080":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")

#8
answer = input("What company was originally called 'Cadabra'? ")
if answer.lower() == "amazon":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")

#9
answer = input("What character have both Robert Downey Jr. and Benedict Cumberbatch played? ")
if answer.lower() == "sherlock holmes":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")

#10
answer = input("What country drinks the most coffee per capita? ")
if answer.lower() == "finland":
    print("correct! ")
    score += 1
else:
    print("incorrect :(")


print("awsome you answerd 10 quiz check your incorrect awnsers this list")
print("You Got " + str(score) + " questions correct")
print(["hong kong", "rome", "spanish", "smith", "scurvy", "apollo", "10080", "amazon", "sherlock holmes", "finland" ])