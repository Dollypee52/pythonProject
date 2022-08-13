print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
lower_case_name = combined_name.lower()

T = lower_case_name.count("t")
R = lower_case_name.count("r")
U = lower_case_name.count("u")
E = lower_case_name.count("e")

true = T + R + U + E

L = lower_case_name.count("l")
O = lower_case_name.count("o")
V = lower_case_name.count("v")
E = lower_case_name.count("e")

love = L + O + V + E

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
