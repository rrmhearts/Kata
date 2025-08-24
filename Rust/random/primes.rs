
struct Primes {
    data: Vec<u32>,
    size: usize
}

impl Primes {

    fn new() -> Self {
        Self {
            data: Vec::<u32>::new(),
            size: 0
        }
    }

    fn is_prime(&self, value: u32) -> bool {
        let largest_divisor = 
            (value as f64).sqrt().ceil() as u32;
        for i in self.data.iter() {
            if *i > largest_divisor {
                break
            }
            if value % i == 0 {
                return false;
            }
        }
        return true;
    }

    fn next_after(&mut self, value: u32) -> u32 {
        for _ in 1..value {
            let latest = self.next();
            if latest > value {
                return latest
            }
        }
        return 0;
    }

    fn next(&mut self) -> u32 {
        if self.data.is_empty() {
            self.data.push(2);
            return 2;
        }
        let mut counter: u32 = *self.data.last().unwrap();
        counter += if counter %2==0 {1} else {2};
        while !self.is_prime(counter) {
            counter+=2;
        }
        self.data.push(counter);
        self.size += 1;

        counter
    }
}

fn main() {
    let mut st = Primes::new();

    for _ in 1..20 {
        print!("Next: {}\n", st.next());
    }
    print!("Next after 1,000,000: {}", st.next_after(1000000))
}