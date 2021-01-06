def sum_count_reverse(n):
    counter=0
    sum=0
    rev=0
    while n>0:
        rem=n%10
        sum+=rem
        rev=rev*10+rem
        n=n//10
        counter+=1
    print("count is ",counter)
    print("sum of all digits is ",sum)
    print("reverse of number is ", rev)
sum_count_reverse(245)
