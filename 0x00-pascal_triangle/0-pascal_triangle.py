def pascal_triangle(n):
    """Returns a list of lists representing Pascal’s triangle of n."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]
            row = [1]  # Start with 1

            # Fill in the middle values using list comprehension
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])

            row.append(1)  # End with 1
            triangle.append(row)

    return triangle
