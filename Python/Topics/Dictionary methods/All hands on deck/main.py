deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
deck_values = dict(zip(deck, value))
hand = [input() for _ in range(6)]
hand_values = [deck_values.get(card) for card in hand]
print(sum(hand_values) / 6)
