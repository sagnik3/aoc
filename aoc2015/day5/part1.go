package main

import "fmt"
import "io/ioutil"
import "log"
import "strings"
import "regexp"

func threeOrMoreVowels(str string) bool {
	vowels := []string{"a", "e", "i", "o", "u"}
	count := 0

	for _, vowel := range vowels {
		count += strings.Count(str, vowel)
	}
	return count >= 3
}

func repeatingLetter(str string) bool {
	for i := 0; i < len(str)-1; i++ {
		if str[i] == str[i+1] {
			return true
		}
	}
	return false
}

func excludeBadSubStrings(str string) bool {
	return !regexp.MustCompile("ab|cd|pq|xy").MatchString(str)
}

func allowed(str string) bool {
	return excludeBadSubStrings(str) && repeatingLetter(str) && threeOrMoreVowels(str)
}

func main() {
	file, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	strings := strings.Split(string(file), "\n")
	count := 0
	for _, str := range strings {
		if allowed(str) {
			count += 1
		}
	}
	fmt.Println(count)

}
