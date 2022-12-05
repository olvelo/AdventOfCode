use std::io::prelude::*;
use std::fs;

fn main() {
    let input = fs::read_to_string("C:/git/AdventOfCode/2022/05/main/src/input.txt").unwrap();

    let mut strings = input.split("\r\n\r\n");

    let initial_state = strings.next().unwrap();
    let instructions = strings.next().unwrap();

    // Hardcode stacks...
    let mut stacks = vec![vec!['S', 'C', 'V', 'N'], vec!['Z', 'M', 'J', 'H', 'N', 'S'], vec!['M', 'C', 'T', 'G', 'J', 'N', 'D'], vec!['T', 'D', 'F', 'J', 'W', 'R', 'M'], vec!['P', 'F', 'H'], vec!['C', 'T', 'Z', 'H', 'J'], vec!['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'], vec!['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'], vec!['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']];

    for instruction in instructions.lines(){
        
        // Decode instruction
        let mut instr_splitted = instruction.split(" ");

        // Must be a way to do the below line shorter / more readable??
        let (_, number, _, stack_from, _, stack_to) = (instr_splitted.next().unwrap(), instr_splitted.next().unwrap().parse::<usize>().unwrap(), instr_splitted.next().unwrap(), instr_splitted.next().unwrap().parse::<usize>().unwrap(), instr_splitted.next().unwrap(), instr_splitted.next().unwrap().parse::<usize>().unwrap());
        
        // Move crates
        for _ in 0..number{

            let package = stacks[stack_from - 1].pop().unwrap();
            stacks[stack_to - 1].push(package);
        }
    }

    // Print out stack bottoms
    for i in 0..9{
        println!{"{}", stacks[i][stacks[i].len() - 1]}
    }


    // Task 2..   Copy pasta

    // Hardcode stacks...
    let mut stacks = vec![vec!['S', 'C', 'V', 'N'], vec!['Z', 'M', 'J', 'H', 'N', 'S'], vec!['M', 'C', 'T', 'G', 'J', 'N', 'D'], vec!['T', 'D', 'F', 'J', 'W', 'R', 'M'], vec!['P', 'F', 'H'], vec!['C', 'T', 'Z', 'H', 'J'], vec!['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'], vec!['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'], vec!['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']];

    for instruction in instructions.lines(){
        
        // Decode instruction
        let mut instr_splitted = instruction.split(" ");

        // Must be a way to do the below line shorter / more readable??
        let (_, number, _, stack_from, _, stack_to) = (instr_splitted.next().unwrap(), instr_splitted.next().unwrap().parse::<usize>().unwrap(), instr_splitted.next().unwrap(), instr_splitted.next().unwrap().parse::<usize>().unwrap(), instr_splitted.next().unwrap(), instr_splitted.next().unwrap().parse::<usize>().unwrap());
        
        let mut tempvec = vec![];

        // Move crates
        for _ in 0..number{

            let package = stacks[stack_from - 1].pop().unwrap();
            tempvec.push(package);
        }

        for _ in 0..number{
            stacks[stack_to - 1].push(tempvec[number - i - 1]);
        }
    }

    // Print out stack bottoms
    for i in 0..9{
        println!{"{}", stacks[i][stacks[i].len() - 1]}
    }

}