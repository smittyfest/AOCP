'''
notes: this solution will work no matter which order the arguments are given.

If we have m = 36 and n = 27, 36 % 27 is equal to 9, so we would next have
m = 27 and n = 9, 27 % 9 = 0, so m becomes 9, n becomes 0, and we get 9 as our
solution.

If we have m = 27 and n = 36, 27 % 36 is equal to 27, m becomes 36, n becomes 27, and 
we proceed as above.

'''
def euclid(m, n):
  if m < 1 or n < 1:
    print 'm and n must both be positive'
  else:
    while n:
      m, n = n, m % n
    return m

if __name__ == '__main__':
 print(euclid(27, 36))
 print(euclid(119, 544))


