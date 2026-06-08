package main

import "fmt"

var soundMap = map[int]string{
	1:  "bd",  // kick (assertion)
	0:  "hh",  // hat (sustain)
	-1: "sn",  // snare (opposition)
}

func vectorToPattern(vector []int) []string {
	pat := make([]string, len(vector))
	for i, v := range vector {
		pat[i] = soundMap[v]
	}
	return pat
}

func euclidean(ones, total int) string {
	return fmt.Sprintf("e(%d, %d)", ones, total)
}

func density(vector []int) float64 {
	nonZero := 0
	for _, v := range vector {
		if v != 0 {
			nonZero++
		}
	}
	return float64(nonZero) / float64(len(vector))
}

func main() {
	vectors := [][]int{
		{1, 0, -1, 1, 0, -1, 1, 1},
		{1, 1, 1, -1, -1, -1, 1, 1},
		{1, 0, 0, 1, 0, 0, 1, 0},
	}

	for _, v := range vectors {
		pat := vectorToPattern(v)
		ones := 0
		for _, x := range v { if x == 1 { ones++ } }
		fmt.Printf("Vector %v\n", v)
		fmt.Printf("  Pattern:   s(%q)\n", pat)
		fmt.Printf("  Euclidean: %s\n", euclidean(ones, len(v)))
		fmt.Printf("  Density:   %.2f\n\n", density(v))
	}
}
