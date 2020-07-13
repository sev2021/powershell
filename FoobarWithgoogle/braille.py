# From foobar.withgoogle.com

def solution(s):
    # Your code here
    to_bri = "i jw    s t a e c d kuozmxnyb h f g lvr p q"
    bri = []
    for i in s:
        if i.isupper():
            bri.append("000001")
        i = i.lower()
        if i == " ":
            bri.append("000000")
        else:
            bri.append(bin(to_bri.index(i)+20)[2:].rjust(6,"0"))
    return "".join(bri)
    
    
# Other solutions: 
# https://py.checkio.org/mission/braille-translator/publications/DiZ/python-3/first/share/36cbcda5ba5c6e7ebe0e18d257517c62/


def braille_page(txt, table=' C       _     N, -.i j  ?! s twa e c d kuozmxnyb h f g lvr p q'):
    ''' Convert a text in Braille given a translation table.'''
    #Normalize text symbols
    sanitized = ''.join('C'*c.isupper() + 'N'*c.isdigit() \
        + chr(ord(c) + 32*c.isupper() + 48*c.isdigit() + 10*(c=='0')) for c in txt)
    #Transcrypt in Braille inline
    binary = ''.join(bin(table.index(c) + 64 << 3)[3:] for c in sanitized) \
        + '0'*9*(len(sanitized) > 10 and -len(sanitized) % 10)
    #Format output in 10-character chunks
    formatted = ['0'.join(binary[m:m+3] for m in range(n*3, len(binary), 90)) \
        for n in range(3 * min(10, len(sanitized)) - 1)]
    return [list(map(int, l)) for l in zip(*formatted)]
