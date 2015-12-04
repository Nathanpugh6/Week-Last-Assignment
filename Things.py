def moveTower (n, source, dest, temp):
    if n == 1:
        print("move disk from ", source, "to","dest"+".")
    else:
        moveTower (n-1, source, temp, dest)
        moveTower (1, source, dest, temp)
        moveTower (n-1, temp, dest, source)

def hanoi (n):
    moveTower (n, "A","B","C")

def main():
    d = eval(input("Enter a number of discs: "))
    hanoi(d)

if __name__ == "__main__":
    main()

def (gCd(x,y):
     print ("X= ", x, "Y= ", y)
     if y == 0: #base case here
         return x
     else:
         return (gCd(y,x%y)

def main():
    x = 252
    y = 105

    print ("GCD of", x, ",", y, "=", gCd(x,y))


if __name__ == "__main__":
    main()