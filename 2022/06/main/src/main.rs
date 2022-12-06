use std::fs;
use std::collections::HashSet;

fn main() {
    let input = fs::read_to_string("C:/git/AdventOfCode/2022/06/main/src/input.txt").unwrap();

    // Look for a sequence of unique letters, with number of letters given below
    let unique_required = 14;
    let mut myletters = vec![];

    for (index, letter) in input.chars().enumerate(){
        myletters.push(letter);

        // Create a hash set of the buffer length, if we have enough letters
        let lettercopy: HashSet<&char> = if index >= unique_required {HashSet::from_iter(myletters[index - unique_required..index].iter())} else {HashSet::new()};
        
        if lettercopy.len() == unique_required{
            println!("Index where we have a unique string of length {}: {}", unique_required, index);
            break;
        }
    }
}