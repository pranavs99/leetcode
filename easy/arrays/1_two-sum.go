func twoSum(nums []int, target int) []int {
	// create a mapping between the complement of a number and its index
	complementToIndex := map[int]int{}

	// iterate through nums and map (target - n) to its index
	for i, n := range nums {
		complement := target - n
		value, found := complementToIndex[n]
		if found {
			return []int{value, i}
		} else {
			complementToIndex[complement] = i
		}
	}

	fmt.Println(complementToIndex)

	return []int{}
}