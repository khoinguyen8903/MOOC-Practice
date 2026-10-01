public class Statistics {
    private int count;
    private int sum;
    public Statistics() {
        this.count = 0;
        this.sum = 0;
    }

    public void addNumber(int number) {
        count += 1;
        sum = sum + number;
    }

    public int getCount() {
        // write code here
        return count;
    }
    public int sum() {
        // write code here
        return sum;
    }

    public double average() {
        // write code here
        if (this.count == 0){
            return 0.00;
        }
        return (double)sum / count;
    }

}