package main

import "fmt"

// Time complexity of this fun is O(n)

func getPairCount(arr []int, sum int) int {

	m := make(map[int]int)
	fmt.Println(m)

	n := len(arr)
	for i := 0; i < n; i++ {
		m[arr[i]]++
		fmt.Println(m)
	}

	twiceCount := 0

	for i := 0; i < n; i++ {
		twiceCount += m[sum-arr[i]]
		fmt.Println(twiceCount)

		// if arr[i] and arr[i] is the case then pair is not considered
		if sum-arr[i] == arr[i] {
			fmt.Println("twice pos ", arr[i])
			twiceCount--
		}
	}
	return twiceCount / 2

}

func main() {

	arr := []int{1, 2, 3, 3, 4, 5}
	sum := 5
	pairCount := getPairCount(arr, sum)
	fmt.Println(pairCount)

}
