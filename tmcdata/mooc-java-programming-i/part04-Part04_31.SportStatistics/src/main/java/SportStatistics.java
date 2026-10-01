
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class SportStatistics {

    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        String file = scan.nextLine();
        Scanner fileScan = new Scanner(Paths.get(file));
        ArrayList<Match> matches = new ArrayList<>();
        while(fileScan.hasNextLine()){
            String line = fileScan.nextLine();
            String[] temp = line.split(",");
            Match match = new Match(temp[0], temp[1], Integer.parseInt(temp[2]), Integer.parseInt(temp[3]) );
            matches.add(match);
        }

        String team = scan.nextLine();
        int count = 0;
        int wins =0;
        int loses =0;
        for (Match match : matches){
            if(match.getHomeTeam().equals(team)|| match.getVisitingTeam().equals(team)){
                count += 1;
                if(match.getHomeTeam().equals(team)&&match.getHomeTeamPoints()<match.getVisitingTeamPoints()){
                    loses += 1;
                }
                else if (match.getHomeTeam().equals(team)&&match.getHomeTeamPoints()>match.getVisitingTeamPoints()){
                    wins +=1;
                }
                else if(match.getVisitingTeam().equals(team)&&match.getVisitingTeamPoints()<match.getHomeTeamPoints()){
                    loses += 1;
                }
                else if (match.getVisitingTeam().equals(team)&&match.getVisitingTeamPoints()>match.getHomeTeamPoints()){
                    wins +=1;
                }

            }


        }
        System.out.println("Games: " + count);
        System.out.println("Wins: " + wins);
        System.out.println("Losses: " + loses);
    }

}
