package main

import "fmt"

func fibonacci(n int) int {
	sum := 0
	if n <= 0 {
		print("Incorrect input")
	} else if n == 1 {
		return 0
	} else if n == 2 {
		return 1
	} else {
		sum = fibonacci(n-1) + fibonacci(n-2)
	}
	return sum

}

func main() {
	sumFib := fibonacci(6)
	fmt.Println(sumFib)

	// 0,1,1,2,3,5 = 5

}
