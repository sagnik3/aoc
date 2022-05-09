package main

import (
	"crypto/md5"
	"fmt"
	"strings"
)

func main() {
	input := "ckczppom"
	//input2 := "abcdef"
	//input3 := "pqrstuv"
	//data := []byte(string(input2))
	var number int 
	substr := "000000"
	
	for{ 
		//val := string(input)+string(strconv.Itoa(number))
		//using string is expensive 
		data := []byte(fmt.Sprintf("%s%d",input,number))
		checksum := fmt.Sprintf("%x",md5.Sum(data))
		fmt.Printf("%s --> hash value is %x\n",data, checksum)
		if strings.HasPrefix(checksum,substr) {
			fmt.Printf("The solution := %s\n and value %x\n",data,checksum)
			break
		}
		number = number+1
	}
}
