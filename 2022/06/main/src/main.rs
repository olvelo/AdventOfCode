use std::fs;

fn main() {
    let input = fs::read_to_string("C:/git/AdventOfCode/2022/06/main/src/input.txt").unwrap();

    // Look for a sequence of unique letters, with number of letters given below. Set up index to track which letter this occurs at, and a vector for the letter buffer
    let unique_required = 14;
    let mut index = 0;
    let mut myletters = vec![];

    // Loop over all letters
    for letter in input.chars(){

        // Fill buffer at the start, if we have less letters than required length
        if myletters.len() < unique_required{
            myletters.push(letter);
        }

        else{

            // Check if unique letters only, by sorting and removing duplicates from our array copy, and comparing their length
            let mut lettercopy = myletters.to_vec();
            lettercopy.sort();
            lettercopy.dedup();

            if lettercopy.len() == myletters.len(){
                println!("Index where we have a unique string of length {}: {}", unique_required, index);
                break;
            }

            // If not unique, fill buffer with new char and remove the one at the back
            else{
                myletters.push(letter);
                myletters.remove(0);
            }
        }
        // Remember to increase index
        index = index + 1;
    }
}