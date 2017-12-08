# coding:utf-8
class TreeNode():
    def __init__(self,value,left_child=None,right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


# 非递归实现
class Tree():
    def __init__(self,root):
        self.root = root


    def preOrder(self):
        if not self.root:
            return
        node = self.root
        stackNode = []
        stackNode.append(node)

        while(len(stackNode)>0):
            node = stackNode.pop()
            print(node.value)
            if node.right_child:
                stackNode.append(node.right_child)
            if node.left_child:
                stackNode.append(node.left_child)

    def inOrder(self):
        if not self.root:
            return

        stackNode = []
        node = self.root
        while stackNode or node:
            while node:
                stackNode.append(node)
                node = node.left_child
            node = stackNode.pop()
            print(node.value)
            node = node.right_child

    def postOrder(self):
        if not self.root:
            return

        stackNode = []
        node = self.root
        markNode = None
        while stackNode or node:
            while node:
                stackNode.append(node)
                node = node.left_child
            node = stackNode.pop()

            if not node.right_child or node.right_child==markNode:  #没有右孩子或已被输出
                print(node.value)
                markNode = node
                node = None
            else:
                stackNode.append(node)   #如果有右孩子，需要重新push进去，先输出右孩子
                node = node.right_child

    def calculateNumberOfNodes(self,root):
        num = 0
        if not root:
            return 0
        else:
            num = 1+self.calculateNumberOfNodes(root.left_child)+self.calculateNumberOfNodes(root.right_child)
        return num

    def traversalByLayer(self,root):
        num = self.calculateNumberOfNodes(root)
        stackNodes = []
        stackNodes.append(root)
        for i in range(num):
            node = stackNodes[i]
            print(node.value)
            if node.left_child:
                stackNodes.append(node.left_child)
            if node.right_child:
                stackNodes.append(node.right_child)

node_9 = TreeNode(9)
node_7 = TreeNode(7)
node_4 = TreeNode(4,node_9,node_7)
node_10 = TreeNode(10)
node_2 = TreeNode(2,node_4,node_10)
node_8 = TreeNode(8)
node_6 = TreeNode(6,node_8)
node_5 = TreeNode(5)
node_3 = TreeNode(3,node_5,node_6)
root = TreeNode(1,node_2,node_3)

tree = Tree(root)
print("PreOrder:")
tree.preOrder()
print("InOrder:")
tree.inOrder()
print("PostOrder:")
tree.postOrder()
print("TraversalByLayer:")
tree.traversalByLayer(tree.root)
"""
PreOrder:
1 2 4 9 7 10 3 5 6 8
InOrder:
9 4 7 2 10 1 5 3 8 6
PostOrder:
9 7 4 10 2 5 8 6 3 1
TraversalByLayer:
1 2 3 4 10 5 6 9 7 8
"""

#递归实现

class Tree_recursive():
    def __init__(self,root):
        self.root = root

    def preOrder(self,root):
        if not root:
            return
        print(root.value)
        self.preOrder(root.left_child)
        self.preOrder(root.right_child)

    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left_child)
        print(root.value)
        self.inOrder(root.right_child)

    def postOrder(self,root):
        if not root:
            return
        self.postOrder(root.left_child)
        self.postOrder(root.right_child)
        print(root.value)


tree = Tree_recursive(root)
print("PreOrder:")
tree.preOrder(tree.root)
print("InOrder:")
tree.inOrder(tree.root)
print("PostOrder:")
tree.postOrder(tree.root)
"""
PreOrder:
1 2 4 9 7 10 3 5 6 8
InOrder:
9 4 7 2 10 1 5 3 8 6
PostOrder:
9 7 4 10 2 5 8 6 3 1
"""






























