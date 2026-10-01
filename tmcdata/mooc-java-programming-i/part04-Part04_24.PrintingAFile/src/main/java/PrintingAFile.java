
import java.nio.file.Paths;
import java.util.Scanner;

public class PrintingAFile {

    public static void main(String[] args) {
        try (Scanner fileScanner = new Scanner(Paths.get("data.txt"))) {
            while (fileScanner.hasNextLine()) {
                System.out.println(fileScanner.nextLine());
            }
        } catch (Exception exception) {
            System.out.println("Error reading the file.");
        }
    }
}
