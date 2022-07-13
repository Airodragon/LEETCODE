import itertools
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [[root,1]]
        temp = []
        while queue:
            pop_element = queue.pop()
            temp.append([pop_element[0].val,pop_element[1]])
            if pop_element[0].left:
                queue.insert(0,[pop_element[0].left,pop_element[1]+1])
            if pop_element[0].right:
                queue.insert(0,[pop_element[0].right,pop_element[1]+1])
        ans = [[x[0] for x in g] for k, g in itertools.groupby(temp, lambda x: x[1])]
        return ans