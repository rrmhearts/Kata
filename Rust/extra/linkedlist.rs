use std::fmt;
use std::iter::FromIterator;

/// Node struct
struct Node<T> {
    data: T,
    next: Option<Box<Node<T>>>,
}

/// Singly linked list
pub struct LinkedList<T> {
    head: Option<Box<Node<T>>>,
    size: usize,
}

impl<T> LinkedList<T> {
    /// Create a new empty list
    pub fn new() -> Self {
        LinkedList { head: None, size: 0 }
    }

    /// Returns the number of elements
    pub fn size(&self) -> usize {
        self.size
    }

    /// Check if the list is empty
    pub fn is_empty(&self) -> bool {
        self.size == 0
    }

    /// Add an element to the end
    pub fn push(&mut self, value: T) {
        self.insert(self.size, value);
    }

    /// Insert at a specific index
    pub fn insert(&mut self, index: usize, value: T) {
        if index > self.size {
            panic!("Index out of bounds");
        }

        let mut new_node = Box::new(Node { data: value, next: None });

        if index == 0 {
            new_node.next = self.head.take();
            self.head = Some(new_node);
        } else {
            let mut current = self.head.as_mut().unwrap();
            for _ in 0..index - 1 {
                current = current.next.as_mut().unwrap();
            }
            // current --> new_node --> current.next
            new_node.next = current.next.take();
            current.next = Some(new_node);
        }

        self.size += 1;
    }

    /// Remove a node at a given index and return its value
    pub fn remove(&mut self, index: usize) -> T {
        if index >= self.size {
            panic!("Index out of bounds");
        }

        let removed;
        if index == 0 {
            removed = self.head.take().unwrap();
            self.head = removed.next;
        } else {
            let mut current = self.head.as_mut().unwrap();
            for _ in 0..index - 1 {
                current = current.next.as_mut().unwrap();
            }
            removed = current.next.take().unwrap();
            current.next = removed.next;
        }

        self.size -= 1;
        removed.data
    }

    /// Get reference to value at index
    pub fn get(&self, index: usize) -> Option<&T> {
        if index >= self.size {
            return None;
        }

        let mut current = self.head.as_ref();
        for _ in 0..index {
            current = current?.next.as_ref();
        }

        /// Returns a reference to the node data
        current.map(|node| &node.data)
    }

    /// Get mutable reference to value at index
    pub fn get_mut(&mut self, index: usize) -> Option<&mut T> {
        if index >= self.size {
            return None;
        }

        let mut current = self.head.as_mut();
        for _ in 0..index {
            current = current?.next.as_mut();
        }

        current.map(|node| &mut node.data)
    }

    /// Clear the list
    pub fn clear(&mut self) {
        self.head = None;
        self.size = 0;
    }
}

/// Iterator for LinkedList
pub struct LinkedListIter<'a, T> {
    next: Option<&'a Node<T>>,
}

impl<'a, T> Iterator for LinkedListIter<'a, T> {
    type Item = &'a T;

    fn next(&mut self) -> Option<Self::Item> {
        self.next.map(|node| {
            self.next = node.next.as_deref();
            &node.data
        })
    }
}

impl<T> LinkedList<T> {
    /// Get an iterator over references to the items
    pub fn iter(&self) -> LinkedListIter<'_, T> {
        LinkedListIter {
            next: self.head.as_deref(),
        }
    }
}

/// Debug printing
/// `println!("List: {:?}", list);` // [10, 15, 20]
impl<T: fmt::Debug> fmt::Debug for LinkedList<T> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let values: Vec<_> = self.iter().collect();
        f.debug_list().entries(values).finish()
    }
}

/// Allow collecting from iterator
impl<T> FromIterator<T> for LinkedList<T> {
    // Create a linked list from an iterator
    fn from_iter<I: IntoIterator<Item = T>>(iter: I) -> Self {
        let mut list = LinkedList::new();
        for item in iter {
            list.push(item);
        }
        list
    }
}

fn main() {
    let mut list = LinkedList::new();
    list.push(10);
    list.push(20);
    list.insert(1, 15);
    println!("List: {:?}", list); // [10, 15, 20]

    println!("Size: {}", list.size()); // 3
    println!("Item at index 1: {:?}", list.get(1)); // Some(15)

    let removed = list.remove(1);
    println!("Removed: {}", removed); // 15
    println!("List after remove: {:?}", list); // [10, 20]

    for val in list.iter() {
        println!("Value: {}", val);
    }
}

// The Standard library includes a linked list as follows:
// use std::collections::LinkedList;

// fn main() {
//     let mut list = LinkedList::new();
//     list.push_back(1);
//     list.push_back(2);
//     list.push_front(0);
//     println!("{:?}", list); // [0, 1, 2]

//     list.pop_front();
//     list.pop_back();
//     println!("{:?}", list); // [1]
// }
