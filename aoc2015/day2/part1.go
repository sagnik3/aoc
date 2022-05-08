package main 

import "fmt"
import "io/ioutil"
import "log"
import "strings"
import "sort"
import "strconv"


func main(){
	file,err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	presents := strings.Split(string(file),"\n")

	total :=0

	for _,v := range presents {
		sides := []int{}

		for _,sidestring := range strings.Split(v,"x") {
			side , _ := strconv.Atoi(sidestring)
			sides  = append(sides,side)
		}

		sort.Ints(sides)

		total += sides[0] * sides[1] *3 
		total += sides[0] * sides[2] *2
		total += sides[1] * sides[2] *2
			
	}
	fmt.Println(total)
}