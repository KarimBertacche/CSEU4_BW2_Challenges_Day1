def containsDuplicate(nums):
    dupDict = dict()

    for num in nums:
        if num not in dupDict:
            dupDict[num] = 1
        else:
            return print(True)
    
    return print(False)