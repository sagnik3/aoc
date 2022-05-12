function ingest(path)
	inp = open(path) do f 
		readsplit(x) = split(readchomp(x),",")
		[parse(Int,s) for s in readsplit(f)]

	# Instead of reporting back the inp individually , return a Vector 
		# of length 9 where each index represents the number of inp of age `idx-1`
	# (since Julia is 1 indexed)
	groups = zeros(Int64,9)
	for f in inp
		groups[f+1] += 1 
	end 

	return groups
end 