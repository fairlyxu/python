"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 50         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player-machine
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

 
     
def mc_trial(board, player):
    """
    This function takes a current board and the next player to move. 
    The function should play a game starting with the given player by making random moves, alternating between players. The function should return when the game is over. The modified board will contain the state of the game, so the function does not return anything. 
    In other words, the function should modify the board input.
    """
    
 
    empty_lst = board.get_empty_squares();
    while(len(empty_lst)>0 and board.check_win()==None):
        empty_lst = board.get_empty_squares();
          
        pos = random.choice(empty_lst);
 
        board.move(pos[0],pos[1],player);
        player = provided.switch_player(player);

def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, a board from a completed game, and which player the machine player is. The function should score the completed board and update the scores grid. As the function updates the scores grid directly, it does not return anything
    """
    board_state = board.check_win();
     
    
    
    if(board_state==provided.DRAW):
        return ;
    
    elif(board_state==player):
        tem_score =  SCORE_CURRENT ;
        tem_score1 =  - SCORE_OTHER ;
    else:
        tem_score =  -SCORE_CURRENT ;
        tem_score1 =  SCORE_OTHER ;
        
    for dummy_row in range(board.get_dim()):
            for dummy_col in range(board.get_dim()):
                if(board.square(dummy_row,dummy_col)==provided.EMPTY):
                     
                    scores[dummy_row][dummy_col] += 0;
                elif(board.square(dummy_row,dummy_col)== player):
                    
                    scores[dummy_row][dummy_col] += tem_score ;
                else :
                    
                    scores[dummy_row][dummy_col] += tem_score1;                
     
def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The function should find all of the empty squares with the maximum score and randomly return one of them as a (row, column) tuple. It is an error to call this function with a board that has no empty squares (there is no possible next move), so your function may do whatever it wants in that case. The case where the board is full will not be tested.
    """
    
    empty_lst = board.get_empty_squares();
    max_score = -1000000 ;
    row = col = row1 = col1= 0;
    if(len(empty_lst)>0):
        #print empty_lst;
        for dummy_i in range(len(empty_lst)):
            
            row = empty_lst[dummy_i][0] ;
            col = empty_lst[dummy_i][1] ;
            
            if(max_score<scores[row][col]):
                
                max_score = scores[row][col]
                row1 = empty_lst[dummy_i][0];
                col1 = empty_lst[dummy_i][1]
                 
         
        return tuple([row1,col1]) ;
    else:
        return ; 
         
def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and the number of trials to run. The function should use the Monte Carlo simulation described above to return a move for the machine player in the form of a (row, column) tuple. Be sure to use the other functions you have written!
    """
    scores = [[0 for dummy_col in range(board.get_dim())]
                 for dummy_row in range(board.get_dim())]
    for dummy_count in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board, player);
        mc_update_scores(scores, trial_board, player);
    
    position = get_best_move(board, scores);
     
    return position
     
        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
