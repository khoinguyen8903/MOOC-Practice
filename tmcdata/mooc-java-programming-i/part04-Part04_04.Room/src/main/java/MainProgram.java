
import java.util.Scanner;

public class MainProgram {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String code = scanner.nextLine();
        int seats = Integer.valueOf(scanner.nextLine());
        Room room = new Room(code, seats);
        System.out.println(room.getCode());
        System.out.println(room.getSeats());
    }

}
