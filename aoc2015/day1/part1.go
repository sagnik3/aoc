package main 

import "fmt"
import "io/ioutil"
import "log"

func main(){

	content,err := ioutil.ReadFile("input.txt")

	if(err !=nil){
		log.Fatal(err)
	}
	currentFloor := 0
	for _,value := range string(content) {
		if value=='(' {
			currentFloor+=1
		} else if value ==')' {
			currentFloor -=1
		} 
	}
	fmt.Println(currentFloor)
	
}