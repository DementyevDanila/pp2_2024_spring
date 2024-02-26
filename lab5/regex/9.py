import re
def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, r"\1 \2", testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
pattern = r'(\w)([A-Z])'
x = re.findall(pattern, "MySuperTest")
print(x)
test(pattern, "MySuperTest", "test1", "My Super Test")
test(pattern, " MySuperTest IAmRobot", "test2", " My Super Test I Am Robot")