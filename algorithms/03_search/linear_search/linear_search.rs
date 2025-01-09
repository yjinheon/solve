
use std::io;

fn main() {
    // handle input
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut parts = input.trim().split_whitespace();
    let n: usize = parts.next().unwrap().parse().unwrap();
    let v: i32 = parts.next().unwrap().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let a: Vec<i32> = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    // linear search 
    let exist = a.iter().any(|&x| x == v);

    
    if exist {
        println!("Yes");
    } else {
        println!("No");
    }
}
