from core.MazeInfo import *
from core.MazeGenerator import *

def giveResult(test):
    if test:
        print("----SUCCES")
    else:
        print("----FAILURE")

# Functions to test if a maze is connected and if maze/cheese is symmetric
def connected_region(cell, connected, maze):
    for (i,j) in maze[cell]:
        if connected[i][j] == 0:
            connected[i][j] = 1
            connected_region((i, j), connected, maze)

def connectedMazeTest(mazeInfo):
    width,height = mazeInfo.getMazeSize()
    maze = mazeInfo.getMaze()
    connected = [[0 for x in range(height)] for y in range(width)]
    connected[0][0] = 1
    connected_region((0,0), connected, maze)
    for i in range(width):
        for j in range(height):
            if connected[i][j] == 0:
                return False        
    return True

def symmetricMazeTest(mazeInfo):
    mazeWidth, mazeHeigth = mazeInfo.getMazeSize()
    maze = mazeInfo.getMaze()
    
    result = True
    for i in range(mazeWidth):
        for j in range(mazeHeigth):
            list_ij=[]
            list_ij_sym=[]

            for key in maze[(i,j)].keys():
                list_ij.append(key)
            for key in maze[(mazeWidth-1-i, mazeHeigth-1-j)]:
                list_ij_sym.append(key)
            list_ij.sort()
            list_ij_sym.sort()
            list_ij_sym.reverse()

            if len(list_ij) == len(list_ij_sym):
                for k in range(len(list_ij)):
                    if (mazeWidth - 1 - list_ij[k][0] != list_ij_sym[k][0]) or (mazeHeigth - 1 - list_ij[k][1] != list_ij_sym[k][1]):
                        result = False
                        return result  
            else:
                result = False
    
    return result

def symmetricCheeseTest(mazeInfo):
    result = True
    mazeWidth, mazeHeight = mazeInfo.getMazeSize()
    piecesOfCheese = mazeInfo.getPiecesOfCheese()
    piecesOfCheese.sort()
    piecesOfCheese_symm = []
    for k in range(len(piecesOfCheese)):
        val = piecesOfCheese[k]
        piecesOfCheese_symm.append((mazeWidth-1-val[0],mazeHeight-1-val[1]))
    
    piecesOfCheese_symm.sort()   
    
    for k in range(len(piecesOfCheese)):
        if (piecesOfCheese[k][0] != piecesOfCheese_symm[k][0]) or (piecesOfCheese[k][1] != piecesOfCheese_symm[k][1]):
            result = False
            return result   
    
    
    return result    



# Tests to test the connected tests
def checkTest_connected_unitTest(width, height, target_density, connected, symmetry, mud_density, mud_range, maze_file, seed, nb_pieces, start_random):
    mazeInfo = MazeGenerator.generateMaze(width, height, target_density, connected, symmetry, mud_density, mud_range, maze_file, seed, nb_pieces, start_random)
    if not (connectedMazeTest(mazeInfo)):
        print("Maze Connected Error : "+maze_file+" maze detected as nonconnected but it should")
        return False
    return True
        
def checkTest_nonConnected_unitTest(width, height, target_density, connected, symmetry, mud_density, mud_range, maze_file, seed, nb_pieces, start_random):
    mazeInfo = MazeGenerator.generateMaze(width, height, target_density, connected, symmetry, mud_density, mud_range, maze_file, seed, nb_pieces, start_random)
    if (connectedMazeTest(mazeInfo)):
        print("Maze Connected Error : "+maze_file+" maze detected as connected but it should")
        return False
    return True


def checkTest_connectedTest():
    result = True
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze2_x3_y3_p1_connect_symm.maze", 0.5, 10, False)       
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze3_x2_y2_p2_connect_symm.maze", 0.5, 10, False)           
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze4_x2_y10_p4_connect_symm.maze", 0.5, 10, False)        
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze5_x1_y10_p4_connect_symm.maze", 0.5, 10, False)
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze6_x11_y10_p6_connect_symm.maze", 0.5, 10, False)        
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze7_x20_y20_p40_connect_symm.maze", 0.5, 10, False)
   
        
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze8_x3_y3_p1_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze9_x2_y2_p2_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze10_x2_y10_p4_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze11_x1_y10_p4_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze12_x11_y10_p6_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze13_x20_y20_p40_nonconnect_symm.maze", 0.5, 10, False)
    
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze14_x3_y3_p1_connect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze16_x2_y10_p4_connect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze17_x11_y10_p6_connect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_connected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze18_x20_y20_p40_connect_nonsymm.maze", 0.5, 10, False)
    
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze20_x3_y3_p1_nonconnect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze21_x2_y10_p4_nonconnect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze22_x1_y10_p4_nonconnect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze23_x11_y10_p6_nonconnect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonConnected_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze24_x20_y20_p40_nonconnect_nonsymm.maze", 0.5, 10, False)
    
    return result
# Tests to test the symmetric tests
def checkTest_symmetric_unitTest(width, height, target_density, connected, symmetry, mud_density, mud_range, maze_file, seed, nb_pieces, start_random):
    mazeInfo = MazeGenerator.generateMaze(width, height, target_density, connected, symmetry, mud_density, mud_range, maze_file, seed, nb_pieces, start_random)
    if not (symmetricMazeTest(mazeInfo)):
        print("Maze Symmetric Error : "+maze_file+" maze detected as nonsymmetric but it should")
        return False
    if not (symmetricCheeseTest(mazeInfo)):
        print("Cheese Symmetric Error : "+maze_file+" cheese detected as nonsymmetric but it should")
        print(mazeInfo.getPiecesOfCheese())
        return False
    return True
        
def checkTest_nonSymmetric_unitTest(width, height, target_density, connected, symmetry, mud_density, mud_range, maze_file, seed, nb_pieces, start_random):
    mazeInfo = MazeGenerator.generateMaze(width, height, target_density, connected, symmetry, mud_density, mud_range, maze_file, seed, nb_pieces, start_random)
    if (symmetricMazeTest(mazeInfo)):
        print("Maze Symmetric Error : "+maze_file+" maze detected as symmetric but it should not")
        return False
    if (symmetricCheeseTest(mazeInfo)):
        print("Cheese Symmetric Error : "+maze_file+" cheese detected as symmetric but it should not")
        return False
    
    return True
    

def checkTest_symmetricTest():
    result = True
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze2_x3_y3_p1_connect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze3_x2_y2_p2_connect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze4_x2_y10_p4_connect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze5_x1_y10_p4_connect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze6_x11_y10_p6_connect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze7_x20_y20_p40_connect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze8_x3_y3_p1_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze9_x2_y2_p2_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze10_x2_y10_p4_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze11_x1_y10_p4_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze12_x11_y10_p6_nonconnect_symm.maze", 0.5, 10, False)
    result = result and checkTest_symmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze13_x20_y20_p40_nonconnect_symm.maze", 0.5, 10, False)
    
    result = result and checkTest_nonSymmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze14_x3_y3_p1_connect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonSymmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze16_x2_y10_p4_connect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonSymmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze17_x11_y10_p6_connect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonSymmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze18_x20_y20_p40_connect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonSymmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze20_x3_y3_p1_nonconnect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonSymmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze21_x2_y10_p4_nonconnect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonSymmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze22_x1_y10_p4_nonconnect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonSymmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze23_x11_y10_p6_nonconnect_nonsymm.maze", 0.5, 10, False)
    result = result and checkTest_nonSymmetric_unitTest(20, 20, 0.3, True, True, 0.7, 10, "maze_files\Maze24_x20_y20_p40_nonconnect_nonsymm.maze", 0.5, 10, False)    
    
    return result


def checkTest():
    print("Check Test : Connected Tests")
    giveResult(checkTest_connectedTest())
    print("\n Check Test : Symmetric Tests")
    giveResult(checkTest_symmetricTest())
    
def checkGenerator(nbTests):
    print("Check generator : "+str(nbTests)+" tests")
    errorsConnected = nbTests
    errorsMazeSym = nbTests
    errorsCheeseSym = nbTests
    
    for i in range(nbTests):
        mazeInfo = MazeGenerator.generateMaze(27, 21, 0.7, True, True, 0.1, 10, "", random.randint(0,sys.maxsize), 41, False)
        errorsConnected -= connectedMazeTest(mazeInfo)
        errorsMazeSym -= symmetricMazeTest(mazeInfo)
        errorsCheeseSym -= symmetricCheeseTest(mazeInfo)
    
    if errorsMazeSym==0 and errorsCheeseSym==0 and errorsConnected==0:
        print("----SUCCESS")
    else:
        print("----ERROR")
        print("Maze non connected : "+str(errorsConnected)+"/"+str(nbTests))
        print("Maze non symmetric : "+str(errorsMazeSym)+"/"+str(nbTests))
        print("Cheese non symmetric : "+str(errorsCheeseSym)+"/"+str(nbTests))
        
def main():
    
    checkTest()
    #checkGenerator(10000)
            
if __name__ == "__main__":
    main()
