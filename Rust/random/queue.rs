
struct Queue<T> {
    pub data: Vec<T>
}

impl<T> Queue<T> {
    const NAME: &str = "Sorted Queue";

    pub fn new() {
        struct Queue { data: Vec!() }
    }
    pub fn push(&mut self, c: T) {
        self.data.push(c);
    }

    fn pop(&mut self) -> Option<T> {
        if self.data.is_empty() {
            return None;
        }

        // self.data.sort();

        self.data.pop() //Some('a')
    }
}

fn main() {

    let mut q = Queue::new();
    print!("{:?}", Queue::NAME);
    q.push(9);
    q.push(8);
    q.push(7);
    q.push(6);
    q.push(9);

    print!("{:?}", q.data);

    q.pop();
    print!("{:?}", q.data);

    q.pop();
    print!("{:?}", q.data);
}