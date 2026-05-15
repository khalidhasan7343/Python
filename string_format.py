# user_input = input("What is your name?")
# a = "Good Morning, {}. How are you? {}".format(user_input , "Have a nice day!")
# print(a)

age = 25
f_name = "John"
l_name = "Doe"

txt = "This is {f_name} {l_name}. He is {age} years old.".format(
    f_name=f_name, l_name=l_name, age=age
)

txt2 = f"This is {f_name} {l_name}. He is {age} years old."
print(txt)
print(txt2)
