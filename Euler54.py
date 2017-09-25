class Card:
    def __init__(self, text):
        val = text[0]
        suit = text[1]
        self.val = None

        try:
            self.val = int(val)
        except:
            if val=="T":
                self.val = 10
            if val == "J":
                self.val = 11
            if val == "Q":
                self.val = 12
            if val == "K":
                self.val = 13
            if val == "A":
                self.val = 14
        
        if suit == "H":
            self.suit = "Heart"
        if suit == "D":
            self.suit = "Diamond"
        if suit == "S":
            self.suit = "Spade"
        if suit == "C":
            self.suit = "Club"
    
    def __repr__(self):
        if self.val > 10:
            if self.val == 11:
                num_string = "Jack"
            if self.val == 12:
                num_string = "Queen"
            if self.val == 13:
                num_string = "King"
            if self.val == 14:
                num_string = "Ace"
        else:
            num_string = str(self.val)
        
        return num_string +" of " + self.suit + "s"

class Hand:

    def score_hand(self):
        vals = [card.val for card in self.cards]
        suits = [card.suit for card in self.cards]

        
        num_suits = len(set(suits))

        unique_vals = list(set(vals))
        unique_vals.sort(key=lambda x: -x)
        for i in range(0, len(unique_vals)):
            unique_vals[i]= [unique_vals[i], vals.count(unique_vals[i])]
        
        two_pairs = 0
        three_of_a_kind = 0
        four_of_a_kind = 0

        for unique in unique_vals:
            if unique[1] == 2:
                two_pairs +=1
            if unique[1]==3:
                three_of_a_kind+=1
            if unique[1]==4:
                high_card = unique[0]
                return (7, high_card, 0, 0, 0, 0)

        if three_of_a_kind == 1:
            for unique in unique_vals:
                if unique[1] == 3:
                    high_card = unique[0]
            if two_pairs == 1:
                return (6, high_card, 0, 0, 0, 0)
            return(3, high_card, 0, 0, 0, 0)
        
        if two_pairs == 2:
            high_cards = []
            for unique in unique_vals:
                if unique[1] == 2:
                    high_cards.append(unique[0])
            high_cards.sort(key=lambda x: -x)

            return(2, high_cards[0], high_cards[1], 0, 0, 0)
        
        if two_pairs == 1:
            for unique in unique_vals:
                if unique[1] == 2:
                    high_card = unique[0]
            high2 = 0
            for unique in unique_vals:
                if unique[0] > high2 and not unique[0]==high_card:
                    high2 = unique[0]
            return (1, high_card, high2, 0, 0, 0)
        
        high_card = max(vals)

        is_flush = num_suits == 1

        is_straight = vals == [num for num in range(min(vals), high_card + 1)]

        if is_flush is True:

            if is_straight is True:

                if high_card == 14:

                    return(9, 0, 0, 0, 0, 0)
                
                return (8, high_card, 0, 0, 0, 0)
            
            high2 = 0
            for val in vals:
                if val > high2 and not val == high_card:
                    high2 = val
            return (5, high_card, high2, 0, 0, 0)

        if is_straight is True:
            return (4, high_card, 0)

        vals.sort(key= lambda x: -x)

        return (0, vals[0], vals[1], vals[2], vals[3], vals[4])


    def __init__(self, cards):
        self.cards = cards
        self.cards.sort(key=lambda x: x.val)
        self.score= self.score_hand()
        print(self.score)

def player1_wins(hand1, hand2):

    if hand1.score[0] > hand2.score[0]:
        print("here")
        return True
    if hand1.score[0] == hand2.score[0]:
        if hand1.score[1] > hand2.score[1]:
            return True
        if hand1.score[1] == hand2.score[1]:
            if hand1.score[2] > hand2.score[2]:
                return True
            if hand1.score[2] == hand2.score[2]:
                if hand1.score[3] > hand2.score[3]:
                    return True
                if hand1.score[3] == hand2.score[3]:
                    if hand1.score[0] > hand2.score[0]:
                        return True
    return False


with open("poker_hands.txt", "r") as hands:
    count = 0
    wins = 0
    text = hands.read()
    text = text.split("\n")
    for game in text:
        print(game)
        count += 1
        print(count)
        hand1 = Hand([Card(c) for c in game.split()[0:5]])
        hand2 = Hand([Card(c) for c in game.split()[5:]])
        
        if player1_wins(hand1, hand2) is True:
            
            wins = wins + 1
        print(wins)
        