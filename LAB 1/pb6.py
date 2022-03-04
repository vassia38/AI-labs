def pb6(arr):
      count = 1
      majIndex = 0
      for i in range(1,len(arr)) :
            #print(str(arr[majIndex]) + ", "+ str(count))
            if arr[majIndex] == arr[i] :
                  count += 1
            else :
                  count -= 1
            if count == 0 :
                  majIndex = i
                  count = 1
      count = 0
      for el in arr :
            if arr[majIndex] == el :
                  count += 1
      if count > len(arr)/2 :
            return majIndex
      return -1

def errMsg(inputArr, expected, result):
      return "Assert failed\n\tarr='"+str(inputArr)+"'\n\tExpected='"+str(expected) \
             +"'\n\tResult='"+str(result)+"'"


def test() :
      arr1 = [1,8,2,2,2,5,2,3,1,2,2]
      res = arr1[pb6(arr1)]
      expected = 2
      assert res == expected, errMsg(arr1,expected,res)
      print("all tests passed")

try:
      test()
except AssertionError as msg:
      print(msg)
