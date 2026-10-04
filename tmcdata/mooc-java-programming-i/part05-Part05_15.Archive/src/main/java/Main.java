
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Archive> list = new ArrayList<>();
        while (true){
            System.out.println("Identifier? (empty will stop)");
            String IdentifierScan = scanner.nextLine();
            if (IdentifierScan.isEmpty()){
                break;
            }
            System.out.println("Name? (empty will stop)");
            String NameScan = scanner.nextLine();
            if (NameScan.isEmpty()){
                break;
            }
            Archive Archive = new Archive(IdentifierScan, NameScan);
            if (!list.contains(Archive)){
                list.add(Archive);
            }
        }
        for (Archive i:list){
            System.out.println(i.getIdentifier() + ": " + i.getName());
        }


    }
}
