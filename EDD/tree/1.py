from graphviz import Digraph

class Node():
    def __init__(self, value: int) -> None:
        self.value = value
        self.left : None | Node = None
        self.right : None | Node = None
    
    def add(self, value) -> None:
        if self.value < value:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.add(value)
        elif self.value > value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.add(value)

    def search(self, value):
        if self.value == value:
            print(self)
        elif self.value < value:
            if self.right == None:
                print("Valor não encontrado!")
            else:
                self.right.search(value)
        elif self.value > value:
            if self.left == None:
                print("Valor não encontrado!")
            else:
                self.left.search(value)

    def __str__(self) -> str:
        vRight = self.right.value if (self.right != None) else None
        vLeft = self.left.value if (self.left != None) else None
        
        return f"""
        self.value: {self.value}
        self.right: {vRight}
        self.left: {vLeft}
        """

def draw_tree(root: Node) -> Digraph:
    dot = Digraph()
    
    def add_nodes_edges(node: Node):
        if node is None:
            return
        
        dot.node(str(id(node)), str(node.value))
        
        if node.left:
            dot.edge(str(id(node)), str(id(node.left)), label="L")
            add_nodes_edges(node.left)
        if node.right:
            dot.edge(str(id(node)), str(id(node.right)), label="R")
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    return dot


root = Node(50)
root.add(74)
root.add(28)
root.add(35)
root.add(42)
root.add(71)
root.add(98)
root.add(65)
root.add(11)
root.add(5)
root.add(14)
root.add(88)
root.add(99)
root.add(7)
root.add(10)
root.add(0)
root.add(21)
root.add(41)
root.add(77)

dot = draw_tree(root)
dot.render('binary_tree', view=True, format='png')