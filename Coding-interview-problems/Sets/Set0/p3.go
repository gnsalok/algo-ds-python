package main

import "fmt"

func findAllPair(arr []int) {

	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr); j++ {
			fmt.Println(arr[i], arr[j], " = ", arr[i]+arr[j])
		}
	}

}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	findAllPair(arr)
}
