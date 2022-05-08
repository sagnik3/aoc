package main 

import "fmt"
import "log"
import "io/ioutil"

func main(){
	file,err := ioutil.ReadFile("input.txt")

	if(err!=nil){
		log.Fatal(err)
	}
	position := 0 

	for index,value := range string(file) {
		if  value == '('{
			position +=1
		} else if value == ')' {
			position -=1
		}

		if position == -1 {
			fmt.Println(index+1)
			break 
		}
	}
}