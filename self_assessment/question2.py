def text_to_tree(expression: str) -> list:
    ''' define helper functions '''
    def _precedence(op) -> int:
        ''' determine precedence for order of operations '''
        if op == '-' or op == '+':
            return 1
        elif op == '*' or op == '/':
            return 2
    
    def _node_create(op, right, left):
        ''' create a dictionary defining the operation and left and right child operands of each node '''
        return {'op': op, 'right': right, 'left': left}
    
    def _output_generate(root, output):
        ''' use BFS to traverse and generate output in specified order '''
        if not root:
            return
        
        queue = [root]                          # initialize queue and visited set

        while queue:                            # while there are nodes left in the queue
            node = queue.pop(0)                 # pop node from the left side (FIFO order)
            if node:
                if node['left']:
                    output.append(f'"{node['op']}" -> "{node['left']['op']}" // left')
                    queue.append(node['left'])  # add left child to queue
                if node['right']:
                    output.append(f'"{node['op']}" -> "{node['right']['op']}" // right')
                    queue.append(node['right']) # add right child to queue
    
    ''' create tree '''
    operators = []
    result = []
    output = []
    ops = ['+', '-', '*', '/']
    i = 0

    while i < len(expression):
        if expression[i] not in ops:                                                    # if char is an operand
            num = ''
            while i < len(expression) and expression[i] not in ops:                     # be sure to retrieve entire operand
                num += expression[i]
                i += 1
            result.append({'op': num, 'left': None, 'right': None})                     # append the operand to result list
            continue
        while operators and _precedence(operators[-1]) >= _precedence(expression[i]):   # if there is something in the stack of higher precedence than the current operator, pop it  
            op = operators.pop()
            right = result.pop()
            left = result.pop()
            result.append(_node_create(op, right, left))                                # append node to result list
        operators.append(expression[i])
        i += 1
    
    while operators:                                                                    # pop the remaining operators from the operators stack
        op = operators.pop()
        right = result.pop()
        left = result.pop()
        result.append(_node_create(op, right, left))                                    # append node to result list

    root = result.pop()

    _output_generate(root, output)

    return output

def print_output(output: list) -> None:
    for line in output:
        print(line)

if __name__ == "__main__":
    expression = "2*7+3"  # Test 1
    output = text_to_tree(expression)
    print_output(output)