from math import log10
def karatsuba(a,b): #positive numbers only
    if a == 0 or b == 0:
        return 0
    elif 0 < a < 10 and 0 < b < 10:
        return a*b
    else:
        m = max(int(log10(a))+1,int(log10(b))+1)
        m = m//2
        const = 10**m 
        a2 = a%const
        a1 = a//const
        b2 = b%const
        b1 = b//const
        
        step1 = karatsuba(a1,b1)
        step2 = karatsuba(a2,b2)
        step3 = karatsuba((a1+a2), (b1+b2))
        step4 = step3 - step2 - step1
        return step1*10**(m*2)+step2+step4*10**(m)