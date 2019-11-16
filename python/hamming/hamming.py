def distance(strand_a, strand_b):
    if not len(strand_a) == len(strand_b):
        raise ValueError("Cannot compare strands.\nStrands does not tally")
    diff = 0
    for i in range(len(strand_a)):
        if not strand_a[i] == strand_b[i]:
            diff += 1
    return diff