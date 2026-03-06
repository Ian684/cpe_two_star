def create_number():
    number = {'A':14,'T':10,'J':11,'Q':12,'K':13}
    for i in range(2, 10):
        number[str(i)] = i
    return number

def create_suit():
    return {'C':1,'D':2,'H':3,'S':4}

def check(result):
    if result == 0:
        print("Black wins.")
    elif result == 1:
        print("White wins.")
    else:
        print("Tie.")

def get_counts(hand):
    counts = {}
    for val, suit in hand:
        counts[val] = counts.get(val, 0) + 1
    return counts

def straight_flush(black, white):
    def is_sf(hand):
        hand = sorted(hand)
        is_flush = all(c[1] == hand[0][1] for c in hand)
        is_straight = all(hand[i][0] == hand[i-1][0] + 1 for i in range(1, 5))
        return (is_flush and is_straight), hand[-1][0]

    b_ok, b_val = is_sf(black)
    w_ok, w_val = is_sf(white)
    
    if not b_ok and not w_ok: return False
    if b_ok and not w_ok: check(0)
    elif w_ok and not b_ok: check(1)
    else:
        if b_val > w_val: check(0)
        elif w_val > b_val: check(1)
        else: check(2)
    return True

def four_kind(black, white):
    def get_four(hand):
        counts = get_counts(hand)
        for val, count in counts.items():
            if count == 4: return True, val
        return False, 0

    b_ok, b_val = get_four(black)
    w_ok, w_val = get_four(white)
    
    if not b_ok and not w_ok: return False
    if b_ok and not w_ok: check(0)
    elif w_ok and not b_ok: check(1)
    else:
        if b_val > w_val: check(0)
        else: check(1)
    return True

def full_house(black, white):
    def get_fh(hand):
        counts = get_counts(hand)
        if len(counts) == 2 and 3 in counts.values():
            for val, count in counts.items():
                if count == 3: return True, val
        return False, 0

    b_ok, b_val = get_fh(black)
    w_ok, w_val = get_fh(white)
    
    if not b_ok and not w_ok: return False
    if b_ok and not w_ok: check(0)
    elif w_ok and not b_ok: check(1)
    else:
        if b_val > w_val: check(0)
        else: check(1)
    return True

def flush(black, white):
    def is_f(hand):
        is_flush = all(c[1] == hand[0][1] for c in hand)
        vals = sorted([c[0] for c in hand], reverse=True)
        return is_flush, vals

    b_ok, b_vals = is_f(black)
    w_ok, w_vals = is_f(white)
    
    if not b_ok and not w_ok: return False
    if b_ok and not w_ok: check(0)
    elif w_ok and not b_ok: check(1)
    else:
        if b_vals > w_vals: check(0)
        elif w_vals > b_vals: check(1)
        else: check(2)
    return True

def straight(black, white):
    def is_s(hand):
        vals = sorted([c[0] for c in hand])
        is_straight = all(vals[i] == vals[i-1] + 1 for i in range(1, 5))
        return is_straight, vals[-1]

    b_ok, b_val = is_s(black)
    w_ok, w_val = is_s(white)
    
    if not b_ok and not w_ok: return False
    if b_ok and not w_ok: check(0)
    elif w_ok and not b_ok: check(1)
    else:
        if b_val > w_val: check(0)
        elif w_val > b_val: check(1)
        else: check(2)
    return True

def three(black, white):
    def get_t(hand):
        counts = get_counts(hand)
        for val, count in counts.items():
            if count == 3: return True, val
        return False, 0

    b_ok, b_val = get_t(black)
    w_ok, w_val = get_t(white)
    
    if not b_ok and not w_ok: return False
    if b_ok and not w_ok: check(0)
    elif w_ok and not b_ok: check(1)
    else:
        if b_val > w_val: check(0)
        else: check(1)
    return True

def double_two(black, white):
    def get_tp(hand):
        counts = get_counts(hand)
        pairs = sorted([val for val, count in counts.items() if count == 2], reverse=True)
        if len(pairs) == 2:
            kicker = [val for val, count in counts.items() if count == 1][0]
            return True, pairs, kicker
        return False, [], 0

    b_ok, b_pairs, b_k = get_tp(black)
    w_ok, w_pairs, w_k = get_tp(white)
    
    if not b_ok and not w_ok: return False
    if b_ok and not w_ok: check(0)
    elif w_ok and not b_ok: check(1)
    else:
        if b_pairs > w_pairs: check(0)
        elif w_pairs > b_pairs: check(1)
        elif b_k > w_k: check(0)
        elif w_k > b_k: check(1)
        else: check(2)
    return True

def two(black, white):
    def get_p(hand):
        counts = get_counts(hand)
        pair_val = [val for val, count in counts.items() if count == 2]
        if len(pair_val) == 1:
            kickers = sorted([val for val, count in counts.items() if count == 1], reverse=True)
            return True, pair_val[0], kickers
        return False, 0, []

    b_ok, b_v, b_ks = get_p(black)
    w_ok, w_v, w_ks = get_p(white)
    
    if not b_ok and not w_ok: return False
    if b_ok and not w_ok: check(0)
    elif w_ok and not b_ok: check(1)
    else:
        if b_v > w_v: check(0)
        elif w_v > b_v: check(1)
        elif b_ks > w_ks: check(0)
        elif w_ks > b_ks: check(1)
        else: check(2)
    return True

def one(black, white):
    b_vals = sorted([c[0] for c in black], reverse=True)
    w_vals = sorted([c[0] for c in white], reverse=True)
    if b_vals > w_vals: check(0)
    elif w_vals > b_vals: check(1)
    else: check(2)
    return True

def main():
    number = create_number()
    suit = create_suit()
    while True:
        try:
            line = input().split()
        except EOFError:break
        if not line: continue
        
        black, white = [], []
        for i in line[:5]:
            black.append([number[i[0]], suit[i[1]]])
        for i in line[5:]:
            white.append([number[i[0]], suit[i[1]]])
        if straight_flush(black, white): continue
        if four_kind(black, white): continue
        if full_house(black, white): continue
        if flush(black, white): continue
        if straight(black, white): continue
        if three(black, white): continue
        if double_two(black, white): continue
        if two(black, white): continue
        one(black, white)

if __name__ == "__main__":
    main()
