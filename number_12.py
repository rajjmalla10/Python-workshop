dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}



nums =  dict(list(dic1.items()) + list(dic2.items())+ list(dic3.items()))
print(nums)

nums.update({7:70})
print(nums)

nums[3] = 80 
print(nums)

nums.pop(3)
print(nums)

sums = (nums.values())
print(sums)

p =1
for num in nums.values():
    if isinstance(num, (int,float)):
        p *= num
print(p)        
        
        
max_v = max(nums.values())
min_v = min(nums.values())
print(f"{max_v}, {min_v}")