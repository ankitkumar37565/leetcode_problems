
def largestRectangleArea( heights):
    n=len(heights)
    left=[0]*n
    right=[0]*n
    stack=[]
    # getting left element
    for i in range(n):
        if not stack:
            left[i]=0
        else:
            while stack and heights[stack[i]]>=heights[i]:
                stack.pop()
            left[i]=stack[-1]+1
            stack.append(i)
    stack=[]
    print(left)
    # getting right element
    for i in range(n-1,-1,-1):
        if not stack:
            right[i]=n-1
        else:
            while stack and heights[stack[i]]>=heights[i]:
                stack.pop()
            right[i]=stack[-1]-1 if stack else n-1
            stack.append(i)
    print(right)
    # calculating area
    maxArea=0
    for i in range(n):
        height=heights[i]
        width=right[i]-left[i]+1
        area=height*width
        maxArea=max(area,maxArea)
    print(maxArea)
    return maxArea
largestRectangleArea([2,1,5,6,2,3])