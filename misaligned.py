def get_color_code(row_index, col_index):
    return row_index * 5 + col_index + 1


def longest_item_length(values):
    return max(len(str(x)) for x in values)


def display_color_table():
    primary_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    secondary_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

    max_primary_len = longest_item_length(primary_colors)
    max_secondary_len = longest_item_length(secondary_colors)

    top_line = "| -- | " + "-" * max_primary_len + " | " + "-" * max_secondary_len + " |"
    print(top_line)

    total_entries = 0
    for r, prim in enumerate(primary_colors):
        for c, sec in enumerate(secondary_colors):
            total_entries += 1
            code = get_color_code(r, c)
            print(f"| {code:<2} | {prim:<{max_primary_len}} | {sec:<{max_secondary_len}} |")
        print(top_line)

    return total_entries
