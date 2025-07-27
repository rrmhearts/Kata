
fn display_stacks(v: &[i32], v2: &[i32], v3: &[i32]) {
    for item in v { print!("{}", item); }
    print!(" ");
    for item in v2 { print!("{}", item); }
    print!(" ");
    for item in v3 { print!("{}", item); }
    println!();
}

fn towers(n: usize, source: &mut Vec<i32>, aux: &mut Vec<i32>, dest: &mut Vec<i32>, toSpare: bool, original: bool) {
    if !original {
        if toSpare {
            println!("to spare");
            display_stacks(&source, &dest, &aux);
        } else {
            println!("to dest");
            display_stacks(&aux, &source, &dest);
        }
    }
    if n == 1 {
        let disk = source.pop().unwrap();
        dest.push(disk);
    } else {
        // move m-1 disks to spare peg
        towers(n-1, source, dest, aux, true, false);
        // now we can move the largest disk to dest peg.
        let disk = source.pop().unwrap();
        dest.push(disk);
        // now move the aux disks to the destination.
        towers(n-1, aux, source, dest, false, false);
    }
}

fn main() {
    let mut stack1 = vec![3, 2, 1];
    let mut stack2: Vec<i32> = vec![];
    let mut stack3: Vec<i32> = vec![];
    println!("Towers of Hanoi!");

    display_stacks(&stack1, &stack2, &stack3);
    towers(stack1.len(), &mut stack1, &mut stack2, &mut stack3, false, true);
    display_stacks(&stack1, &stack2, &stack3);
}