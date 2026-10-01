public class Room {
    private String code;
    private int seats;

    public Room(String code, int seats) {
        this.code = code;
        this.seats = seats;
    }

    public String getCode() { return code; }
    public int getSeats() { return seats; }
}
