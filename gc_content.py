gc_counts = {}

with open('rosalind_gc.txt') as input:
	best_id = ""
	best_ratio = 0
	current_gc_count = 0
	current_base_count = 0
	current_id = ""
	for line in input:
		line = line.strip()

		if line.startswith(">"):
			if current_id != "":
				gc_ratio = (float(current_gc_count) / float(current_base_count)) * 100

				if gc_ratio > best_ratio:
					best_id = current_id
					best_ratio = gc_ratio

			current_gc_count = 0
			current_base_count = 0
			current_id = line[1:]
		else:
			for c in line:
				if c == 'G' or c == 'C': current_gc_count += 1
				current_base_count += 1

	gc_ratio = (float(current_gc_count) / float(current_base_count)) * 100

	if gc_ratio > best_ratio:
		best_id = current_id
		best_ratio = gc_ratio

print best_id
print best_ratio
