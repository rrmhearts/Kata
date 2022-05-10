
class Dog {
    name: string;
    constructor(name: string) {
        this.name = name;
    }

    bark(): void {
        console.log(`${this.name} barks!`)
    }
}

export default Dog