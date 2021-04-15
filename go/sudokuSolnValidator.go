package kata

import "fmt"

type row [9]int
type col [9]int

type Sudoku struct {
	field [9]row
}

func (s Sudoku) getIthCol(i int) col {
	var newCol col
	for j := 0; j < 9; j++ {
		newCol[j] = s.field[j][i]
	}

	return newCol
}

func (s Sudoku) getBlock(i, j int) col {
	var newCol col
	counter := 0

	for x := i - 3; x < i; x++ {
		for y := j - 3; y < j; y++ {
			newCol[counter] = s.field[x][y]
			counter++
		}

	}

	return newCol
}

func arrSum(r [9]int) int {
	s := 0
	for i := 0; i < 9; i++ {
		s += r[i]
	}
	return s
}

func ValidateSolution(m [][]int) bool {
	var sudoku Sudoku
	var r0 row
	for i, r := range m {
		copy(r0[:], r)
		sudoku.field[i] = r0
	}

	for i := 0; i < 9; i++ {
		if arrSum(sudoku.field[i]) != 45 ||
			arrSum(sudoku.getIthCol(1)) != 45 {
			return false
		}
	}

	for i := 3; i <= 9; i += 3 {
		for j := 3; j <= 9; j += 3 {
			fmt.Println(sudoku.getBlock(i, j))
			if arrSum(sudoku.getBlock(i, j)) != 45 {
				return false
			}

		}

	}

	return true
}
