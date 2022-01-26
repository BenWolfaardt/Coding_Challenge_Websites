package leetcode

import (
	elapsedTime "BenWolfaardt/Practice_Coding_Challenges/tree/02-LeetCode-Go/Utilities"
	"time"
)

func generate(numRows int) [][]int {
	// initiate timer for function
	defer elapsedTime.Timer(time.Now())

	var triangle [][]int
	var prevRow = []int{1}

	if numRows > 0 {
		triangle = append(triangle, prevRow)
	}

	for i := 1; i < numRows; i++ {
		lenPrevRow := len(prevRow)
		var currentRow = make([]int, lenPrevRow+1)

		currentRow[0], currentRow[lenPrevRow] = 1, 1

		for j := 1; j < lenPrevRow; j++ {
			currentRow[j] = prevRow[j-1] + prevRow[j]
		}
		triangle = append(triangle, currentRow)
		prevRow = currentRow
	}
	return triangle
}
