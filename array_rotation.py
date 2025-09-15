def rotate_array(array, d):
    n = len(array)
    if d < 0 or d >= n:
        return "invalid rotation Value"
    rotated_arr=[]*n
    for i in range(n):
        rotated_arr.append(array[(i + d) % n])
    return rotated_arr


arr = [1, 2, 3, 4, 5]
d=2  # Number of positions to rotate
rotated_array = rotate_array(arr, d)
print("The array after rotating by", d, "positions is:", rotated_array)