def reverseOnlyLetters(s):
    positions = {idx:i for idx,i in enumerate(s)}
    letter_positions = {k:v for k,v in positions.items() if (65 <= ord(v) <= 90) or 97 <= ord(v) <= 122}
    letters = [v for _,v in letter_positions.items()]
    letters = letters[::-1]
    for let_pos,val in zip(letter_positions.keys(),letters):
        letter_positions[let_pos] = val

    for k,v in letter_positions.items():
        positions[k] = v
    
    ns = ''.join([k for _,k in positions.items()])
    return ns
