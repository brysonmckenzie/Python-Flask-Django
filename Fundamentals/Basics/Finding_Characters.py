def Find_Char(strList,char):
    new_List = []
    for i in strList:
        if char in i:
            new_List.append(i)
    return new_List 

           
    
            

            






print Find_Char(['hello','world','my','name','is','Anna','house'],"o")


