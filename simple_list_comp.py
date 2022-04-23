temps = [221,222,223,224,-999]

new_temps = [temp / 10 for temp in temps]

print(new_temps)

# This equals to this
new_temp = []

for temp1 in temps:
    new_temp.append(temp1/10)

print(new_temp)

# [22.1, 22.2, 22.3, 22.4]
# [22.1, 22.2, 22.3, 22.4]

new_temps2 = [temp / 10 for temp in temps if temp > 1]
print(new_temps2)


new_temps3 = [temp / 10  if temp > 1 else "neg" for temp in temps] # If you use if else, for loop go to the end

print(new_temps3)