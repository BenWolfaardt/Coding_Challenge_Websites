package leetcode

import "testing"

// BFS
func Test_numIslandsBFS(t *testing.T) {
	type args struct {
		grid [][]byte
	}
	testCases := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Example 1",
			args: args{grid: [][]byte{
				{'1', '1', '1', '1', '0'},
				{'1', '1', '0', '1', '0'},
				{'1', '1', '1', '1', '0'},
				{'0', '0', '0', '0', '0'},
			}},
			want: 1,
		},
		{
			name: "Example 2",
			args: args{grid: [][]byte{
				{'1', '1', '0', '0', '0'},
				{'1', '1', '0', '0', '0'},
				{'0', '0', '1', '0', '0'},
				{'0', '0', '0', '1', '1'},
			}},
			want: 3,
		},
	}
	for _, tC := range testCases {
		t.Run(tC.name, func(t *testing.T) {
			if got := numIslandsBFS(tC.args.grid); got != tC.want {
				t.Errorf("numIslands() = %v, want %v", got, tC.want)
			}
		})
	}
}

// DFS
func Test_numIslandsDFS(t *testing.T) {
	type args struct {
		grid [][]byte
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Example 1",
			args: args{grid: [][]byte{
				{'1', '1', '1', '1', '0'},
				{'1', '1', '0', '1', '0'},
				{'1', '1', '1', '1', '0'},
				{'0', '0', '0', '0', '0'},
			}},
			want: 1,
		},
		{
			name: "Example 2",
			args: args{grid: [][]byte{
				{'1', '1', '0', '0', '0'},
				{'1', '1', '0', '0', '0'},
				{'0', '0', '1', '0', '0'},
				{'0', '0', '0', '1', '1'},
			}},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numIslandsDFS(tt.args.grid); got != tt.want {
				t.Errorf("numIslands() = %v, want %v", got, tt.want)
			}
		})
	}
}
