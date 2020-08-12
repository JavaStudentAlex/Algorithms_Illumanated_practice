class Heap:

    def __init__(self, key_element_pairs_arr, operation=min):
        self.__elements = list(key_element_pairs_arr)
        self.__parent_child_cond = operation
        self.__build_heap()

    # should work for O(n)
    def __build_heap(self):
        for node_with_children in reversed(range(len(self.__elements) // 2)):
            self.__bubble_down(node_with_children)

    def __bubble_down(self, parent_index=0):
        left_child = parent_index * 2 + 1
        right_child = parent_index * 2 + 2
        children = [left_child, right_child]

        for child in children:
            if self.__process_heap_property(parent_index, child):
                self.__bubble_down(child)

    def __process_heap_property(self, parent_index, child_index):
        try:
            if not self.__is_heap_property(parent_index, child_index):
                self.__swap(parent_index, child_index)
        except IndexError:
            return False
        return True

    def __is_heap_property(self, parent_index, child_index):
        # no elements to assert heap properties
        if parent_index < 0 or child_index >= len(self.__elements):
            raise IndexError

        parent_val = self.__elements[parent_index][0]
        child_val = self.__elements[child_index][0]
        return parent_val == self.__parent_child_cond(parent_val, child_val)

    def __swap(self, index1, index2):
        self.__elements[index1], self.__elements[index2] = self.__elements[index2], self.__elements[index1]

    # must work for O(log(n))
    def pop_min(self):
        if len(self.__elements) == 0:
            return None

        min_val_pair = self.__elements[0]
        self.__swap(0, -1)
        del self.__elements[-1]
        self.__bubble_down()

        return min_val_pair

    # must work for log(n)
    def insert(self, new_element):
        new_index = len(self.__elements)
        self.__elements.append(new_element)
        self.__bubble_up(new_index)

    def __bubble_up(self, child_index):
        parent = (child_index - 1) // 2
        if self.__process_heap_property(parent, child_index):
            self.__bubble_up(parent)

    def get_size(self):
        return len(self.__elements)
