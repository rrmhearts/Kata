
struct Queue {
    data: Vec<char>
}

impl Queue {
    const NAME: &str = "Sorted Queue";
    pub fn push(&mut self, c: char) {
        self.data.push(c);
    }

    fn pop(&mut self) -> Option<char> {
        if self.data.is_empty() {
            return None;
        }

        self.data.sort();

        self.data.pop() //Some('a')
    }
}


fn main() {

    let mut q = Queue { data: Vec::new() };
    print!("{:?}", Queue::NAME);
    q.push('9');
    q.push('8');
    q.push('7');
    q.push('a');
    q.push('9');

    print!("{:?}", q.data);

    q.pop();
    print!("{:?}", q.data);

    q.pop();
    print!("{:?}", q.data);
}