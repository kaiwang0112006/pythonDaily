# -*- coding: utf-8 -*-

################################################
#
#  二叉树的后序遍历 (https://mp.weixin.qq.com/s?__biz=MzkxNDE0NjIyOA==&mid=2247483907&idx=1&sn=ba61980d39f17842b04261847a7ca0b7&chksm=c17394d8f6041dced3de6eef12521f812b3fede805105b2fbcdbf3d3dcece6704d840eb7449c&mpshare=1&scene=1&srcid=0229K6m4b49USrgOF5WfJe7K&sharer_shareinfo=bd74398035bf10049effd1d12127bbae&sharer_shareinfo_first=c48fc00d642133d38bcab327567ef0b5&exportkey=n_ChQIAhIQLkCSkO1eFg%2F53qDoCbLNQBKYAgIE97dBBAEAAAAAANpeBWYWFQIAAAAOpnltbLcz9gKNyK89dVj0Dixw55ytGDdU4TNkT1JUrA5j1c4hQ4iKZibMR49odakSAWofb%2Bj6czQUcFmu46oAAEmQ0fN3K9oEG2bTq5Yx%2FgWcSsXNWrB%2BG00ac66145DaiUfyFsZ%2BpBLjibiLFtgmdN1XuZ8Eferje16O37O9FBFmOzxVIEOYXF%2BlDP6tukJjPAzaYf6i3UA%2FE0ZmkPINH0gjW%2FPXwR%2Bp9SdkogqNur4B3kBY7%2B6Y2vAoKQnAduyktx3jxS8dsUbDwE3GFnC0%2FoycFegMMexchSEK%2FIOxcHigz1k%2BmVd5EpVkwiyuz1pArRs1x%2BncR9qM2DKotzP%2FTHw%3D&acctmode=0&pass_ticket=oRSw4%2B56HUn7CBuVIyjjNF2WeP7KLktDGSrte83K6pedFq1RWuFsINE1ADFvi9N2rtJpWwMlqNiaMaK4Q5muDg%3D%3D&wx_header=0#rd)
#
################################################

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 后续遍历函数
def postorder_traversal(node):
    if node is not None:
        # 遍历左子树
        postorder_traversal(node.left)
        # 遍历右子树
        postorder_traversal(node.right)
        # 访问根节点
        print(node.data, end=', ')

if __name__ == "__main__":
    # 构建之前给到的示例二叉树
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    # 后续遍历二叉树
    print("Postorder Traversal:", end=' ')
    postorder_traversal(root)