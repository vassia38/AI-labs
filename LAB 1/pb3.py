def pb3(v1,v2):
      sum = 0
      for i, j in zip(v1, v2):
            sum += i*j
      return sum

def errMsg(v1, v2, expected, result):
      return "Assert failed\n\tv1='"+str(v1)+"', v2='"+str(v2)+"'\n\tExpected='"+str(expected) \
             +"'\n\tResult='"+str(result)+"'"


def test() :
      v1 = [1,0,2,0,3]
      v2 = [1,2,0,3,1]
      res = pb3(v1,v2)
      expected = 4
      assert res == expected, errMsg(v1,v2,expected,res)
      print("all tests passed")

try:
      test()
except AssertionError as msg:
      print(msg)

