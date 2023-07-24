# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def solution(root) -> bool:
    if root is None:
        return True

    brightest_lamp = root.value
    left_brightest = solution(root.left)
    right_brightest = solution(root.right)

    if left_brightest is not None:
        brightest_lamp = max(brightest_lamp, left_brightest)
    if right_brightest is not None:
        brightest_lamp = max(brightest_lamp, right_brightest)

    return brightest_lamp


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

if __name__ == '__main__':
    test()