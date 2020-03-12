class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
    

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


'''
        1
       / \
      2   3
     / \   
    4   5
'''

'''
Tree Traversal :
1. PreOrder Traversal       - Root > Left Subtree > Right Subtree 
2. InOrder Traversal        - Left Subtree > Root > Right Subtree
3. PostOrder Traversal      - Left Subtree > Right Subtree > Root 
4. Level Order Traversal    - 
'''

def preOrderTraversal(n):
    if(n!=None):
        print(n.val)
        preOrderTraversal(n.left)
        preOrderTraversal(n.right)

def inOrderTraversal(n):
    if(n!=None):
        preOrderTraversal(n.left)
        print(n.val)
        preOrderTraversal(n.right)

def postOrderTraversal(n):
    if(n!=None):
        preOrderTraversal(n.left)
        preOrderTraversal(n.right)
        print(n.val)

def leveOrderTraversal(n):
    if n == None:
        return
    queue = []
    queue.append(n)
    while(len(queue) > 0):
        print(queue[0].val, end=" ")
        node = queue.pop(0)

        if node.left != None:
            queue.append(node.left)
        
        if node.right != None:
            queue.append(node.right)
    print()

def searchForAValue(value, root):
    if root == None:
        return "Error Message"
    
    queue = []
    queue.append(root)
    node = None
    while(len(queue)>0):
        node = queue.pop(0)
        if node.val == value:
            return "Found Successfuly"
        if node.left != None:
            queue.append(node.left)
        
        if node.right != None:
            queue.append(node.right)
    return "Not Found"

def insert(value, root):
    if root == None:
        root = Node(value)
    
    queue = []
    queue.append(root)
    node = None
    while (len(queue)>0):
        node = queue.pop(0)

        if node.left == None:
            node.left = Node(value)
            break
        else:
            queue.append(node.left)
        
        if node.right == Node:
            node.right = Node(value)
            break
        else:
            queue.append(node.right)
'''
def deleteDeepestNode(d_node, root):
    queue = []
    queue.append(root)
    node = None
    while (len(queue)>0):
        temp = queue.pop()
        if temp is d_node:
            temp = None
            return
        if temp.right != None:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)
        if temp.left != None:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                queue.append(temp.left)

def delete(key, root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.val == key:
            return None
        else:
            return root
    key_node = None
    queue = []
    queue.append(root)
    while(len(queue)): 
        temp = queue.pop(0) 
        if temp.val == key: 
            key_node = temp 
        if temp.left: 
            queue.append(temp.left) 
        if temp.right: 
            queue.append(temp.right) 
    if key_node :  
        x = temp.val 
        deleteDeepestNode(root,temp) 
        key_node.val = x 
    return root         
  '''

# function to delete the given deepest node (d_node) in binary tree  
def deleteDeepest(root,d_node): 
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp is d_node: 
            temp = None
            return
        if temp.right: 
            if temp.right is d_node: 
                temp.right = None
                return
            else: 
                q.append(temp.right) 
        if temp.left: 
            if temp.left is d_node: 
                temp.left = None
                return
            else: 
                q.append(temp.left) 
   
# function to delete element in binary tree  
def deletion(root, key): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.key == key :  
            return None
        else : 
            return root 
    key_node = None
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp.val == key: 
            key_node = temp 
        if temp.left: 
            q.append(temp.left) 
        if temp.right: 
            q.append(temp.right) 
    if key_node :  
        x = temp.val 
        deleteDeepest(root,temp) 
        key_node.val = x 
    return root      

leveOrderTraversal(root)
insert(6, root)
leveOrderTraversal(root)
deletion(root, 4)
leveOrderTraversal(root)
