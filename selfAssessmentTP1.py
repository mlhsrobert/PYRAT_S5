from AIs.TP1 import *

maze = {(0, 0): {(0, 1): 1, (1, 0): 1}, 
        (0, 1): {(0, 2): 1, (0, 0): 1, (1, 1): 1}, 
        (0, 2): {(0, 1): 1}, 
        (0, 3): {(1, 3): 4}, 
        (0, 4): {(0, 5): 5}, 
        (0, 5): {(0, 6): 1, (0, 4): 5, (1, 5): 1}, 
        (0, 6): {(0, 7): 1, (0, 5): 1}, 
        (0, 7): {(0, 6): 1}, 
        (0, 8): {(0, 9): 1, (1, 8): 1}, 
        (0, 9): {(0, 10): 1, (0, 8): 1}, 
        (0, 10): {(0, 9): 1, (1, 10): 1}, 
        (1, 0): {(1, 1): 2, (0, 0): 1}, 
        (1, 1): {(1, 0): 2, (0, 1): 1, (2, 1): 1}, 
        (1, 2): {(1, 3): 1, (2, 2): 1}, 
        (1, 3): {(1, 4): 1, (1, 2): 1, (0, 3): 4}, 
        (1, 4): {(1, 5): 8, (1, 3): 1}, 
        (1, 5): {(1, 6): 1, (1, 4): 8, (0, 5): 1}, 
        (1, 6): {(1, 7): 1, (1, 5): 1, (2, 6): 1}, 
        (1, 7): {(1, 6): 1}, 
        (1, 8): {(0, 8): 1}, 
        (1, 9): {(1, 10): 1}, 
        (1, 10): {(1, 9): 1, (0, 10): 1, (2, 10): 1}, 
        (2, 0): {(2, 1): 1, (3, 0): 1}, 
        (2, 1): {(2, 0): 1, (1, 1): 1}, 
        (2, 2): {(2, 3): 1, (1, 2): 1, (3, 2): 2}, 
        (2, 3): {(2, 4): 1, (2, 2): 1, (3, 3): 1}, 
        (2, 4): {(2, 5): 1, (2, 3): 1}, 
        (2, 5): {(2, 4): 1}, 
        (2, 6): {(2, 7): 1, (1, 6): 1}, 
        (2, 7): {(2, 6): 1}, 
        (2, 8): {(2, 9): 1}, 
        (2, 9): {(2, 8): 1, (3, 9): 1}, 
        (2, 10): {(1, 10): 1, (3, 10): 1}, 
        (3, 0): {(2, 0): 1, (4, 0): 1}, 
        (3, 1): {(4, 1): 2}, 
        (3, 2): {(2, 2): 2, (4, 2): 1}, 
        (3, 3): {(3, 4): 1, (2, 3): 1}, 
        (3, 4): {(3, 5): 1, (3, 3): 1, (4, 4): 1}, 
        (3, 5): {(3, 6): 1, (3, 4): 1}, 
        (3, 6): {(3, 5): 1}, 
        (3, 7): {(3, 8): 1, (4, 7): 1}, 
        (3, 8): {(3, 7): 1}, 
        (3, 9): {(2, 9): 1, (4, 9): 4}, 
        (3, 10): {(2, 10): 1, (4, 10): 9}, 
        (4, 0): {(3, 0): 1, (5, 0): 1}, 
        (4, 1): {(4, 2): 1, (3, 1): 2, (5, 1): 1}, 
        (4, 2): {(4, 1): 1, (3, 2): 1}, 
        (4, 3): {(4, 4): 1}, 
        (4, 4): {(4, 3): 1, (3, 4): 1, (5, 4): 6}, 
        (4, 5): {(4, 6): 1, (5, 5): 1}, 
        (4, 6): {(4, 5): 1, (5, 6): 1}, 
        (4, 7): {(3, 7): 1, (5, 7): 1}, 
        (4, 8): {(4, 9): 1}, 
        (4, 9): {(4, 10): 1, (4, 8): 1, (3, 9): 4}, 
        (4, 10): {(4, 9): 1, (3, 10): 9, (5, 10): 1}, 
        (5, 0): {(5, 1): 6, (4, 0): 1, (6, 0): 1}, 
        (5, 1): {(5, 2): 1, (5, 0): 6, (4, 1): 1}, 
        (5, 2): {(5, 1): 1}, 
        (5, 3): {(5, 4): 1, (6, 3): 1}, 
        (5, 4): {(5, 5): 1, (5, 3): 1, (4, 4): 6, (6, 4): 1}, 
        (5, 5): {(5, 6): 1, (5, 4): 1, (4, 5): 1, (6, 5): 1}, 
        (5, 6): {(5, 7): 1, (5, 5): 1, (4, 6): 1, (6, 6): 6}, 
        (5, 7): {(5, 6): 1, (4, 7): 1}, 
        (5, 8): {(5, 9): 1}, 
        (5, 9): {(5, 10): 6, (5, 8): 1, (6, 9): 1}, 
        (5, 10): {(5, 9): 6, (4, 10): 1, (6, 10): 1}, 
        (6, 0): {(6, 1): 1, (5, 0): 1, (7, 0): 9}, 
        (6, 1): {(6, 2): 1, (6, 0): 1, (7, 1): 4}, 
        (6, 2): {(6, 1): 1}, 
        (6, 3): {(5, 3): 1, (7, 3): 1}, 
        (6, 4): {(6, 5): 1, (5, 4): 1}, 
        (6, 5): {(6, 4): 1, (5, 5): 1}, 
        (6, 6): {(6, 7): 1, (5, 6): 6, (7, 6): 1}, 
        (6, 7): {(6, 6): 1}, 
        (6, 8): {(6, 9): 1, (7, 8): 1}, 
        (6, 9): {(6, 8): 1, (5, 9): 1, (7, 9): 2}, 
        (6, 10): {(5, 10): 1, (7, 10): 1}, 
        (7, 0): {(6, 0): 9, (8, 0): 1}, 
        (7, 1): {(6, 1): 4, (8, 1): 1}, 
        (7, 2): {(7, 3): 1}, 
        (7, 3): {(7, 2): 1, (6, 3): 1}, 
        (7, 4): {(7, 5): 1}, 
        (7, 5): {(7, 6): 1, (7, 4): 1}, 
        (7, 6): {(7, 7): 1, (7, 5): 1, (6, 6): 1}, 
        (7, 7): {(7, 6): 1, (8, 7): 1}, 
        (7, 8): {(6, 8): 1, (8, 8): 2}, 
        (7, 9): {(6, 9): 2},
        (7, 10): {(6, 10): 1, (8, 10): 1}, 
        (8, 0): {(7, 0): 1, (9, 0): 1}, 
        (8, 1): {(8, 2): 1, (7, 1): 1}, 
        (8, 2): {(8, 1): 1}, 
        (8, 3): {(8, 4): 1}, 
        (8, 4): {(8, 3): 1, (9, 4): 1}, 
        (8, 5): {(8, 6): 1}, 
        (8, 6): {(8, 7): 1, (8, 5): 1}, 
        (8, 7): {(8, 8): 1, (8, 6): 1, (7, 7): 1}, 
        (8, 8): {(8, 7): 1, (7, 8): 2, (9, 8): 1}, 
        (8, 9): {(8, 10): 1, (9, 9): 1}, 
        (8, 10): {(8, 9): 1, (7, 10): 1}, 
        (9, 0): {(9, 1): 1, (8, 0): 1, (10, 0): 1}, 
        (9, 1): {(9, 0): 1}, 
        (9, 2): {(10, 2): 1}, 
        (9, 3): {(9, 4): 1}, 
        (9, 4): {(9, 5): 1, (9, 3): 1, (8, 4): 1}, 
        (9, 5): {(9, 6): 8, (9, 4): 1, (10, 5): 1}, 
        (9, 6): {(9, 7): 1, (9, 5): 8}, 
        (9, 7): {(9, 8): 1, (9, 6): 1, (10, 7): 4}, 
        (9, 8): {(9, 7): 1, (8, 8): 1}, 
        (9, 9): {(9, 10): 2, (8, 9): 1, (10, 9): 1}, 
        (9, 10): {(9, 9): 2, (10, 10): 1}, 
        (10, 0): {(10, 1): 1, (9, 0): 1}, 
        (10, 1): {(10, 2): 1, (10, 0): 1}, 
        (10, 2): {(10, 1): 1, (9, 2): 1}, 
        (10, 3): {(10, 4): 1}, 
        (10, 4): {(10, 5): 1, (10, 3): 1}, 
        (10, 5): {(10, 6): 5, (10, 4): 1, (9, 5): 1}, 
        (10, 6): {(10, 5): 5}, 
        (10, 7): {(9, 7): 4}, 
        (10, 8): {(10, 9): 1}, 
        (10, 9): {(10, 10): 1, (10, 8): 1, (9, 9): 1}, 
        (10, 10): {(10, 9): 1, (9, 10): 1}}

def aboveOf_unitTest(loc, goodLocation):
    try:
        location = aboveOf(loc)
        if type(location) != tuple:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The result has to be a tuple. Your result is of the type "+str(type(location))+".\n"
            print(ans)
            return False
            
        if type(location[0]) != int or type(location[1]) != int:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The result has to be a tuple of int. Your result is a tuple of the type ("+str(type(location[0]))+","+str(type(location[1]))+".\n"
            print(ans) 
            return False 
        
        if location!=goodLocation:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The cell above (i,j) is (i,j+1).\n"
            print(ans) 
            return False 
        return True
    except:
        ans = "    Error -- Your function did not work. \n"
        ans += "    location : "+str(loc)+" \n"
        print(ans)
        return False    

def functionAboveOfTest():
    print("TEST of the function 'aboveOf'")
    result = True
    result = result and aboveOf_unitTest((0,0),(0,1))
    result = result and aboveOf_unitTest((12,-7),(12,-6))       

    return result

def belowOf_unitTest(loc, goodLocation):
    try:
        location = belowOf(loc)
        if type(location) != tuple:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The result has to be a tuple. Your result is of the type "+str(type(location))+".\n"
            print(ans)
            return False
            
        if type(location[0]) != int or type(location[1]) != int:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The result has to be a tuple of int. Your result is a tuple of the type ("+str(type(location[0]))+","+str(type(location[1]))+".\n"
            print(ans) 
            return False 
        
        if location!=goodLocation:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The cell below (i,j) is (i,j-1).\n"
            print(ans) 
            return False 
        return True
    except:
        ans = "    Error -- Your function did not work. \n"
        ans += "    location : "+str(loc)+" \n"
        print(ans)
        return False
    
def functionBelowOfTest():
    print("TEST of the function 'belowOf'")
    result = True
    
    result = result and belowOf_unitTest((0,0),(0,-1))
    result = result and belowOf_unitTest((12,-7),(12,-8))   
    
    return result

def leftOf_unitTest(loc, goodLocation):
    try:
        location = leftOf(loc)
        if type(location) != tuple:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The result has to be a tuple. Your result is of the type "+str(type(location))+".\n"
            print(ans)
            return False
            
        if type(location[0]) != int or type(location[1]) != int:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The result has to be a tuple of int. Your result is a tuple of the type ("+str(type(location[0]))+","+str(type(location[1]))+".\n"
            print(ans) 
            return False 
        
        if location!=goodLocation:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The cell on the left of (i,j) is (i-1,j).\n"
            print(ans) 
            return False 
        return True
    except:
        ans = "    Error -- Your function did not work. \n"
        ans += "    location : "+str(loc)+" \n"
        print(ans)
        return False

def functionLeftOfTest():
    print("TEST of the function 'leftOf'")
    result = True
    
    result = result and leftOf_unitTest((0,0),(-1,0))
    result = result and leftOf_unitTest((-12,7),(-13,7)) 
    
    return result

def rightOf_unitTest(loc, goodLocation):
    try:
        location = rightOf(loc)
        if type(location) != tuple:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The result has to be a tuple. Your result is of the type "+str(type(location))+".\n"
            print(ans)
            return False
            
        if type(location[0]) != int or type(location[1]) != int:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The result has to be a tuple of int. Your result is a tuple of the type ("+str(type(location[0]))+","+str(type(location[1]))+".\n"
            print(ans) 
            return False 
        
        if location!=goodLocation:
            ans = "    Error -- The expected answer is "+str(goodLocation)+". Your answer is : "+str(location)+".\n"
            ans += "    location : "+str(loc)+" \n"
            ans += "    The cell on the right of (i,j) is (i+1,j).\n"
            print(ans) 
            return False 
        return True
    except:
        ans = "    Error -- Your function did not work. \n"
        ans += "    location : "+str(loc)+" \n"
        print(ans)
        return False

def functionRightOfTest():
    print("TEST of the function 'rightOf'")
    result = True
    
    result = result and rightOf_unitTest((0,0),(1,0))
    result = result and rightOf_unitTest((-12,7),(-11,7))    
    
    return result


def canMove_unitTest(maze, start, end, goodAns):
    try:
        result = canMove(maze,start,end)
        if type(result) != bool:
            ans = "    Error -- The expected answer is "+str(goodAns)+". Your answer is : "+str(result)+".\n"
            ans += "    mazeMap : "+str(maze)+"\n"
            ans += "    fromLocation : "+str(start)+" \n"
            ans += "    toLocation : "+str(end)+" \n"            
            ans += "    The result has to be a boolean. Your result is of the type "+str(type(result))+".\n"
            print(ans)
            return False 
        
        if result != goodAns:
            ans = "    Error -- The expected answer is "+str(goodAns)+". Your answer is : "+str(result)+".\n"
            ans += "    mazeMap : "+str(maze)+"\n"
            ans += "    You can pass from location "+str(start)+" to location "+str(end)+".\n"
            print(ans)
            return False
        return True
    except:
        ans = "    Error -- Your function did not work. \n"
        ans += "    mazeMap : "+str(maze)+"\n"
        ans += "    fromLocation : "+str(start)+" \n"
        ans += "    toLocation : "+str(end)+" \n" 
        print(ans)
        return False    

def functionCanMoveTest():
    print("TEST of the function 'canMove'")
    result = True
    
    result = result and canMove_unitTest(maze,(0,0),(0,1),True)
    result = result and canMove_unitTest(maze,(0,1),(0,0),True)       
    result = result and canMove_unitTest(maze,(0,0),(-1,0),False)      
    result = result and canMove_unitTest(maze,(-1,0),(0,0),False) 
    result = result and canMove_unitTest(maze,(1,4),(2,4),False) 
    result = result and canMove_unitTest(maze,(2,4),(1,4),False) 
    result = result and canMove_unitTest(maze,(0,5),(0,4),True) 
    result = result and canMove_unitTest(maze,(10,10),(11,10),False)
    result = result and canMove_unitTest(maze,(10,11),(10,10),False)
    result = result and canMove_unitTest(maze,(15,15),(15,16),False)
    result = result and canMove_unitTest(maze,(0,0),(1,1),False)  
    
    return result


def getMove_unitTest(maze,start,end,goodAns):
    try:
        result = getMove(maze,start,end)
        if type(result) != str:
            ans = "    Error -- The expected answer is '"+str(goodAns)+"'. Your answer is : "+str(result)+".\n"
            ans += "    mazeMap : "+str(maze)+" \n"
            ans += "    fromLocation : "+str(start)+" \n"
            ans += "    toLocation : "+str(end)+" \n"            
            ans += "    The result has to be a string. Your result is of the type "+str(type(result))+".\n"
            print(ans)
            return False
        
        if not (result == 'D' or result == 'U' or result == 'L' or result == 'R' or result == 'None'):
            ans = "    Error -- The expected answer is '"+str(goodAns)+"'. Your answer is : "+str(result)+".\n"
            ans += "    mazeMap : "+str(maze)+"\n"
            ans += "    fromLocation : "+str(start)+" \n"
            ans += "    toLocation : "+str(end)+" \n"            
            ans += "    The result has to be a string from this list : 'D' / 'U' / 'L' / 'R' / 'None'.\n"
            print(ans)
            return False        
        
        if result != goodAns:
            ans = "    Error -- The expected answer is '"+str(goodAns)+"'. Your answer is : "+str(result)+".\n"
            ans += "    mazeMap : "+str(maze)+"\n"
            ans += "    You can pass from location "+str(start)+" to location "+str(end)+".\n"
            print(ans)
            return False
        return True
    except:
        ans = "    Error -- Your function did not work. \n"
        ans += "    mazeMap : "+str(maze)+"\n"
        ans += "    fromLocation : "+str(start)+" \n"
        ans += "    toLocation : "+str(end)+" \n"
        print(ans)
        return False     

def functionGetMoveTest():
    print("TEST of the function 'getMove'")
    result = True
    
    result = result and getMove_unitTest(maze,(0,0),(0,1),"U")
    result = result and getMove_unitTest(maze,(0,1),(0,0),"D") 
    result = result and getMove_unitTest(maze,(0,0),(-1,0),"None")
    result = result and getMove_unitTest(maze,(0,0),(1,0),"R")
    result = result and getMove_unitTest(maze,(1,5),(0,5),"L")  
    
    return result
       
def giveResult(result):
    if result:
        print("----COMPLETE \n")
    else:
        print("----ERROR \n")

def main():
    testSuccess = 0
    result = functionAboveOfTest()
    giveResult(result)
    testSuccess += result
    
    result = functionBelowOfTest()
    giveResult(result)
    testSuccess += result
    
    result = functionLeftOfTest()
    giveResult(result)
    testSuccess += result
    
    result = functionRightOfTest()
    giveResult(result)
    testSuccess += result
    
    result = functionCanMoveTest()
    giveResult(result)
    testSuccess += result
    
    result = functionGetMoveTest()
    giveResult(result)
    testSuccess += result    
    
    if testSuccess==6:
        print("----------TOTAL NUMBER OF TESTS : 6")
        print("----------COMPLETE SUCCESS")
    else:
        print("----------TOTAL NUMBER OF TESTS : 6")
        print("----------ERRORS : "+str(6-testSuccess))
        print("----------SUCCESS : "+str(testSuccess))
     
    
    
if __name__ == "__main__":
    main()
