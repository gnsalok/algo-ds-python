package main

import (
	"fmt"
)

// Stack structure using a slice
type Stack struct {
	elements []int
}

// Push adds an element to the top of the stack
func (s *Stack) Push(value int) {
	s.elements = append(s.elements, value)
}

// Pop removes and returns the top element from the stack
func (s *Stack) Pop() (int, error) {
	if len(s.elements) == 0 {
		return 0, fmt.Errorf("stack is empty")
	}
	// Get the last element
	top := s.elements[len(s.elements)-1]
	// Remove the last element
	s.elements = s.elements[:len(s.elements)-1]
	return top, nil
}

// Peek returns the top element without removing it
func (s *Stack) Peek() (int, error) {
	if len(s.elements) == 0 {
		return 0, fmt.Errorf("stack is empty")
	}
	return s.elements[len(s.elements)-1], nil
}

// IsEmpty checks if the stack is empty
func (s *Stack) IsEmpty() bool {
	return len(s.elements) == 0
}

// Size returns the number of elements in the stack
func (s *Stack) Size() int {
	return len(s.elements)
}

// Main function to demonstrate the stack
func main() {
	stack := &Stack{}

	// Push elements onto the stack
	stack.Push(10)
	stack.Push(20)
	stack.Push(30)

	// Print stack details
	fmt.Println("Stack size:", stack.Size())
	fmt.Println("Top element:", func() int {
		top, _ := stack.Peek()
		return top
	}())

	// Pop elements from the stack
	for !stack.IsEmpty() {
		top, _ := stack.Pop()
		fmt.Println("Popped:", top)
	}

	// Try to pop from an empty stack
	_, err := stack.Pop()
	if err != nil {
		fmt.Println("Error:", err)
	}
}
