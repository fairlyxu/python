"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    #hand_set = set(hand);
    score_result = 0 ;
    for item in  set(hand) :  
        score_temp  = item*hand.count(item);         
        if(score_result < score_temp):
            score_result = score_temp
    return score_result;


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcome = list();
    total_sum = 0.0 ;
    for dummy_dix in range(num_die_sides):
        outcome.append(dummy_dix+1);
    all_sequences = gen_all_sequences(outcome,num_free_dice); 
    result_list = list(all_sequences ); 
    for dummy_tuple in  result_list :
        total_sum += score(dummy_tuple+held_dice); 
    return  total_sum/len(result_list); 
      
def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    lst = ([()])
    for i in range(len(hand)):
        temp_lst = []
        for item in lst:
            for num in range(2):
                temp_seq = list(item)
                temp_seq.append(num)
                temp_lst.append(temp_seq)
        lst = temp_lst
 
     
    result = set();
    for temp_list in lst:
        entry_t = [];
        for dummy_i in range(len(temp_list)): 
            if(temp_list[dummy_i]==1):
                entry_t.append(hand[dummy_i]); 
        result.add(tuple(entry_t));
    """
    ans = set([()]) 
    for out in hand:
        temp = set(ans)
        for item in temp:
            item_temp = list(item)
            ans.add(item)
            item_temp.append(out)
            ans.add(tuple(item_temp)) 
    return ans;



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_score = 0.0 ;
    num_dics = len(hand);
    all_held_dice = gen_all_holds(hand) ;
     
    held_dice = set();
    for dummy_dice in (all_held_dice) :        
        expected_val = expected_value(dummy_dice,num_die_sides,num_dics-len(dummy_dice)) ;
        if(max_score < expected_val):
            max_score = expected_val ;
            held_dice =  dummy_dice
            #print 'max_score',max_score,'held_dice' ,held_dice
    return (max_score, held_dice);


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
         
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



