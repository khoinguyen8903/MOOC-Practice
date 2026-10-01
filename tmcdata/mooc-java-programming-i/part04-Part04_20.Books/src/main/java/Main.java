
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // implement here the program that allows the user to enter 
        // book information and to examine them
        ArrayList<Book> books = new ArrayList<>();
        while(true){
            System.out.println("Title: ");
            String title = scanner.nextLine();
            if (title.isEmpty()){
                break;
            }
            System.out.println("Pages: ");
            int pages = Integer.valueOf(scanner.nextLine());
            System.out.println("Publication year: ");
            int year = Integer.valueOf(scanner.nextLine());
            Book book = new Book(title, pages, year);
            books.add(book);
        }
        System.out.println("What information will be printed?");
        String command = scanner.nextLine();
        if(command.equals("everything")){
            for (Book book : books){
                System.out.println(book);
            }
        } else if (command.equals("name")) {
            for (Book book : books){
                System.out.println(book.getTitle());
            }
        }

    }
}
