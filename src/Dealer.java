public class Dealer extends Person{
    public Dealer(String name){
        super(name);
    }

    public void play(Deck deck){
        while (this.getValue() < 17){
            addCard(deck.dealCard());
        }
    }
}
