class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        max_area = 0
        while left<right:
            lowest_height=min(height[left],height[right])
            width = right - left
            area = lowest_height*width

            max_area = max(max_area,area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area


           
        