public class Match {
    String homeTeam;
    String visitingTeam;
    int homeTeamPoints;
    int visitingTeamPoints;

    public Match(String homeTeam, String visitingTeam, int homeTeamPoints, int visitingTeamPoints) {
        this.homeTeam = homeTeam;
        this.visitingTeam = visitingTeam;
        this.homeTeamPoints = homeTeamPoints;
        this.visitingTeamPoints = visitingTeamPoints;
    }

    public String getHomeTeam() {
        return homeTeam;
    }

    public void setHomeTeam(String homeTeam) {
        this.homeTeam = homeTeam;
    }

    public String getVisitingTeam() {
        return visitingTeam;
    }

    public void setVisitingTeam(String visitingTeam) {
        this.visitingTeam = visitingTeam;
    }

    public int getHomeTeamPoints() {
        return homeTeamPoints;
    }

    public void setHomeTeamPoints(int homeTeamPoints) {
        this.homeTeamPoints = homeTeamPoints;
    }

    public int getVisitingTeamPoints() {
        return visitingTeamPoints;
    }

    public void setVisitingTeamPoints(int visitingTeamPoints) {
        this.visitingTeamPoints = visitingTeamPoints;
    }
}

