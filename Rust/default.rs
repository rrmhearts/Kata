
//#[derive(Default, Debug)] // Use default implementation of Default trait
#[derive(Debug)]
struct ConnectionSettings {
    host: String,
    port: u16,
    timeout: u32,
}

// Create our own implementation for Default trait
impl Default for ConnectionSettings {
    fn default() -> Self {
        ConnectionSettings {
            host: String::from("localhost"),
            port: 8080,
            timeout: 30,
        }
    }
}

fn main() {
    // Generates the default struct
    let settings = ConnectionSettings::default(); 
    println!("{:?}", settings); 
    // Output: ConnectionSettings { host: "", port: 0, timeout: 0 }

    let custom_settings = ConnectionSettings {
        port: 8080,
        ..Default::default() // The rest of the fields get the Default values
    };
    println!("{:?}", custom_settings);
}

