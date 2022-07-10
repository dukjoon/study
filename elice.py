
def maxTwoDiff(nums):
    for i in nums:
        for j in nums:
            item = (nums[i] - nums[j])
            
    max(item)
            

def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
