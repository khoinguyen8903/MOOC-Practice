
import java.util.Scanner;

public class DogAttributes {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String name = scanner.nextLine();
        String breed = scanner.nextLine();
        int age = Integer.valueOf(scanner.nextLine());
        Dog dog = new Dog(name, breed, age);
        System.out.println(dog.getName());
        System.out.println(dog.getBreed());
        System.out.println(dog.getAge());
    }
}
