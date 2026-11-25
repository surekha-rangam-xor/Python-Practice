def list_stats(nums):
    result={
        "min":min(nums) ,
        "max":max(nums),
        "total":sum(nums),
        "average":sum(nums)/len(nums),
        "ascending":sorted(nums),
        "descending":sorted(nums,reverse=True),
        "every second":nums[0::2]

    }

    print("min :",result["min"])
    print("max :",result["max"])
    print("total :",result["total"])
    print(f"average :{result["average"]:.2f}")
    print("ascending :",result["ascending"])
    print("descending :",result["descending"])
    print("every second :",result["every second"])
    return result


Result=list_stats([14, 3, 9, 27, 8, 21, 5, 18])
print(Result)

