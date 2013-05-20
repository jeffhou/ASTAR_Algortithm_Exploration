import pygame,math,random
from pygame.locals import *
def manhattan_distance(in_begin_coor, in_end_coor):
	return abs(in_begin_coor[0]-in_end_coor[0])+abs(in_begin_coor[1]-in_end_coor[1])
new_click=False
square_map=[]
for i in range(10):
	square_map.append([])
	for j in range(10):
		square_map[i].append(True)
square_map[2][2]=False
start_coor=(0,0)
end_coor=(9,9)
open_list={start_coor:[None,0,manhattan_distance(start_coor,end_coor)]}
closed_list={}

pygame.init()
mainClock=pygame.time.Clock()

windowWidth=200
windowHeight=200
windowSurface=pygame.display.set_mode((windowWidth,windowHeight))
windowSurface=pygame.display.set_mode((windowWidth,windowHeight))

start=pygame.Rect(start_coor[0]*20, start_coor[1]*20, 20, 20)
final=pygame.Rect(end_coor[0]*20, end_coor[1]*20, 20, 20)
path=[]
while True:
	if 'Display':
		windowSurface.fill((0,0,0))
		for i in range(10):
			for j in range(10):
				if not square_map[i][j]:
					pygame.draw.rect(windowSurface,(255,0,0),pygame.Rect(i*20, j*20, 20, 20))
		if len(path)>0:
			for i in path:
				pygame.draw.rect(windowSurface,(155,155,155),pygame.Rect(i[0]*20+5, i[1]*20+5, 10, 10))
			
		if new_click:
			path=[]
			open_list={start_coor:[None,0,manhattan_distance(start_coor,end_coor)]}
			closed_list={}
			new_click=False
		pygame.draw.rect(windowSurface,(132,85,191),start)
		pygame.draw.rect(windowSurface,(85,132,191),final)
		pygame.display.update()
		
	if 'Events':
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN and event.button == 5:
				a=pygame.mouse.get_pos()
				(start.left,start.top)=(int(a[0]/20)*20,int(a[1]/20)*20)
				start_coor=(int(a[0]/20),int(a[1]/20))
				print(start)
				del a
			if event.type == MOUSEBUTTONDOWN and event.button == 4:
				a=pygame.mouse.get_pos()
				(final.left,final.top)=(int(a[0]/20)*20,int(a[1]/20)*20)
				end_coor=(int(a[0]/20),int(a[1]/20))
				del a
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				new_click=True
				a=pygame.mouse.get_pos()
				square_map[int(a[0]/20)][int(a[1]/20)]=not square_map[int(a[0]/20)][int(a[1]/20)]
			if event.type == KEYDOWN and event.key == 32:
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
							if  i>=0 and j>=0 and i<10 and j<10: #within bounds
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
				path.pop(0)
				for i in path:
					print(i)
				
'''
if 'Logic':
	#pygame.display.set_caption(str(minion['rect'])+str(' ')+str(minion['dir']))
	if int(minion['rect'].right)+int(math.cos(math.radians(minion['dir']))) > windowWidth:
		minion['dir']= (minion['dir']+90)%360
	if int(minion['rect'].bottom)+int(math.sin(math.radians(minion['dir']))) > windowHeight:
		minion['dir']= (minion['dir']+90)%360
	if int(minion['rect'].top)+int(math.sin(math.radians(minion['dir']))) < 0:
		minion['dir']= (minion['dir']+90)%360
	if int(minion['rect'].left)+int(math.cos(math.radians(minion['dir']))) < 0:
		minion['dir']= (minion['dir']+90)%360
		
	minion['rect'].left+=int((math.cos(math.radians(minion['dir']))))
	minion['rect'].top+=int((math.sin(math.radians(minion['dir']))))
mainClock.tick(100)
'''