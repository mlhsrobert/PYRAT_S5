from core.parameters import *
import importlib.util
import sys
import time
import traceback

class AIManager:
    
    def run(pet, filename, q1FromPlayer, q2ToPlayer, width, height, preparation_time, turn_time):
        # Try to lauch a regular AI
        try:
            player = importlib.util.spec_from_file_location("player",filename)
            module = importlib.util.module_from_spec(player)
            player.loader.exec_module(module)
            name = module.TEAM_NAME
            preprocessing = module.preprocessing
            turn = module.turn
        # In case there is a problem, the dummy AI is launched (this AI does nothing)
        except:
            if filename != "":
                var = traceback.format_exc()
                print("Error: " + var, file=sys.stderr)
                print("Error while loading player controlling " + pet + ", dummy player loaded instead", file=sys.stderr)
            player = importlib.util.spec_from_file_location("player","AIs/dummyplayer.py")
            module = importlib.util.module_from_spec(player)
            player.loader.exec_module(module)        
            name = module.TEAM_NAME
            preprocessing = module.preprocessing
            turn = module.turn
            
        # Send the name to the Player
        q2ToPlayer.put(name)
        
        # Receive information from the Player for preprocessing
        maze, myLocation, otherPlayer_location, pieces_of_cheese = q1FromPlayer.get()
        
        # Call the preprocessing function and catch any exception
        try:
            before = time.time()
            preprocessing(maze, width, height, myLocation, otherPlayer_location, pieces_of_cheese, preparation_time)
            after = time.time()
            prep_time = after - before
        except Exception as e:
            prep_time = 0
            traceback.print_exc()
            print(e, file=sys.stderr,)
            
        # Run each turn through the loop
        turn_delay = 0
        turn_delay_count = 0        
        try:
            while 1:
                                           
                # Receive information from the Player for the turn                                                       
                try:
                    myLocation, otherPlayer_location, myScore, otherPlayer_score, pieces_of_cheese = q1FromPlayer.get()
                    while not(q1FromPlayer.empty()):
                        myLocation, otherPlayer_location, myScore, otherPlayer_score, pieces_of_cheese = q1FromPlayer.get() 
                except:
                    # Receive only "stop" to stop the match (insted of all information for the turn)
                    break
                
                # Call the turn function and catch any exception
                try:
                    before = time.time()
                    decision = turn(maze, width, height, myLocation, otherPlayer_location, 
                                    myScore, otherPlayer_score, pieces_of_cheese, turn_time)
                    after = time.time()
                    turn_delay = turn_delay + (after - before)
                    turn_delay_count = turn_delay_count + 1
                except Exception as e:
                    traceback.print_exc()
                    print(e, file=sys.stderr)
                    decision = "None"
                    
                # Send the decision to the Player
                try:                
                    q2ToPlayer.put(decision)
                except:
                    ()
        except:
            ()            
        
        # Receive information for postprocessing
        myLocation, otherPlayer_location, myScore, otherPlayer_score, pieces_of_cheese = q1FromPlayer.get()
        
        # Call the postprocessing function and catch any exception
        if not(args.prevent_postprocessing):
            try:
                module.postprocessing(maze, width, height, myLocation, otherPlayer_location, 
                                      myScore, otherPlayer_score, pieces_of_cheese, turn_time)
            except Exception as e:
                traceback.print_exc()        
                print(e, file=sys.stderr,)
        
        # Send information to the Player about delays
        if turn_delay_count!=0:
            q2ToPlayer.put((prep_time, turn_delay / turn_delay_count))
        else:
            q2ToPlayer.put((prep_time, 0))
