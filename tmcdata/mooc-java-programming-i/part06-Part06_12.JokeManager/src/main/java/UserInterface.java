import java.util.Scanner;

public class UserInterface {
    private JokeManager jokeManager;
    private Scanner scanner;

    public UserInterface(JokeManager jokeManager, Scanner scanner) {
        this.jokeManager = jokeManager;
        this.scanner = scanner;
    }
    public void start() {
        while (true) {
            System.out.println("Commands: \n1 - add a joke\n2 - draw a joke \n3 - list jokes \nX - stop");
            String input = scanner.nextLine();
            if (input.equals("X")) {
                return;
            } else if (input.equals("1")) {
                System.out.println("Write the joke to be added:");
                String input1 = scanner.nextLine();
                this.jokeManager.addJoke(input1);
            } else if (input.equals("2")) {
                System.out.println(this.jokeManager.drawJoke());
            } else if(input.equals("3")) {
                this.jokeManager.printJokes();
            }
        }
    }
}

