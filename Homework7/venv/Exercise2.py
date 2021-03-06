import re
file_object  = open("../Resources/error_log", "r")

for line in file_object:
    pattern = re.compile("\\[([A-Za-z ]+ [0-9]+ [0-9: ]+)\\] [\\[a-z\]]+ \\[[a-z]+ ([0-9.]+)\\] ([A-Za-z0-9():/_\\-. ]+)")

    if pattern.match(line):
        if line.strip():
            matchObj = re.match(pattern, line)
            print("On " + matchObj.group(1) + " a connection with ip address " + matchObj.group(2) + " issued the following error: " + matchObj.group(3))
            print()