def findTargetSumWays( nums, S):
    index = len(nums) - 1
    curr_sum = 0
    
    def dp(nums, target, index, curr_sum):
        # Base Cases
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
        # Decisions
        positive = dp(nums, target, index-1, curr_sum + nums[index])
        negative = dp(nums, target, index-1, curr_sum )
        
        return positive + negative
    return dp(nums, S, index, curr_sum)
# print(findTargetSumWays([5,3,4,7],7))
def coinchange( nums, S):
    index = 0
    curr_sum = 0
    res = 99999999999
    def dp(nums, target, index, curr_sum,ans,res):
        # Base Cases

        if index < 0 or index > len(nums) -1:
            return 999999
        if curr_sum > target:
            return 999999999
        if  curr_sum == target:
            print(ans)
            return ans
        # Decisions
        ans+=1
        positive = dp(nums, target, index, curr_sum + nums[index],ans,res)
        ans-=1
        negative = dp(nums, target, index+1, curr_sum,ans,res)
        return min(positive , negative)
    return dp(nums, S, index, curr_sum,0,9999999)
# print(coinchange([1,2,3],5))

def partialsunsetsum( nums):
    TOTAL = sum(nums)
    if TOTAL % 2 != 0:
        return False
        
    memory = {}
    
    def dp(i, sum1):

        if i == len(nums):
            return (sum1 == TOTAL/2)
        
        if sum1 == TOTAL/2:
            return True

        if (i, sum1) in memory:
            return memory[(i, sum1)]

        memory[(i,sum1)] = dp(i+1, sum1+nums[i]) or dp(i+1, sum1)
        return memory[(i, sum1)]
    return dp(0,0)
print(partialsunsetsum([1,5,11,5]))
def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # def dfs(i, j,memo):
        #     key = str(i) + "" + str(j)
        #     if key in memo :
        #         memo[key]
        #     if i < 0 or i >= m or j < 0 or j >= n :
        #         return 999999
        #     if i == m-1 and j == n-1:
        #         return grid[i][j]
        #     memo[key] = grid[i][j] + min(dfs(i+1,j,memo),dfs(i,j+1,memo))
        #     return memo[key]
        # return dfs(0,0,{})
        for i in range(m):
            for j in range(n):
                if i !=0 and j ==0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif i == 0 and j != 0:
                    grid[i][j] = grid[i][j]+grid[i][j-1]
                elif i==0 and j ==0:
                    grid[i][j] = grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[m-1][n-1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        
        inorderIndex = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:inorderIndex], postorder[:inorderIndex])
        root.right = self.buildTree(inorder[inorderIndex+1:], postorder[inorderIndex:-1])
        
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            ind = nums.index(max(nums))
            root = TreeNode(nums[ind])
            root.left = self.constructMaximumBinaryTree(nums[:ind])
            root.right = self.constructMaximumBinaryTree(nums[ind+1:])
            return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node,seen):
            if not node :
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left,seen) or dfs(node.right,seen)
        return dfs(root,set())
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node,ans):
            if not node :
                return
            dfs(node.left,ans)
            ans.append(node.val)
            dfs(node.right,ans)
            return ans
        return dfs(root,[])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def currentsum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = max(0,self.currentsum(root.left))
            right = max(0,self.currentsum(root.right))
            #comparing for max
            self.max=max(self.max,root.val+left+right)
            #returning one side of node only as both sides can't form a single path to grandparent
            return root.val+max(right, left)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max=root.val
        self.currentsum(root)
        return self.max