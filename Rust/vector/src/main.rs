use std::alloc::{self, Layout};
use std::ptr::{self, NonNull};

/// A custom, growable vector implementation backed by a heap-allocated array.
///
/// This vector, `MyVec<T>`, is a simplified version of `std::vec::Vec<T>`.
/// It manages a contiguous block of memory on the heap and will automatically
/// reallocate its data to a larger block when it runs out of capacity.
#[derive(Debug)]
pub struct MyVec<T> {
    /// A non-null pointer to the start of the heap-allocated buffer.
    ptr: NonNull<T>,
    /// The number of elements currently stored in the vector.
    len: usize,
    /// The total number of elements that can be stored in the current allocation.
    capacity: usize,
}

/// Implementation block for `MyVec`.
impl<T> MyVec<T> {
    /// Creates a new, empty `MyVec`.
    ///
    /// No memory is allocated until the first element is pushed.
    pub fn new() -> Self {
        Self {
            // Use a dangling pointer as a placeholder for a zero-sized allocation.
            ptr: NonNull::dangling(),
            len: 0,
            capacity: 0,
        }
    }

    /// Returns the number of elements in the vector.
    pub fn len(&self) -> usize {
        self.len
    }

    /// Returns `true` if the vector contains no elements.
    pub fn is_empty(&self) -> bool {
        self.len == 0
    }

    /// Private helper method to grow the vector's capacity.
    ///
    /// This method handles reallocating the memory buffer to a larger size
    /// when the vector is full. The new capacity is typically double the old one.
    fn grow(&mut self) {
        // Determine the new capacity. If the current capacity is 0, start with 4.
        // Otherwise, double the current capacity.
        let new_capacity = if self.capacity == 0 { 4 } else { self.capacity * 2 };

        // Define the memory layout for the new allocation.
        let new_layout = Layout::array::<T>(new_capacity).unwrap();
        
        let new_ptr = if self.capacity == 0 {
            // If there's no old allocation, allocate a new block.
            unsafe { alloc::alloc(new_layout) }
        } else {
            // If there is an old allocation, reallocate it to the new size.
            let old_layout = Layout::array::<T>(self.capacity).unwrap();
            unsafe { alloc::realloc(self.ptr.as_ptr() as *mut u8, old_layout, new_layout.size()) }
        };

        // Update the vector's pointer and capacity. `NonNull::new` handles the
        // case where allocation fails (which would return a null pointer and panic).
        self.ptr = match NonNull::new(new_ptr as *mut T) {
            Some(p) => p,
            None => alloc::handle_alloc_error(new_layout),
        };
        self.capacity = new_capacity;
    }

    /// Appends an element to the back of the vector.
    ///
    /// If the vector is at maximum capacity, it will automatically grow.
    pub fn push(&mut self, value: T) {
        if self.len == self.capacity {
            self.grow();
        }

        // SAFETY: We've ensured there is enough capacity, so `self.len` is a
        // valid, in-bounds index to write to.
        unsafe {
            ptr::write(self.ptr.as_ptr().add(self.len), value);
        }
        self.len += 1;
    }

    /// Removes the last element from the vector and returns it.
    ///
    /// Returns `None` if the vector is empty.
    pub fn pop(&mut self) -> Option<T> {
        if self.len == 0 {
            None
        } else {
            self.len -= 1;
            // SAFETY: `self.len` was just decremented, so it points to a valid,
            // initialized element that we can now safely read from.
            unsafe {
                Some(ptr::read(self.ptr.as_ptr().add(self.len)))
            }
        }
    }

    /// Inserts an element at a specific index.
    ///
    /// All elements at and after the insertion index are shifted to the right.
    /// This method panics if `index > self.len`.
    pub fn insert(&mut self, index: usize, value: T) {
        assert!(index <= self.len, "insertion index out of bounds");
        if self.len == self.capacity {
            self.grow();
        }

        // SAFETY: We've checked the bounds. The pointer `p` is valid for reads.
        // `ptr::copy` correctly handles overlapping memory regions, shifting all
        // elements from `index` onwards one position to the right.
        unsafe {
            let p = self.ptr.as_ptr().add(index);
            ptr::copy(p, p.add(1), self.len - index);
            ptr::write(p, value);
        }
        self.len += 1;
    }

    /// Returns a reference to an element at a given index.
    ///
    /// Returns `None` if the index is out of bounds.
    pub fn get(&self, index: usize) -> Option<&T> {
        if index >= self.len {
            None
        } else {
            // SAFETY: We've checked that the index is in bounds, so we can
            // safely create a reference to the element.
            unsafe {
                Some(&*self.ptr.as_ptr().add(index))
            }
        }
    }
}

/// The `Drop` trait is crucial for our manual memory management.
/// It ensures that when a `MyVec` goes out of scope, its allocated
/// memory is properly deallocated.
impl<T> Drop for MyVec<T> {
    fn drop(&mut self) {
        if self.capacity != 0 {
            // Drop all the elements in the vector by popping them. This ensures
            // each element's own `drop` implementation is called.
            while self.pop().is_some() {}

            // Get the layout of the memory we allocated.
            let layout = Layout::array::<T>(self.capacity).unwrap();
            // SAFETY: The pointer was allocated by us with this layout, so it's
            // safe to deallocate it now that it's empty.
            unsafe {
                alloc::dealloc(self.ptr.as_ptr() as *mut u8, layout);
            }
        }
    }
}


fn main() {
    // Create a new vector. It starts with 0 capacity.
    let mut my_vec = MyVec::<i32>::new();
    println!("Created a new vector: {:?}", my_vec);
    println!("---");

    // Push elements. This will trigger the `grow` method.
    println!("Pushing 10, 20, 30, 40, 50...");
    my_vec.push(10);
    my_vec.push(20);
    my_vec.push(30);
    my_vec.push(40);
    my_vec.push(50); // This push will trigger a resize from 4 to 8.

    println!("Vector state after pushing: {:?}", my_vec);
    println!("Element at index 3: {:?}", my_vec.get(3)); // Should be Some(40)
    println!("---");

    // Pop an element.
    println!("Popping an element: {:?}", my_vec.pop()); // Should be Some(50)
    println!("Vector state after pop: {:?}", my_vec);
    println!("---");

    // Insert an element.
    println!("Inserting 99 at index 1...");
    my_vec.insert(1, 99);
    println!("Vector state after insert: {:?}", my_vec);
    println!("Element at index 1: {:?}", my_vec.get(1)); // Should be Some(99)
    println!("Element at index 2: {:?}", my_vec.get(2)); // Should be Some(20)
    println!("---");

    // Empty the vector.
    println!("Emptying the vector...");
    while let Some(val) = my_vec.pop() {
        println!("Popped: {}", val);
    }
    
    println!("Final state: {:?}", my_vec);
    println!("Is it empty? {}", my_vec.is_empty());
}
