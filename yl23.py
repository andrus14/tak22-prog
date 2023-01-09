import random

def choose_card():
    next_suit = random.choice(suits)
    next_rank = random.choice(ranks)

    while (next_suit + next_rank) in used_cards:
        next_suit = random.choice(suits)
        next_rank = random.choice(ranks)

    used_cards.append(next_suit + next_rank)

    return [next_suit, next_rank]

def get_hand_score(hand):
    score = 0
    for card in hand:
        rank = card[1]
        if rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            score += int(rank)
        elif rank in ['poiss', 'emand', 'kuningas']:
            score += 10
        else:
            score += 11

    return score

suits = ['ärtu', 'poti', 'risti', 'ruutu']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'poiss', 'emand', 'kuningas', 'äss']
used_cards = []

player_hand = []
dealer_hand = []

for i in range(2):
    player_hand.append(choose_card())
    dealer_hand.append(choose_card())

print(player_hand, get_hand_score(player_hand))
print(dealer_hand, get_hand_score(dealer_hand))
