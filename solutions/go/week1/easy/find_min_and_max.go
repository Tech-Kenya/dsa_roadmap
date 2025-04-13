package main

import (
	"math"
)

// finding the minimum and maximum element in an array
func FindMinAndMax(nums []int) (int,int) {
	//variables to hold min and max as we iterate through the array
	// initialize max to the smallest possible integer value
	max := math.MinInt
	// initialize min to the largest possible integer value
	min := math.MaxInt

	// iterate through all numbers in the array updating min and max accordingly
	for _,num := range nums {
		if num > max {
			max = num
		}else if num < min {
			min = num
		}
	}

	return min,max
}