# 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时
# ，返回 true；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#  
# 
#  示例 2： 
# 
#  输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= pushed.length == popped.length <= 1000 
#  0 <= pushed[i], popped[i] < 1000 
#  pushed 是 popped 的排列。 
#  
#  Related Topics 栈


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        index, stack = 0, []
        for p in pushed:
            stack.append(p)
            # 依次比较stack的最后一个元素和popped第一个元素是否相等
            # 相等就弹出 同时popped索引加一
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return not stack


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    pushed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    popped = [4, 3, 2, 1, 0, 9, 8, 7, 6, 5]
    print(s.validateStackSequences(pushed, popped))
