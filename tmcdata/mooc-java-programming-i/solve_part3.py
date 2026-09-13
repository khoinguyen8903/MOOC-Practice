import os
import glob

base = r'D:\TMCProjects\tmcdata\mooc-java-programming-i'

solutions = {
    "ThirdElement.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class ThirdElement {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            list.add(input);
        }
        System.out.println(list.get(2));
    }
}
""",
    "SecondPlusThird.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class SecondPlusThird {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<>();
        while (true) {
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            }
            numbers.add(number);
        }
        System.out.println(numbers.get(1) + numbers.get(2));
    }
}
""",
    "IoobProgram.java": """
import java.util.ArrayList;

public class IoobProgram {
    public static void main(String[] args) {
        ArrayList<String> lines = new ArrayList<>();
        lines.add("Never has a man influenced physics so profoundly as Niels Bohr in the early 1900's");
        lines.add("Going back to this time period, little was known about atomic structure; Bohr set out");
        System.out.println(lines.get(100));
    }
}
""",
    "ListSize.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class ListSize {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            list.add(input);
        }
        System.out.println("In total: " + list.size());
    }
}
""",
    "LastInList.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class LastInList {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            list.add(input);
        }
        System.out.println(list.get(list.size() - 1));
    }
}
""",
    "FirstAndLast.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class FirstAndLast {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            list.add(input);
        }
        System.out.println(list.get(0));
        System.out.println(list.get(list.size() - 1));
    }
}
""",
    "RememberTheseNumbers.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class RememberTheseNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<>();
        while (true) {
            int luku = Integer.valueOf(scanner.nextLine());
            if (luku == -1) {
                break;
            }
            numbers.add(luku);
        }
        for (int i : numbers) {
            System.out.println(i);
        }
    }
}
""",
    "OnlyTheseNumbers.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class OnlyTheseNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<>();
        while (true) {
            int number = Integer.valueOf(scanner.nextLine());
            if (number == -1) {
                break;
            }
            numbers.add(number);
        }
        System.out.print("From where? ");
        int start = Integer.valueOf(scanner.nextLine());
        System.out.print("To where? ");
        int end = Integer.valueOf(scanner.nextLine());
        for (int i = start; i <= end; i++) {
            System.out.println(numbers.get(i));
        }
    }
}
""",
    "GreatestInList.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class GreatestInList {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        while (true) {
            int input = Integer.valueOf(scanner.nextLine());
            if (input == -1) {
                break;
            }
            list.add(input);
        }
        int greatest = list.get(0);
        for (int i : list) {
            if (i > greatest) {
                greatest = i;
            }
        }
        System.out.println("The greatest number: " + greatest);
    }
}
""",
    "IndexOf.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class IndexOf {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        while (true) {
            int input = Integer.valueOf(scanner.nextLine());
            if (input == -1) {
                break;
            }
            list.add(input);
        }
        System.out.print("Search for? ");
        int search = Integer.valueOf(scanner.nextLine());
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) == search) {
                System.out.println(search + " is at index " + i);
            }
        }
    }
}
""",
    "IndexOfSmallest.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class IndexOfSmallest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        while (true) {
            int input = Integer.valueOf(scanner.nextLine());
            if (input == 9999) {
                break;
            }
            list.add(input);
        }
        int smallest = list.get(0);
        for (int i : list) {
            if (i < smallest) {
                smallest = i;
            }
        }
        System.out.println("Smallest number: " + smallest);
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) == smallest) {
                System.out.println("Found at index: " + i);
            }
        }
    }
}
""",
    "SumOfAList.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class SumOfAList {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        while (true) {
            int input = Integer.valueOf(scanner.nextLine());
            if (input == -1) {
                break;
            }
            list.add(input);
        }
        int sum = 0;
        for (int i : list) {
            sum += i;
        }
        System.out.println("Sum: " + sum);
    }
}
""",
    "AverageOfAList.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class AverageOfAList {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        while (true) {
            int input = Integer.valueOf(scanner.nextLine());
            if (input == -1) {
                break;
            }
            list.add(input);
        }
        int sum = 0;
        for (int i : list) {
            sum += i;
        }
        System.out.println("Average: " + (1.0 * sum / list.size()));
    }
}
""",
    "OnTheList.java": """
import java.util.ArrayList;
import java.util.Scanner;

public class OnTheList {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            list.add(input);
        }
        System.out.print("Search for? ");
        String search = scanner.nextLine();
        if (list.contains(search)) {
            System.out.println(search + " was found!");
        } else {
            System.out.println(search + " was not found!");
        }
    }
}
""",
    "PrintInRange.java": """
import java.util.ArrayList;

public class PrintInRange {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(3);
        numbers.add(2);
        numbers.add(6);
        numbers.add(-1);
        numbers.add(5);
        numbers.add(1);
        printNumbersInRange(numbers, 0, 5);
    }
    public static void printNumbersInRange(ArrayList<Integer> numbers, int lowerLimit, int upperLimit) {
        for (int number : numbers) {
            if (number >= lowerLimit && number <= upperLimit) {
                System.out.println(number);
            }
        }
    }
}
""",
    "Sum.java": """
import java.util.ArrayList;

public class Sum {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(3);
        numbers.add(2);
        numbers.add(6);
        numbers.add(-1);
        System.out.println(sum(numbers));
    }
    public static int sum(ArrayList<Integer> numbers) {
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return sum;
    }
}
""",
    "RemoveLast.java": """
import java.util.ArrayList;

public class RemoveLast {
    public static void main(String[] args) {
        ArrayList<String> strings = new ArrayList<>();
        strings.add("First");
        strings.add("Second");
        strings.add("Third");
        removeLast(strings);
        System.out.println(strings);
    }
    public static void removeLast(ArrayList<String> strings) {
        if (!strings.isEmpty()) {
            strings.remove(strings.size() - 1);
        }
    }
}
""",
    "Swap.java": """
import java.util.Scanner;

public class Swap {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[5];
        array[0] = 1;
        array[1] = 3;
        array[2] = 5;
        array[3] = 7;
        array[4] = 9;

        int index = 0;
        while (index < array.length) {
            System.out.println(array[index]);
            index++;
        }
        System.out.println("");

        System.out.println("Indices to swap:");
        int idx1 = Integer.valueOf(scanner.nextLine());
        int idx2 = Integer.valueOf(scanner.nextLine());
        int temp = array[idx1];
        array[idx1] = array[idx2];
        array[idx2] = temp;

        System.out.println("");
        index = 0;
        while (index < array.length) {
            System.out.println(array[index]);
            index++;
        }
    }
}
""",
    "IndexWasNotFound.java": """
import java.util.Scanner;

public class IndexWasNotFound {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[10];
        array[0] = 6;
        array[1] = 2;
        array[2] = 8;
        array[3] = 1;
        array[4] = 3;
        array[5] = 0;
        array[6] = 9;
        array[7] = 7;

        System.out.print("Search for? ");
        int searching = Integer.valueOf(scanner.nextLine());
        boolean found = false;
        for (int i = 0; i < array.length; i++) {
            if (array[i] == searching) {
                System.out.println(searching + " is at index " + i + ".");
                found = true;
            }
        }
        if (!found) {
            System.out.println(searching + " was not found.");
        }
    }
}
""",
    "SumOfArray.java": """
public class SumOfArray {
    public static void main(String[] args) {
        int[] array = {5, 1, 3, 4, 2};
        System.out.println(sumOfNumbersInArray(array));
    }
    public static int sumOfNumbersInArray(int[] array) {
        int sum = 0;
        for (int number : array) {
            sum += number;
        }
        return sum;
    }
}
""",
    "ArrayPrinter.java": """
public class ArrayPrinter {
    public static void main(String[] args) {
        int[] array = {5, 1, 3, 4, 2};
        printNeatly(array);
    }
    public static void printNeatly(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
            if (i < array.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println();
    }
}
""",
    "Printer.java": """
public class Printer {
    public static void main(String[] args) {
        int[] array = {5, 1, 3, 4, 2};
        printArrayInStars(array);
    }
    public static void printArrayInStars(int[] array) {
        for (int number : array) {
            for (int i = 0; i < number; i++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
""",
    "PrintThrice.java": """
import java.util.Scanner;

public class PrintThrice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Give a word: ");
        String word = scanner.nextLine();
        System.out.println(word + word + word);
    }
}
""",
    "IsItTrue.java": """
import java.util.Scanner;

public class IsItTrue {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Give a string: ");
        String text = scanner.nextLine();
        if (text.equals("true")) {
            System.out.println("You got it right!");
        } else {
            System.out.println("Try again!");
        }
    }
}
""",
    "Login.java": """
import java.util.Scanner;

public class Login {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter username: ");
        String user = scanner.nextLine();
        System.out.print("Enter password: ");
        String pass = scanner.nextLine();
        
        if ((user.equals("alex") && pass.equals("sunshine")) || (user.equals("emma") && pass.equals("haskell"))) {
            System.out.println("You have successfully logged in!");
        } else {
            System.out.println("Incorrect username or password!");
        }
    }
}
""",
    "LineByLine.java": """
import java.util.Scanner;

public class LineByLine {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            String[] pieces = input.split(" ");
            for (String piece : pieces) {
                System.out.println(piece);
            }
        }
    }
}
""",
    "AVClub.java": """
import java.util.Scanner;

public class AVClub {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            String[] pieces = input.split(" ");
            for (String piece : pieces) {
                if (piece.contains("av")) {
                    System.out.println(piece);
                }
            }
        }
    }
}
""",
    "FirstWords.java": """
import java.util.Scanner;

public class FirstWords {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            String[] pieces = input.split(" ");
            System.out.println(pieces[0]);
        }
    }
}
""",
    "LastWords.java": """
import java.util.Scanner;

public class LastWords {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            String[] pieces = input.split(" ");
            System.out.println(pieces[pieces.length - 1]);
        }
    }
}
""",
    "AgeOfTheOldest.java": """
import java.util.Scanner;

public class AgeOfTheOldest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int oldest = -1;
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            String[] pieces = input.split(",");
            int age = Integer.valueOf(pieces[1]);
            if (age > oldest) {
                oldest = age;
            }
        }
        System.out.println("Age of the oldest: " + oldest);
    }
}
""",
    "NameOfTheOldest.java": """
import java.util.Scanner;

public class NameOfTheOldest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int oldestAge = -1;
        String oldestName = "";
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            String[] pieces = input.split(",");
            int age = Integer.valueOf(pieces[1]);
            if (age > oldestAge) {
                oldestAge = age;
                oldestName = pieces[0];
            }
        }
        System.out.println("Name of the oldest: " + oldestName);
    }
}
""",
    "PersonalDetails.java": """
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
"""
}

# Find all part 3 java files and overwrite them with solutions
files = glob.glob(os.path.join(base, 'part03-*', 'src', 'main', 'java', '*.java'))
for f in files:
    filename = os.path.basename(f)
    if filename in solutions:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(solutions[filename].strip() + "\\n")
            print(f"Solved: {filename}")
    else:
        print(f"Not found in solutions: {filename}")
