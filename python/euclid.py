def euclid(m, n):
  while n:
    m, n = n, m % n
  return m

if __name__ == '__main__':
 print(euclid(27, 36))


