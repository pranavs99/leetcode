// helper function to swap the values at indices a and b
func swap(s []byte, a int, b int) {
	temp := s[a]
	s[a] = s[b]
	s[b] = temp
}

// helper function to accomplish the recursive dirty work of reverseString()
func helper(s []byte, a int, b int) {
	if a == b || a > b {
		return
	}
	swap(s, a, b)
	helper(s, a+1, b-1)
}

func reverseString(s []byte) {
	helper(s, 0, len(s)-1)
}