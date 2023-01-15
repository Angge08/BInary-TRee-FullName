class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
            if self.data == val:
                return True

            if val < self.data:
                if self.left:
                    return self.left.search(val)
                else:
                    return False

            if val > self.data:
                if self.right:
                    return self.right.search(val)
                else:
                    return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def build_tree(elements):
        print("Building tree with these elements:", elements)
        root = BinarySearchTreeNode(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])

        return root

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])

        return root

if __name__ == '__main__':
        fullname = ["A", "N", "G", "E", "L", "I", "C", "A", "C",
                    "D", "E", "L", "M", "E", "N", "D", "O"]
        name_tree = build_tree(fullname)
        print("****************************************************************************************************")
        print("My fullname:", fullname)
        print("****************************************************************************************************")
        print("Min:", name_tree.find_min())
        print("Max:", name_tree.find_max())
        print("****************************************************************************************************")
        print("In order traversal:", name_tree.in_order_traversal())
        print("Pre order traversal:", name_tree.pre_order_traversal())
        print("Post order traversal:", name_tree.post_order_traversal())
        print("****************************************************************************************************")
        name_tree.delete("G")
        print("After deleting the letter G", name_tree.in_order_traversal())
        name_tree.delete("O")
        print("After deleting the letter O", name_tree.in_order_traversal())
        print("****************************************************************************************************")
        print("Is letter A is in the list of my fullname? ", name_tree.search("A"))
        print("Is letter R is in the list of my fullname? ", name_tree.search("R"))
        print("****************************************************************************************************")

if __name__ == '__main__':
        number = [69, 45, 67, 90, 78, 80, 23, 67, 97, 45]
        number_tree = build_tree(number)
        print("****************************************************************************************************")
        print("My phone number:", number)
        print("****************************************************************************************************")
        print("Sum:", number_tree.calculate_sum())
        print("Min:", number_tree.find_min())
        print("Max:", number_tree.find_max())
        print("****************************************************************************************************")
        print("In order traversal:", number_tree.in_order_traversal())
        print("Pre order traversal:", number_tree.pre_order_traversal())
        print("Post order traversal:", number_tree.post_order_traversal())
        print("****************************************************************************************************")
        number_tree.delete(69)
        print("After deleting the number 69", number_tree.in_order_traversal())
        number_tree.delete(97)
        print("After deleting the number 97", number_tree.in_order_traversal())
        print("****************************************************************************************************")
        print("Is number 67 is in the list of my phone number?", number_tree.search(67))
        print("Is number 100 is in the list of my phone number?", number_tree.search(100))

