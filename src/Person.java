import java.util.ArrayList;
import java.util.Iterator;

public abstract class Person implements Iterable<Card> {
    private ArrayList<Card> cards = new ArrayList<>();
    private int value = 0;
    private int hardAces = 0;
    private boolean busted = false;
    public String name;

    public Person(String name){
        this.name = name;
    }

    public void setUp(Deck deck){
        value = 0;
        hardAces = 0;
        busted = false;
        ArrayList<Card> cards = new ArrayList<>();
        for (int i = 0; i < 2; i++){
            addCard(deck.dealCard());
        }
    }

    public ArrayList<Card> getCards(){
        return this.cards;
    }

    public int getValue(){
        return this.value;
    }

    public int getHardAces(){
        return this.hardAces;
    }

    public void addCard(Card card){
        this.cards.add(card);
        this.value += card.getValue();
        if (card.getRank().equals("Ace")){
            this.hardAces += 1;
        }
        adjustForAces();
        checkBusted();
    }

    public void checkBusted(){
        this.busted = this.value > 21;
    }

    public void adjustForAces(){
        while (this.value > 21 && this.hardAces > 0){
            this.value -= 10;
            this.hardAces -= 1;
        }
    }

    public void emptyCards(){
        this.cards = new ArrayList<>();
    }

    public boolean isBusted(){
        return this.busted;
    }

    @Override
    public Iterator<Card> iterator(){
        return cards.iterator();
    }
}
