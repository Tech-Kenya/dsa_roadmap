package main

func ReverseArray(nums []int) []int {
	// using two pointers to reverse the array in place -> to avaid using extra memory
	//declare the left pointer(at the begining of the array)
	left :=0
	//declare the right pointer(at the end of the array)	
	right := len(nums) -1

	for left < right {
		//swap elements => you could also use a temporary variable for swapping
		nums[left],nums[right] = nums[right],nums[left]
		//move pointers inwards
		left++
		right--
	}

	return nums
}

