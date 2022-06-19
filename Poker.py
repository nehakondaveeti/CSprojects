#  File: Poker.py

#  Description: Simulate a Poker Game, knows as the 5-card draw.

#  Student's Name: Neha Kondaveeti

#  Student's UT EID: nk8975

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 02/17

#  Date Last Modified: 02/18

import sys, random

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    # 11 --> jack
    # 12 --> Queen
    # 13 --> King
    # 14 --> Ace

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str (self.rank)
        return rank + self.suit

    # equality tests
    def __eq__ (self, other):
        return self.rank == other.rank

    def __ne__ (self, other):
        return self.rank != other.rank

    def __lt__ (self, other):
        return self.rank < other.rank

    def __le__ (self, other):
        return self.rank <= other.rank

    def __gt__ (self, other):
        return self.rank > other.rank

    def __ge__ (self, other):
        return self.rank >= other.rank

class Deck (object):
  # constructor
    def __init__ (self, num_decks = 1):
        self.deck = []
        for i in range (num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card (rank, suit)
                    self.deck.append (card)

  # shuffle the deck
    def shuffle (self):
        random.shuffle (self.deck)

  # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker (object):
  # constructor
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []
        self.numCards_in_Hand = num_cards

    # deal all the hands
        for i in range (num_players):
            hand = []
            for j in range (self.numCards_in_Hand):
                hand.append (self.deck.deal())
            self.players_hands.append (hand)

  # simulate the play of the game
    def play (self):
    # sort the hands of each player and print the hand
        for i in range (len(self.players_hands)):
            sorted_hand = sorted (self.players_hands[i], reverse = True)
            self.players_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print ('Player ' + str(i + 1) + ' : ' + hand_str)

        hand_type = []	# create a list to store type of hand
        hand_points = []

        for i in range(len(self.players_hands)):
            hp, ht = self.is_high_card(self.players_hands[i])
            hand_type.append(ht)
            hand_points.append(hp)
            if hand_points[i] < self.is_one_pair(self.players_hands[i])[0]:
                hand_points[i], hand_type[i] = self.is_one_pair(self.players_hands[i])
            if hand_points[i] < self.is_two_pair(self.players_hands[i])[0]:
                hand_points[i], hand_type[i] = self.is_two_pair(self.players_hands[i])
            if hand_points[i] < self.is_three_kind(self.players_hands[i])[0]:
                hand_points[i], hand_type[i] = self.is_three_kind(self.players_hands[i])
            if hand_points[i] < self.is_straight(self.players_hands[i])[0]:
                hand_points[i], hand_type[i] = self.is_straight(self.players_hands[i])
            if hand_points[i] < self.is_flush(self.players_hands[i])[0]:
                hand_points[i], hand_type[i] = self.is_flush(self.players_hands[i])
            if hand_points[i] < self.is_full_house(self.players_hands[i])[0]:
                hand_points[i], hand_type[i] = self.is_full_house(self.players_hands[i])
            if hand_points[i] < self.is_four_kind(self.players_hands[i])[0]:
                hand_points[i], hand_type[i] = self.is_four_kind(self.players_hands[i])
            if hand_points[i] < self.is_straight_flush(self.players_hands[i])[0]:
                hand_points[i], hand_type[i] = self.is_straight_flush(self.players_hands[i])
            if hand_points[i] < self.is_royal(self.players_hands[i])[0]:
                hand_points[i], hand_type[i] = self.is_royal(self.players_hands[i])
        
        
        print()

        winner = 0
        for i in range(len(self.players_hands)):
            print('Player '+ str(i+1) +': '+ str(hand_type[i]))
            if hand_points[i] > hand_points[winner]:
                winner = i

        tie = False
        tp = []
        tp.append((winner, hand_points[winner]))
        for i in range(len(self.players_hands)):
            if winner != i:
                if hand_type[i] == hand_type[winner]:
                    tie = True
                    tp.append((i,hand_points[i]))

        #sort tp by hand_points
        
        for i in range(0,len(tp)):
            for j in range(0,len(tp)-i-1):
                if(tp[j][1] < tp[j+1][1]):
                    temp = tp[j] 
                    tp[j]= tp[j + 1] 
                    tp[j + 1]= temp 
        

        print()
        if tie:
            for i in range(len(tp)):
                
                print('Player',tp[i][0]+1,'ties.')

        else:
            
            print('Player',winner+1,'wins.') 


    # determine the type of each hand and print
    	# create a list to store points for hand

    # determine the winner and print 


    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
             same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
          return 0, ''

        rank_order = True
        for i in range (len(hand)):
          rank_order = rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):
          return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'


    # determine if a hand is a straight flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_straight_flush (self, hand):
        # has straight flush if it has BOTH straight and flush hands
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        # straight flush is all same suit
        if (not same_suit):
            return 0, ''

        # checks if rank
        rank_order = True
        for i in range (len(hand)-1):
            rank_order = rank_order and (hand[i].rank == hand[i+1].rank+1)

        if (not rank_order):
            return 0, ''

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush'

    def is_four_kind (self, hand):
        four = False
        track = []
        for i in range (len(hand) - 3):
            if (hand[i].rank == hand[i + 1].rank and hand[i].rank == hand[i + 2].rank and hand[i].rank == hand[i+3].rank):
                four = True
                track.append(i)
                track.append(i+1)
                track.append(i+2)
                track.append(i+3)
                break
        if (not four):
            return 0, ''

        points = 8 * 15 ** 5 + (hand[track[0]].rank) * 15 ** 4 + (hand[track[1]].rank) * 15 ** 3
        points = points + (hand[track[2]].rank) * 15 ** 2 + (hand[track[3]].rank) * 15 ** 1
        
        for i in range(len(hand)):
            if i not in track:
                points = points + hand[i].rank
        return points, 'Four of a Kind'

    def is_full_house (self, hand):
        full = False
        points = 7 * 15 ** 5
        if (hand[0].rank == hand[1].rank and hand[0].rank == hand[2].rank and hand[3].rank == hand[4].rank):
            points = points + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
            full = True
        elif(hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank and hand[2].rank == hand[4].rank):
            points = points + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3 + (hand[4].rank) * 15 ** 2 +  (hand[0].rank) * 15 ** 1 + (hand[1].rank)
            full = True
        else:
            return 0, ''
            
        return points, 'Full House'

    def is_flush (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        # straight flush is all same suit
        if (not same_suit):
            return 0, ''
        
        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points 

        return points, 'Flush'

    def is_straight (self, hand):
        rank_order = True
        for i in range (len(hand)-1):
            rank_order = rank_order and (hand[i].rank == hand[i+1].rank+1)

        if (not rank_order):
            return 0, ''

        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight'

    def is_three_kind (self, hand):
        three = False
        track = []
        points = 4 * 15 ** 5
        for i in range (len(hand) - 2):
            if (hand[i].rank == hand[i + 1].rank and hand[i].rank == hand[i + 2].rank):
                three = True
                track.append(i)
                track.append(i+1)
                track.append(i+2)
                break
        if (not three):
            return 0, ''
        points = points + (hand[track[0]].rank) * 15 ** 4 + (hand[track[1]].rank) * 15 ** 3 + (hand[track[2]].rank) * 15 ** 2
        j = 1
        for i in range(len(hand)):
            if i not in track:
                points = points + hand[i].rank * 15 ** j
                j -= 1

               
        
        j = 2
        for i in range(len(hand)):
            if i not in track:
                points = points + hand[i].rank * 15 ** j
                j -= 1

        points = points + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points, 'Three of a Kind'

    def is_two_pair (self, hand):
        track = []
        one_pair = False
        two_pair = False
        for i in range (len(hand) - 1):
            if (not one_pair  and hand[i].rank == hand[i + 1].rank):
                one_pair = True
                track.append(i)
                track.append(i+1)
                i = i + 1
                if i == len(hand)-1:
                    break
            if one_pair:
                if (hand[i].rank == hand[i + 1].rank):
                    two_pair = True
                    track.append(i)
                    track.append(i+1)
        if (not two_pair):
            return 0, ''

        points = 3 * 15 ** 5 + (hand[track[0]].rank) * 15 ** 4 + (hand[track[1]].rank) * 15 ** 3
        points = points + (hand[track[2]].rank) * 15 ** 2 + (hand[track[3]].rank) * 15 ** 1
        
        for i in range(len(hand)):
            if i not in track:
                points = points + hand[i].rank

        return points, 'Two Pair'

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
    def is_one_pair (self, hand):
        track = []
        one_pair = False
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                one_pair = True
                track.append(i)
                track.append(i+1)
                break
        if (not one_pair):
            return 0, ''

        points = 2 * 15 ** 5 
        points = points + (hand[track[0]].rank) * 15 ** 4 + (hand[track[1]].rank) * 15 ** 3
        j = 2
        for i in range(len(hand)):
            if i not in track:
                points = points + hand[i].rank * 15 ** j
                j -= 1
        
        return points, 'One Pair'

    def is_high_card (self,hand): 
        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points, 'High Card'


def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int (line)
    if (num_players < 2) or (num_players > 6):
        return

    # create the Poker object
    game = Poker (num_players)

    # play the game
    game.play()

if __name__ == "__main__":
    main()