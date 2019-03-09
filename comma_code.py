names = ["varun", "shivam", "rishabh", "aman"]

result = ""
for i in range(0, len(names)):
    if i == len(names) - 1:
        result = result + "and " + str(names[i])
    else:
        result = result + str(names[i]) + ", "

print(result)
