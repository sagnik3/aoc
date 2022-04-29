//copied from here :
//https://github.com/fspoettel/advent-of-code-2021/blob/master/src/lib.rs

use std::env;
use std::fs;

pub fn read_file(folder: &str, day: u8) -> String {
    let cwd = env::current_dir().unwrap();
    let filepath = cwd
        .join("src")
        .join(folder)
        .join(format!("day{:02}.txt", day));

    let f = fs::read_to_string(filepath);
    f.expect("Couldn't read input file")
}
