import os
import sys

def testEgaliteFile(fichierATester, fichierDeReference):
    success = True
    f = open(fichierATester) 
    g = open(fichierDeReference)  
    
    ch1 = f.read() 
    ch2 = g.read()   
    line =0
    for x in range(min(len(ch1),len(ch2))): 
        if ch1[x] == "\n":
            line+=1
        if ch1[x]!=ch2[x]: 
            print("Erreur a la ligne "+str(line+1)) 
            success = False
            return
    
    f.close() 
    g.close() 
    return success

def giveResult(test):
    if test:
        print("----SUCCES")
    else:
        print("----FAILURE")

def runTest1():
    print("TEST 1 : Both won --rat AIs\Test_Rat1.py --python AIs\Test_Python1.py --maze_file maze_files\Maze1.maze --auto_exit --test_file")
    #sys.argv=["nonRegressionScript.py","--rat","AIs\RatTest.py","--python","AIs\PythonTest.py","--maze_file", "maze_files\mazeTest.maze","--auto_exit"]
    #exec(open("nonRegressionScript.py").read())     
    giveResult(testEgaliteFile("testFiles/minutesFiles/NewMinutesFile","testFiles/minutesFiles/Test1"))

def runTest2():    
    print("TEST 2 : AI_rat won against AI_python --rat AIs\Test_Rat2.py --python AIs\Test_Python2.py --maze_file maze_files\Maze1.maze --auto_exit --test_file")
    giveResult(testEgaliteFile("testFiles/minutesFiles/NewMinutesFile","testFiles/minutesFiles/Test2"))
    
def runTest3():    
    print("TEST 3 : AI_python won against AI_rat --rat AIs\Test_Rat3.py --python AIs\Test_Python3.py --maze_file maze_files\Maze1.maze --auto_exit --test_file")
    giveResult(testEgaliteFile("testFiles/minutesFiles/NewMinutesFile","testFiles/minutesFiles/Test3"))
    
def runTest4():    
    print("TEST 4 : AI_rat alone --rat AIs\Test_Rat4.py --maze_file maze_files\Maze1.maze --auto_exit --test_file")
    giveResult(testEgaliteFile("testFiles/minutesFiles/NewMinutesFile","testFiles/minutesFiles/Test4"))
    
def runTest5():    
    print("TEST 5 : AI_python alone --python AIs\Test_Python5.py --maze_file maze_files\Maze1.maze --auto_exit --test_file")
    giveResult(testEgaliteFile("testFiles/minutesFiles/NewMinutesFile","testFiles/minutesFiles/Test5"))
    
def main():
    runTest1()  
    #runTest2()
    #runTest3()
    #runTest4()
    #runTest5()
    
if __name__ == "__main__":
    main()
    