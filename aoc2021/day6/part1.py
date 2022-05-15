def main():
	with open('input.txt') as f:
		p=f.read().split(',')

	p=[int(i) for i in p]
	days={}
	total_days=81
	curr_data = p.copy()

	for day in range(1,total_days):
		temp_data = []
		new_fish = []
		for d in curr_data:
			if d==0:
				new_fish.append(8)
				d=6
			else:
				d-=1
			temp_data.append(d)
		temp_data.extend(new_fish)
		curr_data = temp_data
	print(f"Total fish: {len(curr_data)}")




main()