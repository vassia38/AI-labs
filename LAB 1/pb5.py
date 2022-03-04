def pb5(arr):
      n = len(arr)
      gaussSum = n*(n-1)/2
      sum = 0
      for i in arr:
            sum += i
      return sum - gaussSum
      

def errMsg(inputArr, expected, result):
      return "Assert failed\n\tarr='"+str(inputArr)+"'\n\tExpected='"+str(expected) \
             +"'\n\tResult='"+str(result)+"'"


def test() :
      arr1 = [1,2,3,4,2]
      res = pb5(arr1)
      expected = 2
      assert res == expected, errMsg(arr1,expected,res)
      print("all tests passed")

try:
      test()
except AssertionError as msg:
      print(msg)
