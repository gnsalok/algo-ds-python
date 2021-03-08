package main

import (
	"encoding/json"
	"fmt"
)

// Big O (n^2) there may better solution. (Use Hashmap insted)
/*
func findCommonEle(arr1 []int, arr2 []int) bool {
	for i := 0; i < len(arr1); i++ {
		for j := 0; j < len(arr2); j++ {
			if arr1[i] == arr2[j] {
				return true
			}
		}
	}
	return false
}

*/

func findCommonEle(arr1 []int, arr2 []int) {

	// Create object of first array and set all the value as true
	//
	// arr2[index] --> object.properties

	//code this solution

	// O(a + b)

}

func main() {

	// Inputs
	arr1 := []int{1, 2, 3, 4, 5}
	arr2 := []int{6, 7, 5, 1, 3}

	res := findCommonEle(arr1, arr2)
	fmt.Println(res)
}
