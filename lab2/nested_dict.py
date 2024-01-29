# Вложенные словари

myfamily = {
  "Me" : {
    "name" : "Danila",
    "year" : 2006,
    "member" : "First Child"
  },
  "Mom" : {
    "name" : "Marina",
    "year" : "Always young",
    "member" : "Mother"
  },
  "Dad" : {
    "name" : "Alexey",
    "year" : "Always powerful",
    "member" : "Father"
  }
}
print(myfamily)
print(' ')
# or it possble to create 3 dif dict and combain it to 1

Me = {
    "name" : "Danila",
    "year" : 2006,
    "member" : "First Child"
}
Mom = {
    "name" : "Marina",
    "year" : "Always young",
    "member" : "Mother"
}
Dad = {
    "name" : "Alexey",
    "year" : "Always powerful",
    "member" : "Father"
}

myfamily2 = {
    "Son" : Me,
    "Mother" : Mom,
    "Father" : Dad
}
print(myfamily2)
print(myfamily["Me"]["name"])