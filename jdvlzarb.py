print('welcome jadval zarb app ')
def jadvalzarb():
    n = int(input("enter row num :"))
    m = int(input("enter col num :"))
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                print('x', end='\t')
            elif i == 1:
                print(j-1, end='\t')
            elif j == 1:
                print(i-1, end='\t')
            else:
                print((i-1)*(j-1), end='\t')
        print()

jadvalzarb()