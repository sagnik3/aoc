package main 

import "strings"
import "io/ioutil"
import "log"
import "fmt"

type Position struct {
	x,y int
}

func main(){
	input, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		log.Fatal(err)
	}

	homes := make(map[Position]bool)
	//starting point 
	coord := Position{0,0}

	homes[coord] = true 

	for _,dir := range strings.Split(string(input),""){
		if dir == ">" {
			coord = Position{coord.x+1,coord.y}
		} else if dir =="<" {
			coord = Position{coord.x-1,coord.y}
		} else if dir == "^" {
			coord = Position{coord.x,coord.y-1}
		} else if dir == "v" {
			coord = Position{coord.x,coord.y+1}
		}
		homes[coord] = true
	}
	fmt.Println(len(homes))
}