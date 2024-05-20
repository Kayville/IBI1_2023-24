# Define a duplicate function with two parameters
def duplicates(seq, target):
    count = 0
    start = 0
    seq = ‘ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA’ 
    target=‘GTGTGT’	and	‘GTCTGT’

# Within the loop, continuously search for the index of a specific field in the text to calculate the number of overlapping repetitions until the index no longer exists
    if start < len(seq):
        index = seq.find(target, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break
            return count
  print(count)

