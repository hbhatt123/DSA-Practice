class Graph:
    def floodFill(self, image, sr: int, sc: int, color: int):
        height = len(image)
        width = len(image[0])
        cur_color = image[sr][sc]

        def dfs(sr,sc):
            if sr < 0 or sr >= height or sc < 0 or sc >= width:
                return
            if image[sr][sc] != cur_color:
                return     
            image[sr][sc] = color
            dfs(sr-1,sc)
            dfs(sr+1,sc)
            dfs(sr,sc+1)
            dfs(sr,sc-1)
            print(sr,sc)


        dfs(sr,sc)

        return image        
        
if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    graph = Graph()
    print(graph.floodFill(image,sr,sc,color))
