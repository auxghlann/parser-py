from typing import List, Any, Dict

# =============================================================================
# AST Node Class
# =============================================================================

class ASTNode:
    """
    Base class for all nodes in the Abstract Syntax Tree (AST).
    Each node represents a construct in the programming language, such as
    an expression, a statement, or a declaration.
    """
    def __init__(self, node_type: str):
        """
        Initializes an ASTNode with its type.

        Args:
            node_type (str): The type of the AST node (e.g., 'Program',
                'Expression', 'Statement').
        """
        self.node_type = node_type
        self.children: List[ASTNode] = []  # List of child nodes
        self.value: Any = None #stores the value of the node
        self.data_type: str = None # Store the data type of a node, if applicable
        self.scope: Dict[str, str] = {} # Store the scope of the node

    def add_child(self, child: 'ASTNode'):
        """
        Adds a child node to this node.

        Args:
            child (ASTNode): The child node to add.
        """
        self.children.append(child)

    def __repr__(self):
        """
         Returns a string representation of the AST node.  This is useful for
         debugging and visualizing the tree structure.  It recursively
         displays the node type and its children.
        """
        return f"{self.node_type}(value={self.value}, type={self.data_type}, children={self.children})"


    def pretty_print(self, indent=0):
        """
        Recursively pretty prints the AST in a readable format.

        Args:
            indent (int): The current indentation level.
        """
        indent_str = "  " * indent
        print(f"{indent_str}{self.node_type}(value={self.value}, type={self.data_type})")
        for child in self.children:
            child.pretty_print(indent + 1)
