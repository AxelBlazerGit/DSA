#User function Template for python3
def insert(head, data):
    temp = Node(data)
    temp.npx = head
    return temp
    
def getList(head):
    ans = []
    curr = head
    while curr is not None:
        ans.append(curr.data)
        curr = curr.npx
    return ans
