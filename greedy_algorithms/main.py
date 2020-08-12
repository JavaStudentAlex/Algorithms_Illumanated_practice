from greedy_algorithms.extract_haffman_data_frequency import extract_symbols
from greedy_algorithms.building_haffman_coding_tree_by_haffman import build_haffman_tree


source_dir = "frequencies"
file_name = "haffman_codes_10.txt"

data = extract_symbols("{}/{}".format(source_dir, file_name))
haffman_tree = build_haffman_tree(data)
str_tree = haffman_tree.tree_to_str()
print(str_tree)