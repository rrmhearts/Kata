
struct Stack<T> {
    data: Vec<T>,
    size: usize
}

impl<T> Stack<T> {

    fn new() -> Self {
        Self {
            data: Vec::<T>::new(),
            size: 0
        }
    }

    fn is_empty(&self) -> bool {
        self.size == 0
    }

    fn push(&mut self, value: T) {
        self.data.insert(self.size, value);//push(value)
        self.size += 1;
    }

    fn pop(&mut self) -> T {
        self.size -= 1;
        self.data.remove(self.size)
    }
}


fn main() {
    let mut st = Stack::<i32>::new();

    st.push(5);
    st.push(4);
    st.push(3);

    print!("First: {}\n", st.pop());
    print!("Second: {}\n", st.pop());
    print!("Third: {}\n", st.pop());

    print!("Empty?: {}\n", st.is_empty() );

}