class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


def get_node_by_index(node, index):
    while index:
        node = node.next
        index = index - 1
    return node


def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index - 1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


node3 = Node("Прочитать новости", None)
node2 = Node("Умыться", node3)
node1 = Node("Позавтракать", node2)
node0 = Node("Проснуться", node1)
node, index, value = node0, 1, 'Выпить кофе'

