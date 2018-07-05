nums = input().split()
map(int, nums)

changed = True
while changed:
    changed = False
    for x in range(len(nums)-1):
        if nums[x] > nums[x+1]:
            temp = nums[x]
            nums[x] = nums[x+1]
            nums[x+1] = temp
            changed = True
            for num in nums:
                print(num, end=' ')
            print()

