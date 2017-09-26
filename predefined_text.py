def manhattan_distance(in_begin_coor, in_end_coor):
	return abs(in_begin_coor[0]-in_end_coor[0])+abs(in_begin_coor[1]-in_end_coor[1])

dimension=80
grid_file=open("grid.txt")

square_map=grid_file.readlines()
for i in range(len(square_map)):
	square_map[i]=list(square_map[i].strip())
	for j in range(len(square_map[i])):
		square_map[i][j]=square_map[i][j]=='1'



start_coor=(0,0)
end_coor=(79,79)

open_list={start_coor:[None,0,manhattan_distance(start_coor,end_coor)]}
closed_list={}
while end_coor not in closed_list:
	lowest_f_cost=None
	recommended_coor=None
	for coor in open_list:
		if lowest_f_cost==None:
			lowest_f_cost=open_list[coor][1]+open_list[coor][2]
			recommended_coor=coor
		elif open_list[coor][1]+open_list[coor][2]<lowest_f_cost:
			lowest_f_cost=open_list[coor][1]+open_list[coor][2]
			recommended_coor=coor
		else:
			pass
	closed_list[recommended_coor]=open_list.pop(recommended_coor)
	for i in range(recommended_coor[0]-1,recommended_coor[0]+2):
		for j in range(recommended_coor[1]-1,recommended_coor[1]+2):
			if  i>=0 and j>=0 and i<dimension and j<dimension: #within bounds
				if square_map[i][j] and (i,j) not in closed_list: #square not impassable or in closed set
					#cost
					if recommended_coor==start_coor:
						g_cost=0
					elif recommended_coor[1] == closed_list[recommended_coor][0][1] or recommended_coor[0] == closed_list[recommended_coor][0][0]:
						g_cost=g_cost=10+closed_list[recommended_coor][1]
					else:
						g_cost=g_cost=14+closed_list[recommended_coor][1]
					if (i,j) in open_list and g_cost>open_list[(i,j)][1]:
						pass
					else:
						open_list[(i,j)]=[recommended_coor,g_cost,manhattan_distance((i,j),end_coor)]
path=[end_coor]
while start_coor not in path:
	for coor in closed_list:
		if coor==path[-1]:
			path.append(closed_list[coor][0])
path.reverse()
for i in path:
	print(i)
input()
