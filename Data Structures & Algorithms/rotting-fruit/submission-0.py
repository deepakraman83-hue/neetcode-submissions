class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty,fresh,rotten=0,1,2
        num_fresh=0
        num_min=-1
        q=deque()
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==rotten:
                    q.append((i,j))
                elif grid[i][j]==fresh:
                    num_fresh+=1
        
        if num_fresh==0:
            return 0
        
        while q:
            q_size=len(q)
            num_min+=1
            for _ in range(q_size):
                r,c=q.popleft()
                for i,j in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    if 0<=i<m and 0<=j<n and grid[i][j]==fresh:
                        num_fresh-=1
                        q.append((i,j))
                        grid[i][j]=rotten
        if num_fresh==0:
            return num_min
        else:
            return -1


            
                    
            

                    