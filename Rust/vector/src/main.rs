/// A custom vector implementation backed by a fixed-size array on the stack.
///
/// `T` is the generic type of the elements stored in the vector.
/// `N` is a compile-time constant representing the maximum capacity of the vector.
#[derive(Debug)]
pub struct MyVec<T, const N: usize> {
    /// The internal array to store data. Using `Option<T>` allows us to
    /// represent empty slots, which is crucial for `pop` and initialization.
    data: [Option<T>; N],
    /// The current number of elements in the vector. This must always be
    /// less than or equal to the capacity `N`.
    len: usize,
}

/// Implementation block for `MyVec`.
///
/// This block contains all the methods associated with our custom vector type.
impl<T, const N: usize> MyVec<T, N> {
    /// Creates a new, empty `MyVec`.
    ///
    /// The vector is initialized with a capacity of `N`, but its initial
    /// length is zero. The internal array is filled with `None`.
    ///
    /// # Returns
    ///
    /// A new `MyVec` instance.
    pub fn new() -> Self {
        // We need to initialize an array of `Option<T>`. The `const { None }`
        // syntax creates an array where every element is `None`. This is
        // a clean way to initialize the array without requiring `T` to be `Copy`.
        Self {
            data: [const { None }; N],
            len: 0,
        }
    }

    /// Returns the number of elements in the vector.
    ///
    /// # Returns
    ///
    /// The current length of the vector as a `usize`.
    pub fn len(&self) -> usize {
        self.len
    }

    /// Returns `true` if the vector contains no elements.
    ///
    /// # Returns
    ///
    /// A boolean value indicating whether the vector is empty.
    pub fn is_empty(&self) -> bool {
        self.len == 0
    }

    /// Appends an element to the back of the vector.
    ///
    /// If the vector is already at its maximum capacity (`N`), this
    /// method will return an error.
    ///
    /// # Arguments
    ///
    /// * `value` - The element to add to the vector.
    ///
    /// # Returns
    ///
    /// * `Ok(())` if the push was successful.
    /// * `Err(&'static str)` if the vector is full.
    pub fn push(&mut self, value: T) -> Result<(), &'static str> {
        if self.len >= N {
            // The vector is full, so we cannot add another element.
            return Err("Vector is full");
        }
        // Place the new value at the current end of the vector.
        self.data[self.len] = Some(value);
        // Increment the length to reflect the new element.
        self.len += 1;
        Ok(())
    }

    /// Removes the last element from the vector and returns it.
    ///
    /// If the vector is empty, this method returns `None`.
    ///
    /// # Returns
    ///
    /// An `Option<T>` containing the last element, or `None` if the
    /// vector is empty.
    pub fn pop(&mut self) -> Option<T> {
        if self.is_empty() {
            // Nothing to pop.
            return None;
        }
        // Decrement the length first. `self.len` now points to the
        // element we want to remove.
        self.len -= 1;
        // `Option::take()` replaces the `Some(value)` at the given index
        // with `None` and returns the `Some(value)`. This is perfect for `pop`.
        self.data[self.len].take()
    }

    /// Returns a reference to an element at a given index.
    ///
    /// # Arguments
    ///
    /// * `index` - The index of the element to retrieve.
    ///
    /// # Returns
    ///
    /// An `Option<&T>` containing a reference to the element, or `None` if
    /// the index is out of bounds.
    pub fn get(&self, index: usize) -> Option<&T> {
        if index >= self.len {
            // Index is out of the valid range of elements.
            return None;
        }
        // `Option::as_ref()` converts `&Option<T>` to `Option<&T>`,
        // which is what we want to return.
        self.data[index].as_ref()
    }
}

fn main() {
    // Create a new vector with a capacity of 5 that holds integers.
    let mut my_vec = MyVec::<i32, 5>::new();
    println!("Created a new vector: {:?}", my_vec);
    println!("Is it empty? {}", my_vec.is_empty());
    println!("---");

    // Push some elements into the vector.
    println!("Pushing 10, 20, 30...");
    my_vec.push(10).unwrap();
    my_vec.push(20).unwrap();
    my_vec.push(30).unwrap();

    println!("Vector state: {:?}", my_vec);
    println!("Current length: {}", my_vec.len());
    println!("Is it empty? {}", my_vec.is_empty());
    println!("---");

    // Use `get` to access elements.
    println!("Element at index 1: {:?}", my_vec.get(1)); // Should be Some(20)
    println!("Element at index 4: {:?}", my_vec.get(4)); // Should be None
    println!("---");


    // Pop elements from the vector.
    println!("Popping an element: {:?}", my_vec.pop()); // Should be Some(30)
    println!("Vector state after pop: {:?}", my_vec);
    println!("Popping another element: {:?}", my_vec.pop()); // Should be Some(20)
    println!("Vector state after pop: {:?}", my_vec);
    println!("---");

    // Push until the vector is full.
    println!("Filling the vector...");
    my_vec.push(40).unwrap();
    my_vec.push(50).unwrap();
    my_vec.push(60).unwrap();
    my_vec.push(70).unwrap();
    println!("Vector state when full: {:?}", my_vec);

    // Try to push to a full vector.
    let push_result = my_vec.push(80);
    println!("Trying to push to a full vector: {:?}", push_result); // Should be Err
    println!("---");

    // Pop all remaining elements.
    println!("Emptying the vector...");
    println!("Popped: {:?}", my_vec.pop());
    println!("Popped: {:?}", my_vec.pop());
    println!("Popped: {:?}", my_vec.pop());
    println!("Popped: {:?}", my_vec.pop());
    println!("Popped: {:?}", my_vec.pop());

    // Try to pop from an empty vector.
    println!("Trying to pop from an empty vector: {:?}", my_vec.pop()); // Should be None
    println!("Final state: {:?}", my_vec);
    println!("Is it empty? {}", my_vec.is_empty());
}
