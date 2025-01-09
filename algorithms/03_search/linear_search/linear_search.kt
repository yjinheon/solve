
import java.util.*

fun main() {
    val scanner = Scanner(System.`in`)

    // input
    val n = scanner.nextInt()
    val v = scanner.nextInt()
    val a = IntArray(n) { scanner.nextInt() }

    // linear search
    var exist = false
    for (element in a) {
        if (element == v) {
            exist = true
            break
        }
    }

    // print
    if (exist) {
        println("Yes")
    } else {
        println("No")
    }
}
