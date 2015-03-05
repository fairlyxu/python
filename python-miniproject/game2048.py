"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)} 


def creat_all_directions(num, initial_tiles,direction):
    """
    Create a move in the direction of the dictionary,the input need to traverse the grid number, 
    and reference list of ceramic tile, and direction (tuples)
    return the list in this direction
    """
    t_indices  = [] ; 
     
    for dummy_i in range(len(initial_tiles)):
        temp_tuple = initial_tiles[dummy_i]
        index0 = temp_tuple[0]
        index1 = temp_tuple[1]
        temp = [] ;
        #得到一个列表
        for dummy_j in range(num):
            temp.append((index0,index1));
            index0 +=  direction[0];
            index1 +=  direction[1];           
               
        t_indices.append(temp);
     
    return t_indices ;


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = remove_zero(line) 
    if len(line)>1:
        for dummy_i in range(len(result)-1):
            if(result[dummy_i]==result[dummy_i+1]):
                result[dummy_i]+=result[dummy_i+1]
                result[dummy_i+1] = 0
        result= remove_zero(result)  
    #0 补全      
    list_zero  = [0 for dummy_k in range(len(line)-len(result))];    
    result.extend(list_zero)   
     
    return result

def remove_zero(line):
    """
    remove all 0s in line
    """
    temp = [];
    for dummy_j in range(len(line)):
        if(line[dummy_j]!=0):
            temp.append(line[dummy_j])
    return temp


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height;
        self._grid_width = grid_width ;
        self._indices = dict();
         
        self.reset();
        # ready for move function,initial indices
        initial_left = [];
        initial_right = [] ;
        initial_top = [];
        initial_bottom = [];
        
        
        for dummy_i in range(grid_width): 
            initial_top.append(tuple([0,dummy_i]));
            initial_bottom.append(tuple([grid_height-1,dummy_i]))
        for dummy_i in range(grid_height): 
            initial_left.append(tuple([dummy_i,0]));
            initial_right.append(tuple([dummy_i,grid_width-1]))
        
        self._indices[UP] = creat_all_directions(self._grid_height, initial_top,OFFSETS[UP]);
        self._indices[DOWN] = creat_all_directions(self._grid_height, initial_bottom,OFFSETS[DOWN]);
        self._indices[LEFT] = creat_all_directions(self._grid_width, initial_left,OFFSETS[LEFT]);
        self._indices[RIGHT] = creat_all_directions(self._grid_width, initial_right,OFFSETS[RIGHT]);
        #more easier method :
        #self._indices = {UP:[(0,num) for num in range(grid_width)],
        #                DOWN:[(grid_height-1,num) for num in range(grid_width)],
        #                LEFT:[( num,0) for num in range(grid_height)],
        #                RIGHT:[( num,grid_height-1) for num in range(grid_height)]}
        
   

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [[ 0 for dummy_col in range(self._grid_width)] 
                             for dummy_row in range(self._grid_height)];
         
        self.new_tile();
        self.new_tile();
 
 

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """        
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):         
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # 1- Up  2- Down 3- Left 4- Right
        merge_titls_indices  = self._indices.get(direction) ;
        merge_titls_value  = [] ;
        
        # 得到需要合并的坐标 以及对应的值
        for dummy_i in range(len(merge_titls_indices)):
            tt_index = merge_titls_indices[dummy_i];
            temp_list = [] ; 
            for dummy_j in range(len(tt_index) ): 
                #get location (tuple)
                temp_location = tt_index[dummy_j];
                temp_list.append(self._cells[temp_location[0]][temp_location[1]])
             
            merge_titls_value.append(merge(temp_list));
               
        # 对cells 进行重新赋值
        for dummy_i in range(len(merge_titls_indices)):
            temp_list = [] ;
            for dummy_j in range(len(merge_titls_indices[dummy_i])):
                #get location (tuple)
                temp_location = merge_titls_indices[dummy_i][dummy_j];
                self.set_tile(temp_location[0], temp_location[1], merge_titls_value[dummy_i][dummy_j]) 
        # 需要考虑不产生新的tile的情况
        self.new_tile();

    def new_tile(self):         
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        value = 2
        count = 0 ;
        row_loca =  random.randint(0, self._grid_height-1)
        col_loca =  random.randint(0, self._grid_width-1)         
        while(self._cells[row_loca][col_loca]!= 0):
            count += 1;
            row_loca = random.randint(0, self._grid_height-1)
            col_loca = random.randint(0, self._grid_width-1) 
            if(count>self._grid_height*self._grid_width):
                return;
            
            
        if random.random() < 0.1:
            value = 4 
          
        self.set_tile(row_loca,col_loca,value)
         

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value ;

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """ 
        return self._cells[row][col];
 

poc_2048_gui.run_gui(TwentyFortyEight(4,4))
 

 
 
