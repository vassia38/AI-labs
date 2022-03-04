def pb2(x1,y1,x2,y2):
      sqDist = (x2-x1)**2 + (y2-y1)**2
      return sqDist**(1/2)

def errMsg(p1,p2,expected,result):
      return "Assert failed\n\tp1='"+str(p1)+"', p2='"+str(p2)+"'\n\tExpected='"+str(expected) \
             +"'\n\tResult='"+str(result)+"'"

def test() :
      x1,y1 = [1,5]
      x2,y2 = [4,1]
      res = pb2(x1,y1,x2,y2)
      expected = 5.0
      assert res == expected, errMsg([x1,y1],[x2,y2],expected,res)
      print("all tests passed")

try:
      test()
except AssertionError as msg :
      print(msg)
