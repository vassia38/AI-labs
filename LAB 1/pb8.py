def pb8(n) :
    res = []
    for i in range(n+1):
        res.append(format(i,"b"))
    return res
            

def test() :
    n = 16
    res = pb8(n)
    assert len(res) - 1 == n, "test1 failed"
    
try :
    test()
    print("all tests passed")
except AssertionError as msg :
    print(msg)

