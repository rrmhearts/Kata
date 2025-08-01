fn display_stacks(peg_a_name: &str, peg_a: &[i32], peg_b_name: &str, peg_b: &[i32], peg_c_name: &str, peg_c: &[i32]) {
    print!("{}: ", peg_a_name);
    for item in peg_a {
        print!("{} ", item);
    }
    print!("  {}: ", peg_b_name);
    for item in peg_b {
        print!("{} ", item);
    }
    print!("  {}: ", peg_c_name);
    for item in peg_c {
        print!("{} ", item);
    }
    println!();
}

fn towers(n: usize, source_name: &str, source: &mut Vec<i32>, aux_name: &str, aux: &mut Vec<i32>, dest_name: &str, dest: &mut Vec<i32>) {
    if n == 1 {
        let disk = source.pop().unwrap();
        dest.push(disk);
        println!("Move disk {} from {} to {}", disk, source_name, dest_name);
        display_stacks("Peg A", &source, "Peg B", &aux, "Peg C", &dest);
    } else {
        // Move n-1 disks from source to auxiliary, using destination as temporary
        towers(n - 1, source_name, source, dest_name, dest, aux_name, aux);

        // Move the largest disk from source to destination
        let disk = source.pop().unwrap();
        dest.push(disk);
        println!("Move disk {} from {} to {}", disk, source_name, dest_name);
        display_stacks("Peg A", &source, "Peg B", &aux, "Peg C", &dest);

        // Move n-1 disks from auxiliary to destination, using source as temporary
        towers(n - 1, aux_name, aux, source_name, source, dest_name, dest);
    }
}

fn main() {
    let mut stack1 = vec![3, 2, 1];
    let mut stack2: Vec<i32> = vec![];
    let mut stack3: Vec<i32> = vec![];

    println!("Towers of Hanoi!");
    display_stacks("Peg A", &stack1, "Peg B", &stack2, "Peg C", &stack3);

    towers(stack1.len(), "Peg A", &mut stack1, "Peg B", &mut stack2, "Peg C", &mut stack3);

    println!("\nFinal state:");
    display_stacks("Peg A", &stack1, "Peg B", &stack2, "Peg C", &stack3);
}
