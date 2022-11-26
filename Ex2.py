text=input()

def find_longest(txt):
    longest_word=max(txt.split(),key=len)
    print(longest_word)
find_longest(text)