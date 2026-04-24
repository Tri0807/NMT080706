#cau 1
def SumDigit (n):
    if n == 0:
        return 0
    else:
        return n % 10 + SumDigit(n//10)
n = int (input("nhập một số nguyên dương: "))    
print("Tổng các chữ số của",n,"là:", SumDigit(n)) 

#cau 2
def gt(n):
    if n == 0:
        return 1
    else:
        return n *gt(n-1)
n = int (input("nhập một số nguyên dương:"))
print("Giai thừa của",n,"là:",gt(n))
#cau 3
def luy_thua(x,n):
    if n == 0:
        return 1
    else:
        return x * luy_thua(x,n-1)
    a = int(input("Nhập cơ số:"))
    b = int(input("Nhập số mũ:"))
    print(a,"^",b,"=",luy_thua(a,b))
 #cau 4
def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
a = int(input("Nhập số nguyên dương thứ nhất:"))
b = int(input("Nhâp số nguyên dương thứ hai"))
print("Ước chung lớn nhất của",a ,"và",b,"là:", gcd(a,b))        