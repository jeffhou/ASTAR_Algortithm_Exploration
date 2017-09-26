import pygame,math,random
from pygame.locals import *
def manhattan_distance(in_begin_coor, in_end_coor):
	return abs(in_begin_coor[0]-in_end_coor[0])+abs(in_begin_coor[1]-in_end_coor[1])
new_click=False
start_coor=(0,0)
end_coor=(9,9)
pygame.init()
windowWidth=200
windowHeight=200
mainClock=pygame.time.Clock()
windowSurface=pygame.display.set_mode((windowWidth,windowHeight))
start=pygame.Rect(start_coor[0]*20, start_coor[1]*20, 20, 20)
final=pygame.Rect(end_coor[0]*20, end_coor[1]*20, 20, 20)
while True:
	if 'Display':
		windowSurface.fill((0,0,0))
		for i in range(10):
			for j in range(10):
				if (i+j)%2==0:
					pygame.draw.rect(windowSurface,(120,120,0),pygame.Rect(i*20, j*20, 20, 20))
				else:
					pygame.draw.rect(windowSurface,(0,120,120),pygame.Rect(i*20, j*20, 20, 20))
		pygame.draw.rect(windowSurface,(85,132,191),final)
		pygame.draw.rect(windowSurface,(132,85,191),start)
		pygame.display.update()
		
	if 'Events':
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				a=pygame.mouse.get_pos()
				(start.left,start.top)=(int(a[0]/20)*20,int(a[1]/20)*20)
				start_coor=(int(a[0]/20),int(a[1]/20))
				print(start)
				del a
			if event.type == MOUSEBUTTONDOWN and event.button == 3:
				a=pygame.mouse.get_pos()
				(final.left,final.top)=(int(a[0]/20)*20,int(a[1]/20)*20)
				end_coor=(int(a[0]/20),int(a[1]/20))
				del a
	if 'Logic':
		if start.left!=final.left:
			start.left-=int((start.left-final.left)/abs(start.left-final.left))
		if start.top!=final.top:
			start.top-=int((start.top-final.top)/abs(start.top-final.top))
	mainClock.tick(20)