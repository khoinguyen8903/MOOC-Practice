import os

base_dir = r"D:\TMCProjects\tmcdata\mooc-java-programming-i"

solutions = {
    "Part02_01.Squared": "Squared",
    "Part02_02.SquareRootOfSum": "SquareRootOfSum",
    "Part02_03.AbsoluteValue": "AbsoluteValue",
    "Part02_04.ComparingNumbers": "ComparingNumbers",
    "Part02_05.CarryOn": "CarryOn",
    "Part02_06.AreWeThereYet": "AreWeThereYet",
    "Part02_07.OnlyPositives": "OnlyPositives",
    "Part02_08.NumberOfNumbers": "NumberOfNumbers",
    "Part02_09.NumberOfNegativeNumbers": "NumberOfNegativeNumbers",
    "Part02_10.SumOfNumbers": "SumOfNumbers",
    "Part02_11.NumberAndSumOfNumbers": "NumberAndSumOfNumbers",
    "Part02_12.AverageOfNumbers": "AverageOfNumbers",
    "Part02_13.AverageOfPositiveNumbers": "AverageOfPositiveNumbers",
    "Part02_14.Counting": "Counting",
    "Part02_15.CountingToHundred": "CountingToHundred",
    "Part02_16.FromWhereToWhere": "FromWhereToWhere",
    "Part02_17.SumOfASequence": "SumOfASequence",
    "Part02_18.SumOfASequenceTheSequel": "SumOfASequenceTheSequel",
    "Part02_19.Factorial": "Factorial",
    "Part02_20.RepeatingBreakingAndRemembering": "RepeatingBreakingAndRemembering",
    "Part02_21.InAHoleInTheGround": "InAHoleInTheGround",
    "Part02_22.Reprint": "Reprint",
    "Part02_23.FromOneToParameter": "FromOneToParameter",
    "Part02_24.FromParameterToOne": "FromParameterToOne",
    "Part02_25.Division": "Division",
    "Part02_26.DivisibleByThree": "DivisibleByThree",
    "Part02_27.NumberUno": "NumberUno",
    "Part02_28.Word": "Word",
    "Part02_29.Summation": "Summation",
    "Part02_30.Smallest": "Smallest",
    "Part02_31.Greatest": "Greatest",
    "Part02_32.Averaging": "Averaging",
    "Part02_33.StarSign": "StarSign",
    "Part02_34.AdvancedAstrology": "AdvancedAstrology",
}

codes = {
"Squared": """import java.util.Scanner;
public class Squared {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = Integer.valueOf(scanner.nextLine());
        System.out.println(number * number);
    }
}""",
"SquareRootOfSum": """import java.util.Scanner;
public class SquareRootOfSum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int first = Integer.valueOf(scanner.nextLine());
        int second = Integer.valueOf(scanner.nextLine());
        System.out.println(Math.sqrt(first + second));
    }
}""",
"AbsoluteValue": """import java.util.Scanner;
public class AbsoluteValue {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = Integer.valueOf(scanner.nextLine());
        if (number < 0) {
            System.out.println(number * -1);
        } else {
            System.out.println(number);
        }
    }
}""",
"ComparingNumbers": """import java.util.Scanner;
public class ComparingNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int first = Integer.valueOf(scanner.nextLine());
        int second = Integer.valueOf(scanner.nextLine());
        if (first > second) {
            System.out.println(first + " is greater than " + second + ".");
        } else if (first < second) {
            System.out.println(first + " is smaller than " + second + ".");
        } else {
            System.out.println(first + " is equal to " + second + ".");
        }
    }
}""",
"CarryOn": """import java.util.Scanner;
public class CarryOn {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Shall we carry on?");
            String input = scanner.nextLine();
            if (input.equals("no")) {
                break;
            }
        }
    }
}""",
"AreWeThereYet": """import java.util.Scanner;
public class AreWeThereYet {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 4) {
                break;
            }
        }
    }
}""",
"OnlyPositives": """import java.util.Scanner;
public class OnlyPositives {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number < 0) {
                System.out.println("Unsuitable number");
                continue;
            } else if (number == 0) {
                break;
            }
            System.out.println(number * number);
        }
    }
}""",
"NumberOfNumbers": """import java.util.Scanner;
public class NumberOfNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = 0;
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            }
            count++;
        }
        System.out.println("Number of numbers: " + count);
    }
}""",
"NumberOfNegativeNumbers": """import java.util.Scanner;
public class NumberOfNegativeNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = 0;
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            }
            if (number < 0) {
                count++;
            }
        }
        System.out.println("Number of negative numbers: " + count);
    }
}""",
"SumOfNumbers": """import java.util.Scanner;
public class SumOfNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            }
            sum += number;
        }
        System.out.println("Sum of the numbers: " + sum);
    }
}""",
"NumberAndSumOfNumbers": """import java.util.Scanner;
public class NumberAndSumOfNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = 0;
        int sum = 0;
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            }
            count++;
            sum += number;
        }
        System.out.println("Number of numbers: " + count);
        System.out.println("Sum of the numbers: " + sum);
    }
}""",
"AverageOfNumbers": """import java.util.Scanner;
public class AverageOfNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = 0;
        int sum = 0;
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            }
            count++;
            sum += number;
        }
        double average = (double) sum / count;
        System.out.println("Average of the numbers: " + average);
    }
}""",
"AverageOfPositiveNumbers": """import java.util.Scanner;
public class AverageOfPositiveNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = 0;
        int sum = 0;
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            }
            if (number > 0) {
                count++;
                sum += number;
            }
        }
        if (count == 0) {
            System.out.println("Cannot calculate the average");
        } else {
            System.out.println((double) sum / count);
        }
    }
}""",
"Counting": """import java.util.Scanner;
public class Counting {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = Integer.valueOf(scanner.nextLine());
        for (int i = 0; i <= number; i++) {
            System.out.println(i);
        }
    }
}""",
"CountingToHundred": """import java.util.Scanner;
public class CountingToHundred {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = Integer.valueOf(scanner.nextLine());
        for (int i = number; i <= 100; i++) {
            System.out.println(i);
        }
    }
}""",
"FromWhereToWhere": """import java.util.Scanner;
public class FromWhereToWhere {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Where to? ");
        int to = Integer.valueOf(scanner.nextLine());
        System.out.print("Where from? ");
        int from = Integer.valueOf(scanner.nextLine());
        for (int i = from; i <= to; i++) {
            System.out.println(i);
        }
    }
}""",
"SumOfASequence": """import java.util.Scanner;
public class SumOfASequence {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Last number? ");
        int last = Integer.valueOf(scanner.nextLine());
        int sum = 0;
        for (int i = 1; i <= last; i++) {
            sum += i;
        }
        System.out.println("The sum is " + sum);
    }
}""",
"SumOfASequenceTheSequel": """import java.util.Scanner;
public class SumOfASequenceTheSequel {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("First number? ");
        int first = Integer.valueOf(scanner.nextLine());
        System.out.print("Last number? ");
        int last = Integer.valueOf(scanner.nextLine());
        int sum = 0;
        for (int i = first; i <= last; i++) {
            sum += i;
        }
        System.out.println("The sum is " + sum);
    }
}""",
"Factorial": """import java.util.Scanner;
public class Factorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Give a number: ");
        int number = Integer.valueOf(scanner.nextLine());
        int fact = 1;
        for (int i = 1; i <= number; i++) {
            fact *= i;
        }
        System.out.println("Factorial: " + fact);
    }
}""",
"RepeatingBreakingAndRemembering": """import java.util.Scanner;
public class RepeatingBreakingAndRemembering {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Give numbers:");
        int sum = 0;
        int count = 0;
        int even = 0;
        int odd = 0;
        while (true) {
            int number = Integer.valueOf(scanner.nextLine());
            if (number == -1) {
                break;
            }
            sum += number;
            count++;
            if (number % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
        System.out.println("Thx! Bye!");
        System.out.println("Sum: " + sum);
        System.out.println("Numbers: " + count);
        System.out.println("Average: " + ((double) sum / count));
        System.out.println("Even: " + even);
        System.out.println("Odd: " + odd);
    }
}""",
"InAHoleInTheGround": """public class InAHoleInTheGround {
    public static void main(String[] args) {
        printText();
    }
    public static void printText() {
        System.out.println("In a hole in the ground there lived a method");
    }
}""",
"Reprint": """import java.util.Scanner;
public class Reprint {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("How many times?");
        int times = Integer.valueOf(scanner.nextLine());
        for (int i = 0; i < times; i++) {
            printText();
        }
    }
    public static void printText() {
        System.out.println("In a hole in the ground there lived a method");
    }
}""",
"FromOneToParameter": """public class FromOneToParameter {
    public static void main(String[] args) {
    }
    public static void printUntilNumber(int number) {
        for (int i = 1; i <= number; i++) {
            System.out.println(i);
        }
    }
}""",
"FromParameterToOne": """public class FromParameterToOne {
    public static void main(String[] args) {
    }
    public static void printFromNumberToOne(int number) {
        for (int i = number; i >= 1; i--) {
            System.out.println(i);
        }
    }
}""",
"Division": """public class Division {
    public static void main(String[] args) {
    }
    public static void division(int numerator, int denominator) {
        System.out.println((double) numerator / denominator);
    }
}""",
"DivisibleByThree": """public class DivisibleByThree {
    public static void main(String[] args) {
    }
    public static void divisibleByThreeInRange(int beginning, int end) {
        for (int i = beginning; i <= end; i++) {
            if (i % 3 == 0) {
                System.out.println(i);
            }
        }
    }
}""",
"NumberUno": """public class NumberUno {
    public static void main(String[] args) {
    }
    public static int numberUno() {
        return 1;
    }
}""",
"Word": """public class Word {
    public static void main(String[] args) {
    }
    public static String word() {
        return "Hello";
    }
}""",
"Summation": """public class Summation {
    public static int sum(int num1, int num2, int num3, int num4) {
        return num1 + num2 + num3 + num4;
    }
    public static void main(String[] args) {
        int result = sum(4, 3, 6, 1);
        System.out.println("Sum: " + result);
    }
}""",
"Smallest": """public class Smallest {
    public static int smallest(int number1, int number2) {
        if (number1 < number2) {
            return number1;
        }
        return number2;
    }
    public static void main(String[] args) {
        int result = smallest(2, 7);
        System.out.println("Smallest: " + result);
    }
}""",
"Greatest": """public class Greatest {
    public static int greatest(int number1, int number2, int number3) {
        int max = number1;
        if (number2 > max) max = number2;
        if (number3 > max) max = number3;
        return max;
    }
    public static void main(String[] args) {
        int result = greatest(2, 7, 3);
        System.out.println("Greatest: " + result);
    }
}""",
"Averaging": """public class Averaging {
    public static int sum(int number1, int number2, int number3, int number4) {
        return number1 + number2 + number3 + number4;
    }
    public static double average(int number1, int number2, int number3, int number4) {
        return (double) sum(number1, number2, number3, number4) / 4;
    }
    public static void main(String[] args) {
        double result = average(4, 3, 6, 1);
        System.out.println("Average: " + result);
    }
}""",
"StarSign": """public class StarSign {
    public static void main(String[] args) {
        printStars(3);
        System.out.println("\\n---");
        printSquare(4);
        System.out.println("\\n---");
        printRectangle(5, 6);
        System.out.println("\\n---");
        printTriangle(3);
        System.out.println("\\n---");
    }
    public static void printStars(int number) {
        for (int i = 0; i < number; i++) {
            System.out.print("*");
        }
        System.out.println("");
    }
    public static void printSquare(int size) {
        for (int i = 0; i < size; i++) {
            printStars(size);
        }
    }
    public static void printRectangle(int width, int height) {
        for (int i = 0; i < height; i++) {
            printStars(width);
        }
    }
    public static void printTriangle(int size) {
        for (int i = 1; i <= size; i++) {
            printStars(i);
        }
    }
}""",
"AdvancedAstrology": """public class AdvancedAstrology {
    public static void printStars(int number) {
        for (int i = 0; i < number; i++) {
            System.out.print("*");
        }
        System.out.println("");
    }
    public static void printSpaces(int number) {
        for (int i = 0; i < number; i++) {
            System.out.print(" ");
        }
    }
    public static void printTriangle(int size) {
        for (int i = 1; i <= size; i++) {
            printSpaces(size - i);
            printStars(i);
        }
    }
    public static void christmasTree(int height) {
        for (int i = 1; i <= height; i++) {
            printSpaces(height - i);
            printStars(i * 2 - 1);
        }
        printSpaces(height - 2);
        printStars(3);
        printSpaces(height - 2);
        printStars(3);
    }
    public static void main(String[] args) {
        printTriangle(5);
        System.out.println("---");
        christmasTree(4);
        System.out.println("---");
        christmasTree(10);
    }
}"""
}

for folder, class_name in solutions.items():
    folder_name = "part02-" + folder
    java_file = os.path.join(base_dir, folder_name, "src", "main", "java", f"{class_name}.java")
    if os.path.exists(java_file):
        with open(java_file, "w", encoding="utf-8") as f:
            f.write(codes[class_name])
            print(f"Updated {java_file}")
    else:
        print(f"Not found: {java_file}")

print("All tasks completed.")
