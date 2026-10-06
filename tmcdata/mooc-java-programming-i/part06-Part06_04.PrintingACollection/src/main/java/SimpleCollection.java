
import java.util.ArrayList;

public class SimpleCollection {

    private String name;
    private ArrayList<String> elements;

    public SimpleCollection(String name) {
        this.name = name;
        this.elements = new ArrayList<>();
    }

    public void add(String element) {
        this.elements.add(element);
    }

    public ArrayList<String> getElements() {
        return this.elements;
    }
    @Override
    public String toString(){
        String output = "The collection " + this.name;
        int size = this.elements.size();
        if (this.elements.size() == 0){
            output += " is empty.";
        }
        else{
            output+= " has " + size + " element";
            if (size >1){
                output += "s:\n";
            }
            else {
                output += ":\n";
            }
            for (int i = 0; i<size; i++) {
                output += this.elements.get(i);
                if(i!=size-1){
                    output+= "\n";
                }
            }
        }
        return output;
    }


}
