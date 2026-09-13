import java.util.Scanner;

public class PersonalDetails {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sumOfYears = 0;
        int count = 0;
        String longestName = "";
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            String[] pieces = input.split(",");
            String name = pieces[0];
            int year = Integer.valueOf(pieces[1]);
            
            if (name.length() > longestName.length()) {
                longestName = name;
            }
            sumOfYears += year;
            count++;
        }
        System.out.println("Longest name: " + longestName);
        System.out.println("Average of the birth years: " + (1.0 * sumOfYears / count));
    }
}
