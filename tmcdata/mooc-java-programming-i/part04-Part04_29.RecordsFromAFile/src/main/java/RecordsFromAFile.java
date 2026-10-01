
import java.io.IOException;
import java.nio.file.Paths;
import java.util.Scanner;

public class RecordsFromAFile {

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        String fileName = scanner.nextLine();
        Scanner fileScanner = new Scanner(Paths.get(fileName ));
        while(fileScanner.hasNextLine()){
            String line = fileScanner.nextLine();
            String[] parts = line.split(",");
            int age = Integer.parseInt(parts[1].trim());
            if(age == 1){
                System.out.println(parts[0].trim() + ", age: " + age + " year");
            }
            else{
                System.out.println(parts[0].trim() + ", age: " + age + " years");
            }

        }

    }
}
