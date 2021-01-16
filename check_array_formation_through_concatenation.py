def canFormArray(arr, pieces):
    total = len(arr)
    count = 0
    for piece in pieces:
        try:
            start = arr.index(piece[0])
        except:
            continue
        end = start + len(piece)
        if arr[start:end] == piece:
            piece_in_arr = True
        else:
            piece_in_arr = False
        if piece_in_arr == False:
            return False
        count += len(piece)
        if count == total:
            return True
    return False
print(canFormArray([1,3,5,7], [[2,4,6,8]]))