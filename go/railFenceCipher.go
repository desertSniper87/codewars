package kata

import (
	"fmt"
)

func zigZagRowN (n int) int {
	
}

func Encode(s string, n int) string {
	l := len(s)
	// var encoded_s = make([]rune, l, l)
	// var encoded_mat = make([][]rune, n, n)

	for i := 0; i < l; i++ {
		row := i % (n-1)
		fmt.Println(row)
		
	}
	return "NIGGA"
}

func Decode(s string, n int) string {
	return "ASSHOLE"
}
