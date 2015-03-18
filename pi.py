from sympy.mpmath import mp
from Tkinter import *
from colour import Color

class piDraw:
    def __init__(self, size):
        self.size = size + (size+1)%2
        self.start = 0
        mp.dps = 9*self.size**2
        self.pi = str(mp.pi/10)[3:]
    def next(self):
        result = int(self.pi[self.start:self.start+3])
        self.start += 3
        return result
    def nextColor(self):
        return self.next()/1000.0
    def restart(self):
        self.start = 0
    def makeGrid(self):
        grid = [[(0,0,0) for i in range(self.size)] for j in range(self.size)]
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
    def drawSquare(self, x, y, cellsize):
        print("Soon...")
            
                
pi = piDraw(201)
grid = pi.drawGrid()
