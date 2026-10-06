import java.util.ArrayList;

public class Hold {
    private int maxWeight;
    private ArrayList<Suitcase> suitcases = new ArrayList<>();
    private int weight;

    public Hold(int maxWeight) {
        this.maxWeight = maxWeight;
        this.weight = 0;
    }
    public void addSuitcase(Suitcase suitcase){
        if(suitcase.totalWeight() + this.weight <= this.maxWeight){
            this.suitcases.add(suitcase);
            this.weight += suitcase.totalWeight();
        }
    }
    @Override
    public String toString(){
        return this.suitcases.size() + " suitcases" + "(" + this.weight + " kg)";
    }
    public void printItems(){
        for(int i =0; i< this.suitcases.size(); i++){
            this.suitcases.get(i).printItems();
        }
    }
}
