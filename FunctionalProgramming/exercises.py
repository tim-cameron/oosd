__author__ = 'camertp1'

# exercise 1 :
print reduce(lambda x, y: x * y,1 + range(1,6))



# exercise 2 :
def findreplace(s, c): return filter(lambda x: x != c, s)
findreplace("hello world", "o")

# exercise 3 :
def occurance(s, c): return map (lambda x: x == c, s).count(True);
occurance("hello world", "o")

# exercise 4 :
def words (s, c): return filter (lambda x: x.startswith(c), s.split(' '))
words ("hello world, how are you", "h")

# exercise 5 :
def toupper (s, c): return filter (lambda x: c.upper() if x == c else x, s)
# ???????????????????????????????????
