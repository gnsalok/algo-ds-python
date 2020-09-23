package main

import (
	"fmt"
)

/*
import (
    "sync"
    "time"
)

type IPCounter struct {
    IPAddr string
    Time   time.Time
    Count  int
}

type ipCounterMap struct {
    counters map[string]IPCounter
    mutex    sync.RWMutex
}

*/
func findAllPairs(arr []int) {
	//n := len(arr)
	m := make(map[int][]int)

	// for i:=0; i< (n-1); i++{
	// 	for j := i+1; j <= n; j++{

	// 		sum := arr[i] + arr[j]

	// 		if v, found :=  m[sum]; found{

	// 			prePair := m.get(sum)
	// 			fmt.Println(prePair)

	// 			fmt.Println(arr[i], arr[j])  (3,2)

	// 		}else{
	// 			m[sum] = (arr[i], arr[j])

	// 		}
	// }
}

func main() {

	findAllPairs()

}
