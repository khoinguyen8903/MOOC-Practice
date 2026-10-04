
public class Money {

    private final int euros;
    private final int cents;

    public Money(int euros, int cents) {

        if (cents > 99) {
            euros = euros + cents / 100;
            cents = cents % 100;
        }

        this.euros = euros;
        this.cents = cents;
    }

    public int euros() {
        return this.euros;
    }

    public int cents() {
        return this.cents;
    }

    public String toString() {
        String zero = "";
        if (this.cents < 10) {
            zero = "0";
        }

        return this.euros + "." + zero + this.cents + "e";
    }
    public Money plus(Money addition) {
        Money newMoney = new Money(this.euros + addition.euros, this.cents + addition.cents()); // create a new Money object that has the correct worth

        // return the new Money object
        return newMoney;
    }
    public boolean lessThan(Money compared){
        if(this.euros<compared.euros){
            return true;
        }
        else if(this.euros > compared.euros){
            return  false;
        }
        else if (this.euros == compared.euros()){
            if (this.cents < compared.cents()){
                return true;
            }
            else {
                return false;
            }
        }
        return true;
    }
    public Money minus(Money decreaser){
        int newEuros = 0;
        int newCents = 0;
        if(!this.lessThan(decreaser)) {
            newEuros = this.euros - decreaser.euros;
            newCents = 0;
            if (this.cents - decreaser.cents < 0){
                newCents = this.cents + 100 -decreaser.cents;
                newEuros -= 1;
            }
            else {
                newCents = this.cents - decreaser.cents;
            }
        }
        Money newMoney = new Money(newEuros, newCents);
        return newMoney;
    }

}
