import unittest

def pb1(myStr):
      myStr = myStr.split()
      max = myStr[0]
      for word in myStr :
            if word > max :
                  max = word
      return max

def errMsg(inputStr,ExpStr,ResStr):
      return "Assert failed\n\tstr='"+inputStr+"'\n\tExpected='"+ExpStr \
             +"'\n\tResult='"+ResStr+"'"

def test() :
      str1 = "Ana are mere rosii si galbene"
      res = pb1(str1)
      expected = "si1"
      assert res == expected, errMsg(str1,expected,res)
      print("all tests passed")

try:
      test()
except AssertionError as msg :
      print(msg)

