struct ServiceFactory;

impl ServiceFactory {
    // T is in the return type, but there are no input arguments 
    // for the compiler to inspect and infer T from.
    fn build_service<T: Default>(&self) -> T {
        T::default()
    }
}

// Two different service types
#[derive(Debug, Default)]
struct WebService;

#[derive(Debug, Default)]
struct DatabaseService;

fn main() {
    let factory = ServiceFactory;

    //  SUCCESS: Turbofish explicitly guides the compiler
    let web = factory.build_service::<WebService>();
    let db = factory.build_service::<DatabaseService>();

    println!("Created: {:?} and {:?}", web, db);

    // What is a default
    let db = DatabaseService;
    println!("Created: {:?} and ?", db);
    let db_default = DatabaseService::default();
    println!("Created default: {:?} and ?", db_default);
}