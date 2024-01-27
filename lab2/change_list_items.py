colors = ["red", "orange", "blue", "yellow", "purple", "green", "magenta"]
colors[3] = "black"
print(colors)
colors[1:3] = ["gray", "white"]
print(colors)
colors[0:1] = ["pink", "brown"] # except that there is now enough space to replace 2 elements, they will bw inserted to list, size will increase
print(colors)
colors[5:] = ["cyan"] # if there are a lot of space to replace element, n elements will change, other will delete
print(colors)
colors.insert(3, "gold") # without replacing, just add new element to position
print(colors)