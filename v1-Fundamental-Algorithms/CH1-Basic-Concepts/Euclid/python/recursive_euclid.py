'''
Recursive implementation of Euclid's Algorithm. This version
avoids variable substitutions as specified in Exercise 3 of Section
1.1
'''
def euclid(m, n):
    if m < 1 or n < 0:
        return 0
    else:
        if n == 0:
            return m
        else:
            return euclid(n, m % n)

if __name__ == '__main__':
    print(euclid(27, 36))
    print(euclid(119, 544))
