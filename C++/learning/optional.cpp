#include <iostream>
#include <utility>
#include <stdexcept>
#include <string>

// Custom exception for bad access
class bad_optional_access : public std::exception {
public:
    const char* what() const noexcept override {
        return "Bad optional access";
    }
};

template <typename T>
class SimpleOptional {
private:
    bool m_has_value;
    
    // Properly aligned storage for type T. 
    // We do not use "T m_value" because that would require T to be default-constructible
    // and would construct it even when the optional is empty.
    alignas(T) unsigned char m_storage[sizeof(T)];

    // Helper methods to cast our raw storage to the actual type
    T* ptr() { return reinterpret_cast<T*>(m_storage); }
    const T* ptr() const { return reinterpret_cast<const T*>(m_storage); }

public:
    // 1. Default Constructor (Empty state)
    SimpleOptional() : m_has_value(false) {}

    // 2. Value Constructors
    SimpleOptional(const T& value) : m_has_value(true) {
        new (ptr()) T(value); // Placement new: construct T in our pre-allocated memory
    }

    SimpleOptional(T&& value) : m_has_value(true) {
        new (ptr()) T(std::move(value));
    }

    // 3. Copy Constructor
    SimpleOptional(const SimpleOptional& other) : m_has_value(other.m_has_value) {
        if (other.m_has_value) {
            new (ptr()) T(*other.ptr());
        }
    }

    // 4. Move Constructor
    SimpleOptional(SimpleOptional&& other) noexcept : m_has_value(other.m_has_value) {
        if (other.m_has_value) {
            new (ptr()) T(std::move(*other.ptr()));
        }
    }

    // 5. Destructor
    ~SimpleOptional() {
        reset();
    }

    // 6. Assignment Operators
    SimpleOptional& operator=(const SimpleOptional& other) {
        if (this != &other) {
            if (m_has_value && other.m_has_value) {
                *ptr() = *other.ptr(); // Normal assignment if both have values
            } else if (!m_has_value && other.m_has_value) {
                new (ptr()) T(*other.ptr()); // Placement new if target was empty
                m_has_value = true;
            } else if (m_has_value && !other.m_has_value) {
                reset(); // Destroy our value if the source is empty
            }
        }
        return *this;
    }

    // 7. Utility Methods
    void reset() {
        if (m_has_value) {
            ptr()->~T(); // Explicitly call the destructor
            m_has_value = false;
        }
    }

    bool has_value() const noexcept {
        return m_has_value;
    }

    explicit operator bool() const noexcept {
        return m_has_value;
    }

    // 8. Accessors (Undefined behavior if empty)
    T& operator*() { return *ptr(); }
    const T& operator*() const { return *ptr(); }

    T* operator->() { return ptr(); }
    const T* operator->() const { return ptr(); }

    // 9. Safe Accessor (Throws if empty)
    T& value() {
        if (!m_has_value) throw bad_optional_access();
        return *ptr();
    }

    const T& value() const {
        if (!m_has_value) throw bad_optional_access();
        return *ptr();
    }
};

// --- Example Usage ---
int main() {
    SimpleOptional<std::string> opt_str;

    if (!opt_str) {
        std::cout << "Optional is empty.\n";
    }

    std::cout << "--- Memory Breakdown ---\n";
    std::cout << "Size of bool:                        " << sizeof(bool) << " byte(s)\n";
    std::cout << "Size of std::string:                 " << sizeof(std::string) << " bytes\n";
    
    // The total size includes the bool, the string storage, and alignment padding
    std::cout << "Total size of opt_str:               " << sizeof(opt_str) << " bytes\n";


    opt_str = SimpleOptional<std::string>("Hello, C++!");

    // Let's prove the size doesn't change when we add data
    std::cout << "\n--- After Assignment ---\n";
    
    // If you were using the full implementation from the previous message:
    // opt_str = SimpleOptional<std::string>("A massive string taking up lots of characters...");
    
    std::cout << "Total size of opt_str is STILL:      " << sizeof(opt_str) << " bytes\n";
    
    if (opt_str.has_value()) {
        std::cout << "Optional contains: " << *opt_str << "\n";
        std::cout << "String length: " << opt_str->length() << "\n";
    }

    opt_str.reset();

    try {
        std::cout << opt_str.value() << "\n"; // Will throw
    } catch (const bad_optional_access& e) {
        std::cout << "Caught exception: " << e.what() << "\n";
    }

    return 0;
}