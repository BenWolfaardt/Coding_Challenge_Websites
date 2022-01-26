package leetcode

import (
	"reflect"
	"testing"
)

func Test_generate(t *testing.T) {
	type args struct {
		num_rows int
	}
	testCases := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "Example 1",
			args: args{num_rows: 5},
			want: [][]int{
				{1},
				{1, 1},
				{1, 2, 1},
				{1, 3, 3, 1},
				{1, 4, 6, 4, 1},
			},
		},
		{
			name: "Example 2",
			args: args{num_rows: 10},
			want: [][]int{
				{1},
				{1, 1},
				{1, 2, 1},
				{1, 3, 3, 1},
				{1, 4, 6, 4, 1},
				{1, 5, 10, 10, 5, 1},
				{1, 6, 15, 20, 15, 6, 1},
				{1, 7, 21, 35, 35, 21, 7, 1},
				{1, 8, 28, 56, 70, 56, 28, 8, 1},
				{1, 9, 36, 84, 126, 126, 84, 36, 9, 1},
			},
		},
	}
	for _, tC := range testCases {
		t.Run(tC.name, func(t *testing.T) {
			if got := generate(tC.args.num_rows); !reflect.DeepEqual(got, tC.want) {
				t.Errorf("generate() = %v, want %v", got, tC.want)
			}
		})
	}
}
