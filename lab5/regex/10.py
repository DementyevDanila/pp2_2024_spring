import re
def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, r"\1_\2", testData)
    result = re.sub("\s", "_", result)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
pattern = r'(\w)([A-Z])'
s1 = "MySuperTest"
s2 = "MySuperTest IAmRobot"


test(pattern, s1, "test1", "My_Super_Test")
test(pattern, s2, "test2", "My_Super_Test_I_Am_Robot")