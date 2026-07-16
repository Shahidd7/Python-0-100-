import random
sec_num = random.randint(1,100)
attempt = 0
while True:
    s = int(input("enter any number from 0-100:"))
    if(s > 100 or s < 1):
        print("Please select numbers from 1 - 100")
        continue
    attempt = attempt + 1
    if (s > sec_num):
        print(f"Your number {s} is too high")
    elif (sec_num > s):
        print(f"your number {s} too low")
    else :
        print(f"you got it Right, the number {s} and guessed number {sec_num} are same!!!")
        print(f"you got the number in {attempt} attempts")
        try:
            with open("highscore.txt","r") as file:
                best_score = int(file.read())
        except(FileNotFoundError):
            best_score = 999
        if attempt < best_score:
            print("New High-Score")
            with open("highscore.txt","w") as file:
                file.write(str(attempt))
        else:
            print(f"The best score was {best_score}.Try Again")


    