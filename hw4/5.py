class Wordplay:
    def __init__(self,word):
        self.word= word
    
    def words_with_length(self):
        return['{}:{}'.format(w,len(w)) for w in b]
    
    def starts_with(self):
        return [w for w in b if w[0]=='s']

    def end_with(self):
        return [w for w in b if w[-1]=='s']
    
    def palindromes(self):
        return [w for w in b if w[:]==w[: : -1]]

    def only(self):
        return [w for w in b if 'l' in w]
    
    def avoids(self):
        return [w for w in b if 'l' not in w]

s = open('word.txt').read()
a = s.lower()
b = a.split()
c = Wordplay(b)

print('word with length: ', c.words_with_length())
print('Letter end with s: ', c.end_with())
print('Pallidromic letter: ', c.palindromes())
print('Word contain l: ' , c.only())
print('Word not contain l: ', c.avoids())