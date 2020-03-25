class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # masking each row in reservedSeats
        d = collections.defaultdict(int)
        for (r, c) in reservedSeats:
            d[r] |= 1 << (c-1)
        
        ans = 2 * n
        # iterate each masked row and verify
        for r, binary in d.items():
            if binary | 513 == 513:
                continue
            elif binary | 543 == 543 or binary | 903 == 903 or binary | 993 == 993:
                ans -= 1
            else:
                ans -= 2
        return ans        
        
            
# How to make ith bit (from right) as 1?
# 1 << i-1
# e.g. 3rd bit as 0
# 1 << 2 will be binary '100' which is decimal 4

# How to verify ith bit (from right) of num is 0?
# e.g. 3rd bit from right
# num | int('0b1011', 2) == int('0b1011', 2)


# Mask for row can fit 2 four-person families
# int('0b1000000001', 2) == 513 

# Mask for row can fit 1 four-person families
# int('0b1000011111', 2) == 543
# int('0b1110000111', 2) == 903
# int('0b1111100001', 2) == 993
