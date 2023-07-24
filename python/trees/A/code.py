# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def solution(root) -> int:
    if root is None:
        return None

    brightest_lamp = root.value
    left_brightest = solution(root.left)
    right_brightest = solution(root.right)

    if left_brightest is not None:
        brightest_lamp = max(brightest_lamp, left_brightest)
    if right_brightest is not None:
        brightest_lamp = max(brightest_lamp, right_brightest)

    return brightest_lamp


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3

if __name__ == '__main__':
    test()

"""
Гоша повесил на стену гирлянду в виде бинарного дерева, в узлах которого 
находятся лампочки. У каждой лампочки есть своя яркость. Уровень яркости 
лампочки соответствует числу, расположенному в узле дерева. Помогите Гоше 
найти самую яркую лампочку в гирлянде, то есть такую, у которой яркость наибольшая.
"""