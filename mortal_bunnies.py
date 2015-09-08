def num_rabbits(months, lifespan):
	if months == 0: return 1
	if months == 1: return 1
	if months == 2: return 2
	answer = num_rabbits(months-1, lifespan) + num_rabbits(months-2, lifespan) - num_rabbits(months-3, lifespan)
	return answer

print num_rabbits(4, 3)
