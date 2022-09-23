class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        hashMap ={}
        for i in nums1:
            if i not in hashMap:
                hashMap[i]=1
            else:
                hashMap[i] = hashMap[i] + 1
        for j in nums2:
            if j in hashMap:
                answer.append(j)
                hashMap[j]=hashMap[j]-1
                if hashMap[j] == 0:
                    del hashMap[j]
        return answer