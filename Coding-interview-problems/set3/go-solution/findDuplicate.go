package main

import (
	"fmt"
)

func add(arr []int) int {

	sum := 0
	for i := 0; i < len(arr); i++ {
		sum = sum + arr[i]
	}
	return sum

}

func findDuplicate(arr []int) int {
	n := len(arr)
	result := add(arr) - ((n - 1) * n / 2)
	return result

}

func main() {

	arr := []int{1, 2, 2, 3, 4, 5}
	dupVal := findDuplicate(arr)
	fmt.Println(dupVal)
}
