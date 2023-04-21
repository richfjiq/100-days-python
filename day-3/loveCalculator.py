# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2
lower_str = combined_string.lower()

t_char = lower_str.count("t")
r_char = lower_str.count("r")
u_char = lower_str.count("u")
e_char = lower_str.count("e")

a = t_char + r_char + u_char + e_char

l_char = lower_str.count("l")
o_char = lower_str.count("o")
v_char = lower_str.count("v")
e_char = lower_str.count("e")

b = l_char + o_char + v_char + e_char

total = int(f"{a}{b}")

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
