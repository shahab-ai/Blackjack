from deck import Card
value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
              'K': 10, 'A': (1, 11)}

def calc_cards_sum(cards, total=0):

    if total == 0 and len(cards) == 2 and \
       ''.join(map(lambda x:x.number, cards)) == 'AA':
        return 21

    if len(cards) == 0:
        return total

    else:
        card = cards[0]
        if card.number != 'A':
            return calc_cards_sum(cards[1:],
                                  total + value_dict[card.number])
        else:
            total1 = calc_cards_sum(cards[1:], total + 1)
            total2 = calc_cards_sum(cards[1:], total + 11)
            canonical_total = list(filter(lambda x: x <= 21, [total1, total2]))
            if len(canonical_total)!=0:
                return max(canonical_total)
            else:
                return min(total1, total2)
