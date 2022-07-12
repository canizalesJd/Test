# print the whole grid by each row
def print_game(game):
    for row in game:
        print("  ".join(row))


# loop through each row and check for space to insert a word with certain length horizontally
def get_rows_and_index(game, length):
    res = {}
    ngrid = len(game)
    for nrow in range(ngrid):
        row = game[nrow]
        index_set = set()
        start = 0
        count = 0
        for i in row:
            if i == "-":
                count += 1
                if count >= length:
                    # insert the start index as there is enough space to insert
                    index_set.add(start + count - length)
            else:
                start += (count + 1)
                count = 0
        if index_set:
            res[nrow] = list(index_set)
    return res


# loop through each column and check for space to insert a word with certain length vertically
def get_cols_and_index(game, length):
    res = {}
    ngrid = len(game)
    for ncol in range(ngrid):
        index_set = set()
        start = 0
        count = 0
        for nrow in range(ngrid):
            if game[nrow][ncol] == "-":
                count += 1
                if count >= length:
                    index_set.add(start + count - length)
            else:
                start += (count + 1)
                count = 0
        if index_set:
            res[ncol] = index_set
    return res