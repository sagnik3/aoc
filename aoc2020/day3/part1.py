def main():
    with open('input.txt','r') as f:
        p= f.readlines()

    p=[x.strip() for x in p]
    p = [ line[0:-1] for line in p]
    
    width =  len(p[0])

    def check(right,bottom):
        x, y = 0 , 0
        count = 0

        while not  y >= len(p) - 1:
            x += right
            y += bottom 

            if x>= width:
                x -= width 
            if p[y][x] == "#":
                count +=1
        return count 


    print(check(3,1))


main()
