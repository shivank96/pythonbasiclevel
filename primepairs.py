import collections
def primepairs():
    n=int(input())
    i=2
    k=0
    le=0
    li=[]
    while i<=n:
        count=0
        j=1
        while j<=i:
            if i%j==0:
                count=count+1
            j=j+1
        if count==2:
            li.append(i)
            le=le+1
        i=i+1
    l=0
    # pairs = []
    # pair = []
    if n%2==0:
        response = int(n/2)
    else:
        response=int(n/2)+1
    for l in range(len(li)):
        m=1
        for m in range(len(li)):
            res=li[l]+li[m]
            if res== n and li[l]<=response:
                print(li[l],"+",li[m],"=",n)
                # pair.append(li[l])
                # pair.append(li[m])
                # pairs.append(pair)
            m=m+1
        l=l+1
    # temp = collections.Counter(frozenset(ele) for ele in pairs)
    # ans = [temp[frozenset(ele)]==1 for ele in pairs]
    # if len(ans)%2==0:
    #     response = int(len(ans)/2)
    # else:
    #     response = int((len(ans)/2)+1)
    #
    # for x in range(response):
    #     print(ans[x])
    print(li)
primepairs()