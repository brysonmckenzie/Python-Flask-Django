def is_mixedINT(arr):

    for index in arr:
        if isinstance(index,int) == True:
            return "not mixedi"
        # elif isinstance(index,int) != True:
        #     return "mixedi"
        elif isinstance(index,(str,int)) != True:
            return "not mixeds"
        # elif isinstance(index,str ) != True:
        #     return "mixeds"
        elif isinstance(index,float) == True:
            return "not mixedfs"
        else:
            return "mixed"
              

print is_mixedINT([5,"he"])


            
            

    







