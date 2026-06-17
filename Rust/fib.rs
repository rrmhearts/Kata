

fn fibonnocci(number: i32) -> u32 {
    
    let mut a: u32 = 0;
    let mut b: u32 = 1;

    if number == 0 {
        return 1;
    }

    for _ in 0..number {
        let temp = b;
        b = a + b;
        a = temp;
    }
    b
    /// This also works.
    // if number <= 0 {
    //     1
    // } else {
    //     fibonnocci(number-1) + fibonnocci(number-2)
    // }
}

fn main() {
    //let number : u32 = 0;

    for number in 0..20 {
        println!("The {} fibonnocci number is {}", number, fibonnocci(number));

    }
}