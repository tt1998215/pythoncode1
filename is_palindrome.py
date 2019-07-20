def is_palindrome(n):
    L=[]
    for i in str(n):
        L.append(i)
    L2=list(revers(L))
    for i in range(len(L)):
        if L[i]!=L2[i]:
            return 0
        return 1
#
# def revers(L):
#     L2=[]
#     for i in range(len(L)):
#         L2[i]=L[len(L)-1-i]
#     return L2


def revers(L):
    L1=[]
    for i in range(len(L)):
        L1.append(L[len(L)-1-i])
    return L1
# L=[1,2,3,4]
# L2=revers(L)
# print(L2)
output = filter(is_palindrome, range(1, 1000))
print(list(output))