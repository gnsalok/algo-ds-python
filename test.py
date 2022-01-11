ll = [(1,2), (2,5), (9,8)]
key = 9
foundKey = False


for i,v in enumerate(ll):
    rkey,rvalue = v
    iteration = i
    if(rkey == key):
        foundKey = True
        break

if(foundKey):
    print(i)
    ll[iteration] = (3,10)


print(ll)





   


    
    
    
