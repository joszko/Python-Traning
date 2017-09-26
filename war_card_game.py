# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:

    # This is the Deck Class. This object will create a deck of cards to initiate
    # play. You can then use this Deck list of cards to split in half and give to
    # the players. It will use SUITE and RANKS to create the deck. It should also
    # have a method for splitting/cutting the deck in half and Shuffling the deck.

    def __init__(self):
        self.deck = [(s, r) for s in SUITE for r in RANKS]

    def shuffle_split(self):
        shuffle(self.deck)
        return self.deck[:26], self.deck[26:]


class Hand:

    # This is the Hand class. Each player has a Hand, and can add or remove
    # cards from that hand. There should be an add and remove card method here.

    def __init__(self, cards):
        self.cards = cards

    # for printing the hand
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add_card(self, new_cards):
        self.cards.extend(new_cards)

    # pop() returns the removed object from the list.
    def remove_card(self):
        return self.cards.pop()


class Player:

    # This is the Player class, which takes in a name and an instance of a Hand
    # class object. The Payer can then play cards and check if they still have cards.

    def __init__(self, player_name, hand):
        self.name = player_name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        # return True if player has cards left
        return len(self.hand.cards) != 0


# GAME PLAY

# Create a new deck, shuffle the cards and split the deck in half

deck = Deck()
hand_1, hand_2 = deck.shuffle_split()

# Create players
player_1 = Player("Computer", Hand(hand_1))

name = input("Provide name: ")
player_2 = Player(name, Hand(hand_2))

total_rounds = 0
war_count = 0

while player_1.still_has_cards() and player_2.still_has_cards():
    total_rounds += 1
    print("new round")
    print(player_2.name + " has the count" + str(len(player_2.hand.cards)))
    print(player_1.name + " has the count" + str(len(player_1.hand.cards)))
    print("Play a card")
    print("\n")

    cards_on_table = []
    player_1_card = player_1.play_card()
    player_2_card = player_2.play_card()

    cards_on_table.append(player_1_card)
    cards_on_table.append(player_2_card)

    if player_1_card[1] == player_2_card[1]:
        war_count += 1
        print("WAR!")

        cards_on_table.extend(player_1.remove_war_cards())
        cards_on_table.extend(player_2.remove_war_cards())

        player_1_card = player_1.play_card()
        player_2_card = player_2.play_card()

        cards_on_table.append(player_1_card)
        cards_on_table.append(player_2_card)

        if RANKS.index(player_1_card[1]) < RANKS.index((player_2_card[1])):
            player_2.hand.add_card(cards_on_table)
        else:
            player_1.hand.add_card(cards_on_table)

    else:
        if RANKS.index(player_1_card[1]) < RANKS.index((player_2_card[1])):
            player_2.hand.add_card(cards_on_table)
        else:
            player_1.hand.add_card(cards_on_table)

print("Game Over")
print("Number of rounds: " + str(total_rounds))
print("War happened " + str(war_count) + " times")

if player_1.still_has_cards():
    print(player_1.name + " won!")
else:
    print(player_2.name + "won!")
