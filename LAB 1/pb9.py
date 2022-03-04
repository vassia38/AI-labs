import numpy

def createSumMatrix(matrix, n ,m) :
    sum = numpy.zeros((n,m))
    for i in range(n) :
        for j in range(m) :
            left = sum[i][j-1] if j-1 >= 0 else 0
            top = sum[i-1][j] if i-1 >= 0 else 0
            corner = sum[i-1][j-1] if j-1 >= 0 and i-1 >= 0 else 0
            sum[i][j] = matrix[i][j] + left + top - corner
    return sum

def pb8(matrix,n,m,pair) :
    x1,y1 = pair[0]
    x2,y2 = pair[1]
    sum = createSumMatrix(matrix,n,m)
    bLeft = y1-1 >= 0
    bTop = x1-1 >= 0
    left = sum[x2][y1-1] if bLeft == True else 0
    top = sum[x1-1][y2] if bTop == True else 0
    corner = sum[x1-1][y1-1] if bLeft == True and bTop == True else 0
    return sum[x2][y2] - left - top + corner

def errMsg(inputArr, expected, result) :
    return "Assert failed\n\tarr='"+str(inputArr)+"'\n\tExpected='"+str(expected) \
            +"'\n\tResult='"+str(result)+"'"

def test() :
    matrix1 = [[0, 2, 5, 4, 1],
        [4, 8, 2, 3, 7],
        [6, 3, 4, 6, 2],
        [7, 3, 1, 8, 3],
        [1, 5, 7, 9, 4]]
    n = 5
    m = 5
    pair1 = [[1,1],[3,3]]
    pair2 = [[2,2],[4,4]]
    res = pb8(matrix1, n, m, pair1)
    expected = 38
    assert res == expected, errMsg(matrix1, expected, res)
    res = pb8(matrix1, n, m, pair2)
    expected = 44
    assert res == expected, errMsg(matrix1, expected, res)
    print("all tests passed")


try :
    test()
except AssertionError as msg :
    print(msg)

