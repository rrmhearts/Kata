
struct Primes<u32> {
    data: Vec<u32>,
    size: usize
}

impl Primes<u32> {

    fn new() -> Self {
        Self {
            data: Vec::<u32>::new(),
            size: 0
        }
    }

    fn not_prime(&self, value: u32) -> bool {
        for i in self.data.iter() {
            // print!("{}, {}\n", value, i);
            if value % i == 0 {
                return true;
            }
        }
        false
    }

    fn next(&mut self) -> u32 {
        if self.data.is_empty() {
            self.data.push(2);
            return 2;
        }
        let mut counter: u32 = *self.data.last().unwrap();
        // while counter 
        counter += if counter %2==0 {1} else {2};
        while self.not_prime(counter) {
            counter+=1;
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
}