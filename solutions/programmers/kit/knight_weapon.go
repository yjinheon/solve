package main

import "fmt"

func solve(num int, limit int, power int) int {
	arr := []int{} // initalize an empty array
	res := 0

	// 약수의 개수 구하기

	for i := 1; i <= num; i++ {
		arr = append(arr, get_num_divisor(i))
	}

	fmt.Println(arr)

	process(arr, limit, power)

	for _, v := range arr {
		res += v
	}

	fmt.Println(res)

	return res
}

func process(arr []int, limit, power int) []int {
	for i, v := range arr {
		if v > limit {
			arr[i] = power
		}
	}
	return arr
}

func get_num_divisor(num int) int {
	count := 0
	for i := 1; i*i <= num; i++ {
		if i*i == num {
			count++
			continue
		}

		if num%i == 0 {
			count += 2
			continue
		}
	}

	return count
}

func main() {
	solve(5, 3, 2)
	solve(10, 3, 2)
}
