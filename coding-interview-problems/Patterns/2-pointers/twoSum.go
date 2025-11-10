package main

import "fmt"

func twoSum(arr []int, target int) []int {
	st := make(map[int]int)
	for i := range arr {
		comp := target - arr[i]
		if idx, ok := st[comp]; ok {
			return []int{idx, i}
		}
		st[arr[i]] = i
	}
	return nil
}

func main() {
	input := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(input, target)
	fmt.Println(result)
}
