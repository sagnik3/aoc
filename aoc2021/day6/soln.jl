struct School 
	agegroups::Vector{Int64}
end 

function Base.Iterate(iter::School)
	groups = copy(iter.agegroups)
	(sum(groups),groups)
end 


function Base.Iterate(iter::School,groups::vector{Int64})
	groups = circshift(groups,-1)
	groups[7] += groups[9]
	(sum(groups),groups)
end 


function Base.getindex(school::School,i::Int)
	for(generation,groups) in enumerate(school)
		generation > i && return groups 
	end 
end


function sole(input,days)
	school = School(days)
	return sum(school[days])
end 
