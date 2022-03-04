from collections import Counter

def pb4(myStr):
      myStr = myStr.split()
      c = Counter(myStr)
      res = []
      for el in c.keys() :
            if c[el] == 1:
                  res.append(el)
      return res

def errMsg(inputStr, expected, result):
      return "Assert failed\n\tstr='"+inputStr+"'\n\tExpected='"+str(expected) \
             +"'\n\tResult='"+str(result)+"'"


def test() :
      str1 = "ana are ana are mere rosii ana"
      res = pb4(str1)
      expected = ['mere', 'rosii']
      assert res == expected, errMsg(str1,expected,res)
      print("all tests passed")

try:
      test()
except AssertionError as msg:
      print(msg)
