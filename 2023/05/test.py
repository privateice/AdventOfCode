def find_overlapping_ranges(start, end, ranges):
    overlaps = []
    non_overlapping_parts = []

    for s, e in ranges:
        # Check for complete overlap
        if s <= start and e >= end:
            overlaps.append((s, e))
        # Check for partial overlap
        elif e >= start and s <= end:
            overlaps.append((max(s, start), min(e, end)))
    
    # Identify non-overlapping parts
    if overlaps:
        non_overlapping_parts.append((start, overlaps[0][0]))
        for i in range(1, len(overlaps)):
            non_overlapping_parts.append((overlaps[i-1][1], overlaps[i][0]))
        non_overlapping_parts.append((overlaps[-1][1], end))
    else:
        non_overlapping_parts.append((start, end))

    return overlaps, non_overlapping_parts

# Example usage:
A = 1000000
B = 5000000
start = A
end = A + B

ranges = [(2000000, 3000000), (4000000, 6000000), (7000000, 8000000)]

overlaps, non_overlapping_parts = find_overlapping_ranges(start, end, ranges)

print("Overlapping ranges:", overlaps)
print("Non-overlapping parts:", non_overlapping_parts)
