import math 

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627

def karatsuba (num1,num2):
    #Making the two inputs of the same length

    if num1<10 or num2<10:
        return num1*num2
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) != len(num2):
        if len(num1) > len (num2):
            diff_len = len(num1) - len(num2)
            num2 = diff_len*"0" + num2
        if len(num1) < len(num2):
            diff_len = len(num2) - len(num1)
            num1 = diff_len*"0" + num1
    #Now getting into the recursive part to solve the problem 

    n = len(num1)
    j = n//2 
    
    a = num1[:j]
    b = num1[j:]
    c = num2[:j]
    d = num2[j:]

    ac = karatsuba (int(a),int(c))
    bd = karatsuba (int(b),int(d))
    a_b_c_d= karatsuba (int(a)+int(b),int(c)+int(d))
    diff = a_b_c_d - bd - ac 
    ans = ac*10**(2*(n-j)) + diff*10**(n-j) + bd # the n-j nuance is key: for eg. 12340 = 12*10^3 + 340 OR 123*10^2 + 40;
    # in the first instance j = 2 and n-j = 3; in the second instance j = 3 and n-j = 2. In my code we have taken the former j. 
    return ans

test_case = karatsuba (a,b)
print (test_case)
