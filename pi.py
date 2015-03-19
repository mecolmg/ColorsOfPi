from sympy.mpmath import mp
from Tkinter import *
from colour import Color
import time
import math

class piDraw:
    def __init__(self, size):
        self.size = size
        self.start = 0
        self.pi = str(mp.pi/10)[2:]
    def next(self):
        result = int(self.pi[self.start:self.start+3])
        self.start += 3
        return result
    def nextColor(self):
        return self.next()/1000.0
    def restart(self):
        self.start = 0
    def getPi(self, size):
        mp.dps = size
        self.pi = str(mp.pi/10)[2:]
    def makeGrid(self):
        self.restart()
        self.size = self.size + (self.size+1)%2
        self.getPi(9*self.size**2)
        grid = [[0 for i in range(self.size)] for j in range(self.size)]
        x = y = 0
        dx = 0
        dy = -1
        m = self.size/2
        for a in range(self.size**2):
            if (-m <= x <= m) and (-m <= y <= m):
                c = Color(rgb=(self.nextColor(),self.nextColor(),self.nextColor()))
                grid[x+m][y+m] = [c.hex]
            if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
                dx, dy = -dy, dx
            x, y = x+dx, y+dy
        return grid
    def drawGrid(self):
        grid = self.makeGrid()
        master = Tk()
        cellsize = 5
        size = cellsize * self.size
        w = Canvas(master,width=size,height=size)
        w.pack()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                w.create_rectangle(c*cellsize,r*cellsize,
                                   (c+1)*cellsize,(r+1)*cellsize,
                                   fill=grid[r][c])
        mainloop()
    def drawCircle(self):
        radius = 300
        self.restart()
        if self.size < 3:
            print('Invalid size, must be greater than 3')
            return -1
        self.getPi(self.size+2)

        master = Tk()
        size = radius*2+50
        w = Canvas(master,width=size,height=size)
        w.pack()
        w.create_oval(25,25,25+radius*2,25+radius*2,fill="white")
        count = [0 for _ in xrange(10)]
        coords =[]
        for i in xrange(len(self.pi)-2):
            count[int(self.pi[i])] += 1
            color = "#"+self.pi[i:i+3]
            coords.append([int(self.pi[i]),int(self.pi[i+1]),color])
        angles = [36.0 for _ in xrange(10)]
        for i in range(10):
            if count[i] != 0:
                angles[i] = 36.0/count[i]
        count2 = [0 for _ in xrange(10)]
        start = time.time()
        for line in coords[:-1]:
            count2 = self.drawLine(line, count2, angles, radius, w)
        end = time.time()
        print(end-start)
        mainloop()

    def drawLine(self,coord, count, angles, radius, canvas):
        p1,p2,color = coord
        angle1 = math.radians(36.0*p1+angles[p1]*count[p1])
        count[p1] += 1
        angle2 = math.radians(36.0*p2+angles[p2]*count[p2])
        if(count[p1] == 1):
            x1 = (radius+10)*math.cos(angle1)+radius+25
            y1 = (radius+10)*math.sin(angle1)+radius+25
            canvas.create_text(x1,y1, text=str(p1))

        x1 = radius*math.cos(angle1)+radius+25
        y1 = radius*math.sin(angle1)+radius+25
        x2 = radius*math.cos(angle2)+radius+25
        y2 = radius*math.sin(angle2)+radius+25
        canvas.create_line(x1,y1,x2,y2,fill=color)
        return count

pi = piDraw(100000)
pi.drawCircle()

