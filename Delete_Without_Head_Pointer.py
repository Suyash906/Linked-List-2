def deleteNode(curr_node):
    #code here
    next_node = curr_node.next
    
    curr_node.data = next_node.data
    
    curr_node.next = next_node.next
