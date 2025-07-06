fun solution(num : Int,
             limit : Int,
             power : Int) : Int {
    val divisors = IntArray(num +1) { getDivisorCount(it) }

    return divisors.slice(1..num).sumOf {
      if (it > limit) power else it
    }
}

fun getDivisorCount(num : Int) : Int {
    if (num ==0) return 0
    var count = 0
    var i = 1

    while (i * i <= num) {
        if (i*i == num) {
           count++
        } else if (num % i == 0) {
          count += 2
        }
        i++
    }

    return count

}


fun main() {
    println(solution(10, 3, 2))
    println(solution(5, 3, 2))
}
