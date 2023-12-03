

def masters_theorem():
    print('T(n) = a*T(n/b) + O(n^k*log^p(n)')

    try:
        a = int(input("a= "))
        b = int(input("b= "))
        k = int(input("k= "))
        p = int(input("p= "))
    except ValueError:
        print('Wrong format')
        masters_theorem()
        return 0

    print(f'T(n) = {a}*T(n/{b}) + O(n^{k}*log^{p}(n)')

    if a >= 1 and b > 1 and k >= 0 \
            :
        if a > pow(b, k):
            print('Case 1')
            print(f'T(n) = O(n^(log({b},{a})')
        elif a == pow(b, k):
            print('Case 2')
            if p > -1:
                print(f'T(n) = O(n^(log({b},{a})*log^({p} + 1)n')
                print(f'T(n) = O(n^(log({b},{a})*log^{p + 1}(n)')
            if p == -1:
                print(f'T(n) = O(n^(log({b},{a})*log(log(n))')
            if p < -1:
                print(f'T(n) = O(n^(log({b},{a})')
        elif a < pow(b, k):
            print('Case 3')
            if p >= 0:
                print(f'T(n) = O(n^{k}*log^{p}(n)')
            elif p < 0:
                print(f'T(n) = O(n^{k}')
    else:
        print('Wrong format')



masters_theorem()