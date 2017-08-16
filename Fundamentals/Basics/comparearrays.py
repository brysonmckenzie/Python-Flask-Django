def CompareArrays(arr1,arr2):

    if len(arr1) != len (arr2):
        return False
    elif len(arr1) == len (arr2):
        for i in arr1:
            if arr1 != arr2:
                print arr1,arr2
                return False
            else:
                return True

   






    