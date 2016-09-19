'''#-*- coding: utf8 -*-'''
# no problem with encoding in python3. use python3 man
# http://d2.naver.com/helloworld/76650

BASE = 0xAC00
END = 0xD7AF
CHO = 21*28
JUNG = 28

# chosung : 0 - 18
CHOLIST_D = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']
CHOLIST_S = [u'ㄱ', u'ㄱ', u'ㄴ', u'ㄷ', u'ㄷ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅂ', u'ㅅ', u'ㅅ', u'ㅇ', u'ㅈ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']
# jungsung : 0 - 20
#JUNG_LIST = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']
# jongsung : 0 - 27
#JONG_LIST = [u' ', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

def chosung(txt, mode = 0):
    """returns chosung of string
    
    >>> chosung(u'가나다')
    'ㄱㄴㄷ'

    if 1 is given as second argument, it removes double consonant
    >>> chosung(u'까나다', 1)
    'ㄱㄴㄷ'
    """
    ret = []
    for chara in txt:
        chr_id = ord(chara)
        # if char is not hangul syllable, append it self
        if (chr_id < BASE) or (chr_id > END):
            ret.append(chara)
            continue
            
        cho_idx = (chr_id - BASE) // CHO
        if mode == 0:
            ret.append(CHOLIST_D[cho_idx])
        else:
            ret.append(CHOLIST_S[cho_idx])

    return ''.join(ret)

def main():
   import doctest
   doctest.testmod()

if __name__=='__main__':
    main()