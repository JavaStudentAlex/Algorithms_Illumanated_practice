
class HaffmanTree:

    def __init__(self, left, right, frequency=None):
        self.left = left
        self.right = right
        self.frequency = frequency if frequency is not None \
            else left.get_overall_frequency() + right.get_overall_frequency()

    def get_overall_frequency(self):
        return self.frequency

    def tree_to_str(self, node_code="", node_level=0):

        def node_to_str():
            return "{left_padding}{element}\n".format(left_padding=" \t" * node_level, element=node_code)

        def branch_to_str(next_branch, code):
            return next_branch.tree_to_str(code, node_level+1)

        if self.left is None and self.right is None:
            return node_to_str()
        else:
            result_str = branch_to_str(self.left, node_code+"0")
            result_str += "root\n" if node_code == "" else node_to_str()
            result_str += branch_to_str(self.right, node_code+"1")
            return result_str
