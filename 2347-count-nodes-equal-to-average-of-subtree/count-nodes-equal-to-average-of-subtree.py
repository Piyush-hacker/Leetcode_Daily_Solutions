class Solution:
    def avgOfNode(self, node: TreeNode, result: list):
        if node == None:
            return [0, 0]
        leftNodes: list = self.avgOfNode(node.left, result)
        rightNodes: list = self.avgOfNode(node.right, result)
        sumOfNodes: int = leftNodes[0] + rightNodes[0] + node.val
        cntOfNodes: int = leftNodes[1] + rightNodes[1] + 1
        if sumOfNodes // cntOfNodes == node.val:
            result[0] += 1
        return [sumOfNodes, cntOfNodes]
    
    def averageOfSubtree(self, root: TreeNode) -> int:
        result: list = [0]
        self.avgOfNode(root, result)
        return result[0]