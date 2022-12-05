use std::fs::File;
use std::io::prelude::*;

fn read_input() -> String{
    let mut file = File::open("C:/git/AdventOfCode/2022/04/main/src/input.txt").unwrap();
    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();
    return data;
}



fn main() {
    let input = read_input();
    
    // Task 1: Count number of sets contained in the other
    // Task 2: Count number of sets that don't overalap at all
    let lines = input.lines();

    let mut contained_counter = 0;
    let mut line_counter = 0;
    let mut non_overlapping_counter = 0;
    for line in lines{
        // Split line and extract ranges
        let mut split = line.split(",");
        let mut points_1 = split.next().unwrap().split("-");
        let mut points_2 = split.next().unwrap().split("-");

        // Extract min and max points
        let min_1 = points_1.next().unwrap().parse::<i32>().unwrap();
        let max_1 = points_1.next().unwrap().parse::<i32>().unwrap();
        let min_2 = points_2.next().unwrap().parse::<i32>().unwrap();
        let max_2 = points_2.next().unwrap().parse::<i32>().unwrap();

        // Count number of full overlaps
        if (min_1 <= min_2 && max_1 >= max_2) || (min_1 >= min_2 && max_1 <= max_2){
            contained_counter += 1;
        }

        // Count number of sections without overlap at all
        if min_1 > max_2 || min_2 > max_1{
            non_overlapping_counter += 1
        }
        
        line_counter += 1;
    }

    println!("Task 1: {}", contained_counter);
    println!("Task 2: {}", line_counter - non_overlapping_counter);

}
