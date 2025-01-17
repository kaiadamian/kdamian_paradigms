def tree_to_text(tree, root_node):
    ''' convert tree represented by an adjacency list to a string containing the mathematical expression '''
    def _recursive_build(node):
        if not tree[node]:                      # if the node is an operand (leaf), return its number
            return node.split('_')[1]
        
        left = _recursive_build(tree[node][0])  # recursive call on left operand
        right = _recursive_build(tree[node][1]) # recursive call on right operand
        op = node.split('_')[1]                 # retrieve operator of node
        
        return f'{left}{op}{right}'             # build the expression
    
    return _recursive_build(root_node)


def main() -> None:
    # Test 1
    tree =  {"n1_+": ["n2_*","n3_3"], "n2_*":["n4_2","n5_7"], "n4_2":[],"n5_7":[],"n3_3":[]}
    root_node = "n1_+" 
    # Test 2
    tree2 ={'n1_+': ['n2_3', 'n3_*'], 'n3_*': ['n4_/', "n5_2"], 'n4_/': ["n6_10", "n7_5"], "n6_10": [], "n7_5": [], "n5_2": [], 'n2_3': []}
    root_node2 = "n1_+" 
    # print output
    print(f'Test 1: {tree_to_text(tree, root_node)}')
    print(f'Test 2: {tree_to_text(tree2, root_node2)}')
    

if __name__ == '__main__':
    main()