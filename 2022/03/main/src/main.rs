use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;
use std::collections::HashSet;

fn read_input() -> String{
    let mut file = File::open("C:/git/AdventOfCode/2022/03/main/src/input.txt").unwrap();
    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();
    return data;
}

fn main() {
    let input = read_input();

    // Part 1
    // Find common letter in each compartment
    let lines = input.lines();
    let mut duplicates = String::new();
    for line in lines{
        // Split in middle of the string
        let (compartment_1, compartment_2) = line.split_at(line.chars().count() / 2);
        
        // Create hashmap of letters in first compartment
        let mut lettercount: HashMap<char, u8> = HashMap::new();
        for letter in compartment_1.chars(){
            lettercount.insert(letter, 1);
        }

        // Find duplicate
        for letter in compartment_2.chars(){
            if lettercount.contains_key(&letter){
                duplicates.push(letter);
                break;
            }
        }
    }

    // Calculate sum of priorities (a = 1, ... , z = 26, A = 27, ... , Z = 52)
    let mut sum = 0;
    for letter in duplicates.chars(){
        if letter.is_lowercase(){
            sum += letter as u32 - 'a' as u32 + 1;
        }
        else{
            sum += letter as u32 - 'A' as u32 + 27;
        }
    }

    println!("Task 1: Sum = {}", sum);

    // Part 2
    // Check common item in groups of three
    let mut lines = input.lines();
    let mut badges = String::new();

    // Read out three lines at a time, until EOF
    while let (Some(line_1), Some(line_2), Some(line_3)) = (lines.next(), lines.next(), lines.next()){
        
        // Create hastset of letters in line1
        let mut common_letters = HashMap::new();
        for letter in line_1.chars(){
            common_letters.insert(letter, 1);
        }

        // Go through next line to see if same characters are there as well
        for letter in line_2.chars(){
            if common_letters.contains_key(&letter){
                common_letters.insert(letter, 2);
            }
        }

        // Check if in all three strings
        for letter in line_3.chars(){
            if common_letters.contains_key(&letter) && common_letters[&letter] == 2{
                badges.push(letter);
                break;
            }
        }
    }

    // Calculate sum of priorities (a = 1, ... , z = 26, A = 27, ... , Z = 52)
    sum = 0;
    for letter in badges.chars(){
        if letter.is_lowercase(){
            sum += letter as u32 - 'a' as u32 + 1;
        }
        else{
            sum += letter as u32 - 'A' as u32 + 27;
        }
    }

    println!("Task 1: Sum = {}", sum);

}
