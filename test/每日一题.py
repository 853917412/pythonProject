
def p_1464(nums): #显示最大值下标
    nums1 = sorted(nums,reverse=True)
    if nums1[0] == nums1[1]:
        for i in range(len(nums)):
            if nums[i] == nums1[0]:
                print(str(i),end='')
    else:
        print(str(nums.index(nums1[0]))+str(nums.index((nums1[1]))))

def p_006(List, target):
    for i in List:
        for j in List:
            if i != j:
                if i + j == target:
                    print('[{},{}]'.format(List.index(i),List.index(j)))
                    return 0
                else:
                    pass
            else:
                pass