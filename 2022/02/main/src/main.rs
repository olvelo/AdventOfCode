use std::fs::File;
use std::io::prelude::*;

fn read_input() -> String{
    let mut file = File::open("C:/git/AdventOfCode/2022/02/main/src/input.txt").unwrap();
    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();
    return data;
}

fn add_score_task1(hand_opponent: &str, hand_player: &str, total_score: &mut u32){
    let hand_opponent = hand_opponent.chars().next().unwrap();
    let hand_player = hand_player.chars().next().unwrap();
    *total_score += hand_player as u32 - 'W' as u32;

    *total_score += match hand_player{
        'X' => match hand_opponent{
            'A' => 3,
            'B' => 0,
            'C' => 6,
            _other => 0,
        },
        'Y' => match hand_opponent{
            'A' => 6,
            'B' => 3,
            'C' => 0,
            _other => 0,
        },
        'Z' => match hand_opponent{
            'A' => 0,
            'B' => 6,
            'C' => 3,
            _other => 0,
        },
        _other => 0,
    }
}

fn add_score_task2(hand_opponent: &str, wanted_outcome: &str, total_score: &mut u32){
    let hand_opponent = hand_opponent.chars().next().unwrap();
    let wanted_outcome = wanted_outcome.chars().next().unwrap();

    *total_score += match wanted_outcome{
        'X' => match hand_opponent{
            'A' => 3,
            'B' => 1,
            'C' => 2,
            _other => 0,
        },
        'Y' => match hand_opponent{
            'A' => 4,
            'B' => 5,
            'C' => 6,
            _other => 0,
        },
        'Z' => match hand_opponent{
            'A' => 8,
            'B' => 9,
            'C' => 7,
            _other => 0,
        },
        _other => 0,
    };

}

fn main() {
    let input = read_input();
    let lines = input.lines();

    let mut total_score = 0;
    for line in lines{
        let mut line_splitted = line.split(" ");
        let hand_opponent = line_splitted.next().unwrap();
        let hand_player = line_splitted.next().unwrap();
        add_score_task1(hand_opponent, hand_player, &mut total_score);
    }
    println!("Task 1: Total score is {}", total_score);

    let input = read_input();
    let lines = input.lines();

    total_score = 0;
    for line in lines{
        let mut line_splitted = line.split(" ");
        let hand_opponent = line_splitted.next().unwrap();
        let wanted_outcome = line_splitted.next().unwrap();
        add_score_task2(hand_opponent, wanted_outcome, &mut total_score);
    }
    println!("Task 2: Total score is {}", total_score);
}
