#python2
def get_rank_h(card):
    if '2' <= card[0] <= '9':
        return ord(card[0]) - ord('0')
    if card[0] == 'T': return 10
    if card[0] == 'J': return 11
    if card[0] == 'Q': return 12
    if card[0] == 'K': return 13
    if card[0] == 'A': return 14
    
    
def get_rank_l(card):
    if '2' <= card[0] <= '9':
        return ord(card[0]) - ord('0')
    if card[0] == 'T': return 10
    if card[0] == 'J': return 11
    if card[0] == 'Q': return 12
    if card[0] == 'K': return 13
    if card[0] == 'A': return 1

    
def main():
    # cards = input().split()
    cards =  ["2D" ,"5D" ,"3D" ,"4D" ,"6D"]
    print(cards)
    same_suits = len(set(map(lambda x: x[1], cards))) == 1
    values_h = sorted(map(get_rank_h, cards))
    values_l = sorted(map(get_rank_l, cards))
    good_ranks = max(values_h) - min(values_h) == 4 or \
                 max(values_l) - min(values_l) == 4 
    print('YES' if same_suits and good_ranks else 'NO')
    
    
if __name__ == '__main__':
    main()
    