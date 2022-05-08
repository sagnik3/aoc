package main

import "fmt"
import "strconv"
import "strings"
import "sort"
import "bufio"
import "log"
import "os"

func main() {
	file, err := os.Open("./input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	total := 0

	for scanner.Scan() {
		present := scanner.Text()
		sides := []int{}

		for _, sideString := range strings.Split(present, "x") {
			side, _ := strconv.Atoi(sideString)
			sides = append(sides, side)
		}
		sort.Ints(sides)

		//wrap case
		total += (sides[0] + sides[1])*(2)

		//bow case
		total += sides[0] * sides[1] * sides[2]
	}
	fmt.Println(total)
}
