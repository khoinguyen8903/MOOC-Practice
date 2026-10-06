import java.util.ArrayList;
import java.util.Random;

public class JokeManager {
    private ArrayList<String> jokeManager = new ArrayList<>();

    public JokeManager() {
    }
    public void addJoke(String joke){
        this.jokeManager.add(joke);
    }
    public String drawJoke(){
        if (this.jokeManager.size() == 0){
            return ("Jokes are in short supply.");
        }
        else {
            Random random = new Random();
            int randomIndex = random.nextInt(this.jokeManager.size());
            return this.jokeManager.get(randomIndex);
        }
    }
    public void printJokes(){
        String output = "";
        for (int i = 0; i < this.jokeManager.size(); i++){
            output += this.jokeManager.get(i);
            if (i!= this.jokeManager.size() - 1){
                output += "\n";
            }
        }
        System.out.println(output);
    }
}
