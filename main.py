A = ["", ""]

def Initialize(maxLimit):
    for i in range(2, maxLimit+1): A.insert(i, 1)

def Sieve():
    for i in range(2, len(A)):
        if i <= maxLimit**(1/2):
            for x in range(2, len(A)):
                if x % i == 0 and x > i:
                    A[x] = 0

def Verify():
    print("\n")
    print("Tablica: ", A)
    print("\n")
    print("Indkesy i elementy tablicy: ")
    for x in range(len(A)):
        print("Indeks: ",x,"Element: ",A[x])


print("Podaj górny zakres zbioru [2,n], z którego wyznaczane mają być liczby pierwsze: ", end="")
maxLimit = int(input())
Initialize(maxLimit), Sieve(), Verify()





