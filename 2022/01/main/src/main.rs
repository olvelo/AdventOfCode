use std::fs::File;
use std::io::prelude::*;

fn read_input() -> String{
    let mut file = File::open("C:/git/AdventOfCode/2022/01/main/src/input.txt").expect("File not found");
    let mut data = String::new();
    file.read_to_string(&mut data).expect("Error when reading file");
    return data;
}

fn main() {
    let input = read_input();
    let lines = input.lines();

    let mut calorie_sums = Vec::new();
    let mut calorie_sum = 0;
    for line in lines{
        if line != ""{
            calorie_sum = calorie_sum + line.parse::<i32>().unwrap();
        }
        else{
            calorie_sums.push(calorie_sum);
            calorie_sum = 0;
        }
    }
    calorie_sums.push(calorie_sum);
    calorie_sums.sort();
    calorie_sums.reverse();

    println!("Three largest calorie sums: {}, {} and {}", calorie_sums[0], calorie_sums[1], calorie_sums[2]);
    println!("Sum of three largest calorie sums: {}", calorie_sums[0] + calorie_sums[1] + calorie_sums[2]);
}
