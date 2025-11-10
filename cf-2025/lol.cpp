#include <iostream>

class Dog
{
private:
    std::string name {};
public:
    Dog(std::string name) : name{name} {}

    void bark() {
        std::cout << name << " says woof\n";
    }
};

int main(){
    std::cout << "Hello\n";
    Dog french = Dog("Johnny");
    french.bark();
    return 0;
}