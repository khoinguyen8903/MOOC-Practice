import java.util.ArrayList;

public class Suitcase {
    private int maxWeight;
    private ArrayList<Item> items;
    private int totalWeight; // Tạo thêm biến để theo dõi tổng cân nặng hiện tại

    public Suitcase(int maxWeight) {
        this.maxWeight = maxWeight;
        this.items = new ArrayList<>();
        this.totalWeight = 0; // Khởi tạo lúc đầu vali nặng 0 kg
    }

    public void addItem(Item item) {
        // Chỉ cần kiểm tra xem: Tổng cân hiện tại + Món mới có vượt giới hạn không?
        if (this.totalWeight + item.getWeight() <= this.maxWeight) {
            this.items.add(item);
            this.totalWeight += item.getWeight(); // Thêm thành công thì cộng dồn cân nặng luôn
        }
    }

    @Override
    public String toString() {
        // Trường hợp 1: Vali trống
        if (this.items.isEmpty()) {
            return "no items (0 kg)";
        }

        // Trường hợp 2: Vali có đúng 1 món (Dùng "item" KHÔNG có 's')
        if (this.items.size() == 1) {
            return "1 item (" + this.totalWeight + " kg)";
        }

        // Trường hợp 3: Vali có nhiều món (Dùng "items" CÓ 's')
        return this.items.size() + " items (" + this.totalWeight + " kg)";
    }

    public void printItems(){
        for(Item item : this.items){
            System.out.println(item);
        }
    }
    public int totalWeight(){
        return this.totalWeight;
    }
    public Item heaviestItem(){
        if (this.items.isEmpty()){
            return null;
        }
        else {
            Item heaviest = this.items.get(0);
            for (int i = 1; i< this.items.size(); i++){
                if(heaviest.getWeight() < this.items.get(i).getWeight()){
                    heaviest = this.items.get(i);
                }
            }
            return heaviest;
        }

    }
}