import heapq
 
class MaxHeap:
 
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)
 
    def top(self):
        return -self.data[0]
 
    def push(self, item):
        heapq.heappush(self.data, -item)
 
    def pop(self):
        return -heapq.heappop(self.data)
 
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)

def pb7(arr, k) :
      n = len(arr)
      mh = MaxHeap(arr)
      while k > 1:
            mh.pop()
            k -= 1
      return mh.top()
            

def errMsg(inputArr, expected, result) :
      return "Assert failed\n\tarr='"+str(inputArr)+"'\n\tExpected='"+str(expected) \
             +"'\n\tResult='"+str(result)+"'"


def test() :
      arr1 = [7,4,6,3,9,1]
      k = 2
      res = pb7(arr1, k)
      expected = 7
      assert res == expected, errMsg(arr1,expected,res)
      print("all tests passed")

try :
      test()
except AssertionError as msg :
      print(msg)

