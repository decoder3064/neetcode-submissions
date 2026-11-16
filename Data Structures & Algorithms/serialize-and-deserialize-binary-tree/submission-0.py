# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoded = []
        def dfs(root):
            if not root:
                encoded.append("N")
                return 
            encoded.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print(encoded)
        return ','.join(encoded)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        iterate = data.split(',')
        self.index = 0

        def dfs():
            if iterate[self.index] == 'N':
                node = None 
                self.index+=1
                return 

            node = TreeNode(int(iterate[self.index]))
            self.index +=1 

            node.left = dfs()
            node.right = dfs()
            return node 
        return  dfs()

        






