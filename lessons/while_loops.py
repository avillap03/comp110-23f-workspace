"""Demonstarte while loops by finding low values in string"""

cards: str = "523561"

card_index: int = 0
low_card: int = int(cards[0])
#look at each number in the string
while card_index < 6:
    #check if current card is less than low card
    current_card: int = int(cards[card_index])
    if (current_card < low_card):
        #update the low card to be the value the current card 
        low_card = current_card
    card_index = card_index + 1
print (low_card)