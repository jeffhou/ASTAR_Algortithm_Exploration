import pygame,math,random
from pygame.locals import *
def manhattan_distance(in_begin_coor, in_end_coor):
	return abs(in_begin_coor[0]-in_end_coor[0])+abs(in_begin_coor[1]-in_end_coor[1])
new_click=False
square_map=[]
grid_file=open("grid.txt")
square_map=grid_file.readlines()
for i in range(len(square_map)):
	square_map[i]=list(square_map[i].strip())
	for j in range(len(square_map[i])):
		square_map[i][j]=square_map[i][j]=='1'
start_coor=(0,0)
end_coor=(0,0)
open_list={start_coor:[None,0,manhattan_distance(start_coor,end_coor)]}
closed_list={}

pygame.init()
mainClock=pygame.time.Clock()

windowWidth=400
windowHeight=400
windowSurface=pygame.display.set_mode((windowWidth,windowHeight))
windowSurface=pygame.display.set_mode((windowWidth,windowHeight))

start=pygame.Rect(start_coor[0]*5, start_coor[1]*5, 5, 5)
final=pygame.Rect(end_coor[0]*5, end_coor[1]*5, 5, 5)
path=[]
destination=start_coor
while True:
	pygame.display.set_caption(str(start_coor)+' '+str(len(path))+' '+str(end_coor))
	if 'Display':
		windowSurface.fill((0,0,0))
		obstacle_course=pygame.image.load('new_preview.png')
		windowSurface.blit(obstacle_course,(0,0))			
		pygame.draw.rect(windowSurface,(132,85,191),start)
		pygame.display.update()
		try:
			pygame.draw.rect(windowSurface,(255,255,255),pygame.Rect(destination[0]*5, destination[1]*5, 5, 5))
		except:
			pass
	if 'Events':
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				path=[]
				
				closed_list={}
				a=pygame.mouse.get_pos()
				(start.left,start.top)=(int(a[0]/5)*5,int(a[1]/5)*5)
				start_coor=(int(a[0]/5),int(a[1]/5))
				open_list={start_coor:[None,0,manhattan_distance(start_coor,end_coor)]}
				del a
			if event.type == MOUSEBUTTONDOWN and event.button == 3:
				path=[]
				
				closed_list={}
				a=pygame.mouse.get_pos()
				(final.left,final.top)=(int(a[0]/5)*5,int(a[1]/5)*5)
				end_coor=(int(a[0]/5),int(a[1]/5))
				open_list={start_coor:[None,0,manhattan_distance(start_coor,end_coor)]}
				del a
			if path==[] and end_coor!=start_coor and event.type==MOUSEBUTTONDOWN:
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
							if  i>=0 and j>=0 and i<80 and j<80: #within bounds
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
						if coor==path[-1] and closed_list[coor][0]!=None:
							path.append(closed_list[coor][0])
				path.reverse()
				path.pop(0)
				print(path)
				destination=path.pop(0)
	if 'Logic':
		if start_coor!=end_coor:
			if start_coor!=destination and start.left==destination[0]*5 and start.top==destination[1]*5:
				start_coor=destination
			if len(path)>0:
				if start.left==destination[0]*5 and start.top==destination[1]*5:
					destination=path.pop(0)
			if start.left!=destination[0]*5 or start.top!=destination[1]*5:
				if start.left!=destination[0]*5:
					start.left-=int((start.left-destination[0]*5)/abs(start.left-destination[0]*5))
				if start.top!=destination[1]*5:
					start.top-=int((start.top-destination[1]*5)/abs(start.top-destination[1]*5))
			if start.left == final.right and start.top==final.top:
				destination==(int(start.left/5),int(start.top/5))
				path=[]
	mainClock.tick(100)
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