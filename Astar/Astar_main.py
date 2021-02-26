
"""
this project will be a go at an object oriented visual representation of an A* search algorithm
"""

class astar:
    def __init__(self,db):
        self.board = db
        
        self.f_scores=[]
        self.discovered=[]
        self.alg()
    
    #place spot in order of fscores
    def put_f(self, val, spot):
        for i in range(len(self.f_scores)):
            if val < self.f_scores[i][0]:
                self.f_scores.insert(i,(val,spot))
                return None
        self.f_scores.append((val,spot))

    #return distance to end
    def h(self,s1,s2):
        p1 = (s1.grid_info()['column']+1,s1.grid_info()['row']+1)
        p2 = (s2.grid_info()['column']+1,s2.grid_info()['row']+1)
        # print(abs(p2[0]-p1[0]) + abs(p2[1]-p1[1]))
        return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])
    
    #add neighbor info to a spot object
    def find_neighbors(self, spot):
        cx = spot.grid_info()['column']
        cy = spot.grid_info()['row']
        spot.neighbors=[]
    
        #up
        if cy>0 and self.board.pos[cx][cy-1]['bg'] != 'black':
            if self.discovered.count(self.board.pos[cx][cy-1]) == 0:
                spot.neighbors.append(self.board.pos[cx][cy-1])
                self.board.pos[cx][cy-1].b4 = spot.b4 + [spot]
                self.discovered.append(self.board.pos[cx][cy-1])
    
        #down
        if cy < self.board.size-1 and self.board.pos[cx][cy+1]['bg'] != 'black':
            if self.discovered.count(self.board.pos[cx][cy+1]) == 0:
                spot.neighbors.append(self.board.pos[cx][cy+1])
                self.board.pos[cx][cy+1].b4 = spot.b4 + [spot]
                self.discovered.append(self.board.pos[cx][cy+1])
    
        #left
        if cx>0 and self.board.pos[cx-1][cy]['bg'] != 'black':
            if self.discovered.count(self.board.pos[cx-1][cy]) == 0:
                spot.neighbors.append(self.board.pos[cx-1][cy])
                self.board.pos[cx-1][cy].b4 = spot.b4 + [spot]
                self.discovered.append(self.board.pos[cx-1][cy])
    
        #right
        if cx<self.board.size-1 and self.board.pos[cx+1][cy]['bg'] != 'black':
            if self.discovered.count(self.board.pos[cx+1][cy]) == 0:
                spot.neighbors.append(self.board.pos[cx+1][cy])
                self.board.pos[cx+1][cy].b4 = spot.b4 + [spot]
                self.discovered.append(self.board.pos[cx+1][cy])

    #color where the algorithm has looked gold
    def path(self, spot):
        if spot != self.board.end:
            for step in spot.b4:
                if step != self.board.start:
                    step.config(bg='gold')
        else:
            for step in spot.b4:
                if step != self.board.start:
                    step.config(bg='purple')

    #where the A* magic happens
    def alg(self):
        self.board.start.b4=[]
        current = self.board.start
        self.f_scores.append((self.h(self.board.start,self.board.end),self.board.start))
        while current != self.board.end:
            #gaining info
            self.find_neighbors(current)
            for n in current.neighbors:
                self.put_f(self.h(n, self.board.end)+len(n.b4),n)
            # print(self.f_scores)
            #taking best option
            current = self.f_scores[0][1]
            self.f_scores.remove(self.f_scores[0])
            self.path(current)
        self.path(current)

