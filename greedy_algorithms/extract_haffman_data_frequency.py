
def extract_symbols(source):
    with open(source, "rt") as codes_file:
        number_of_codes = int(codes_file.readline())
        yield from (int(codes_file.readline()) for i in range(number_of_codes))