class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


def solution(node):
    while node:
        print(node.value)
        node = node.next


node3 = Node("Прочитать новости", None)
node2 = Node("Умыться", node3)
node1 = Node("Позавтракать", node2)
node0 = Node("Проснуться", node1)
solution(node0)