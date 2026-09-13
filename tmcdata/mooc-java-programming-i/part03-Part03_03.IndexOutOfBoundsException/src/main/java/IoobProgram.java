import java.util.ArrayList;

public class IoobProgram {
    public static void main(String[] args) {
        ArrayList<String> lines = new ArrayList<>();
        lines.add("Never has a man influenced physics so profoundly as Niels Bohr in the early 1900's");
        lines.add("Going back to this time period, little was known about atomic structure; Bohr set out");
        System.out.println(lines.get(100));
    }
}
