"""
Mini-project # 6 - Blackjack
需求：21点  https://class.coursera.org/interactivepython-005/human_grading/view/courses/972530/assessments/33/results/mine
"""
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
player_score = 0
dealer_score = 0
promot = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand_list = [];

    def __str__(self):
        # return a string representation of a hand
         ans = ""
         for i in range(len(self.hand_list)):
             ans += str(self.hand_list[i])+" ";
         return ans ;

    def add_card(self, card):
        # add a card object to a hand
         self.hand_list.append(card);

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0;
        exit_A = 0 ;
        for card in self.hand_list:
            value += VALUES.get(card.rank)
            if('A'==card.rank):
                exit_A +=1;
        if(exit_A>0 and value+10<=21):
            value+=10;
        return value;
            
        # compute the value of the hand, see Blackjack video   
    def draw(self, canvas, pos):
        i=0;
        for card in self.hand_list:
            #print type(card)
            card.draw(canvas,(pos[0]+i*CARD_SIZE[0],pos[1]))            
            i+=1;
       
# define deck class 
class Deck:
    def __init__(self):
        self.deck_list =[];
        for i in range(len(SUITS)):
            for j in range(len(RANKS)) :
                self.deck_list.append(Card(SUITS[i],RANKS[j]))
     # create a Deck object       

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_list);

    def deal_card(self):
        if(len(self.deck_list)>0):
            return self.deck_list.pop();
        else:
            print 'no deck left'
        # deal a card object from the deck
    
    def __str__(self):
        ans = ""
        for i in range(len(self.deck_list)):
            ans +=str(self.deck_list[i])+" ";
        return ans ;	 

deck = Deck();
#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer,promot,dealer_score
    # your code goes here
    promot = "Hit or stand?";
    outcome = "";
    if(in_play):
           promot = "Hit or stand?";
           outcome = "You conceded";
           dealer_score += 1 ;
           #in_play = False ;
    
    deck = Deck();
    

    player = Hand();
    dealer = Hand();
    deck.shuffle();
    card1  = deck.deal_card();
    card2  = deck.deal_card();
    card3  = deck.deal_card();
    card4  = deck.deal_card();
    print card1 ,card2,card3 ,card4
    player.add_card(card1);player.add_card(card2);
    dealer.add_card(card2);dealer.add_card(card4);
    in_play = True

def hit():
    # replace with your code below
    global outcome, in_play, deck, player, dealer,dealer_score ,promot;
    # if the hand is in play, hit the player
    if(in_play):
        card1  = deck.deal_card();
        player.add_card(card1);
        if( player.get_value() <= 21):            
            promot = "Hit or stand?";
        
    # if busted, assign a message to outcome, update in_play and score
        else:
           in_play = False;
           promot = "Hit or stand?";
           outcome = "You have busted"
           dealer_score += 1 ;
    
def stand():
    # replace with your code below   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global outcome, in_play ,dealer_score,player_score,promot;
    if(in_play):
        while(in_play and dealer.get_value() <17 ):
            card = deck.deal_card();
            dealer.add_card(card);
            if(dealer.get_value() > 21):
                in_play = False;
                player_score += 1 ;
                #promot = "Dealer have busted";
                outcome = "Dealer have busted";
               
        # assign a message to outcome, update in_play and score
        in_play = False ;
        if(dealer.get_value() <=21 and dealer.get_value() >= player.get_value()):
            outcome = "dealer win ";   
            dealer_score += 1 ;
           
        elif(dealer.get_value() <= 21) :
            outcome = "You win ";
            player_score += 1 ;
           
        promot = "New deal?"; 
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Game---Blackjack', [30, 50], 30, 'white');
    canvas.draw_text('score->dealer: player' , [300, 50], 25, 'black');
    canvas.draw_text(str(dealer_score)+" : "+str(player_score), [442, 80], 25, 'black');   
    canvas.draw_text('Dealer'  , [30, 150], 25, 'black');
    canvas.draw_text('Player'  , [30, 350], 25, 'black');
    canvas.draw_text(outcome  , [330, 150], 25, 'black');
    canvas.draw_text(promot  , [330, 350], 25, 'black'); 
    dealer.draw(canvas, (30,170));
    player.draw(canvas, (30,370));
    if(in_play):
        canvas.draw_image(card_back, (CARD_CENTER[0]+CARD_SIZE[0],CARD_CENTER[1]), CARD_SIZE, (66,218), CARD_SIZE)        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
# remember to review the gradic rubric