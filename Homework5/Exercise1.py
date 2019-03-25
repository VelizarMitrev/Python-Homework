import re

print("Enter your full name")
full_name = input()

matchObj = re.match("([A-Z])[a-z]+ ?([A-Z])[a-z]+ ?([A-Z][a-z]+)", full_name) # The names of the person should start with a capital letter otherwise the regex won't work!

print(matchObj.group(1) + "." + matchObj.group(2) + "." + matchObj.group(3))
