import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Deck {
    private static final ArrayList<String> suits = new ArrayList<>(Arrays.asList("Hearts", "Diamonds", "Clubs", "Spades"));
    private static final ArrayList<String> ranks = new ArrayList<>(Arrays.asList("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"));
    private int index = -1;
    private ArrayList<Card> deck = setUp();

    public ArrayList<Card> setUp(){
        ArrayList<Card> cards = new ArrayList<>();
        for (String suit : suits){
            for (String rank :  ranks){
                cards.add(new Card(suit, rank));
            }
        }
        Collections.shuffle(cards);
        return cards;
    }

    public Card dealCard(){
        try{
            this.index++;
            return this.deck.get(this.index);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Deck is empty. Reshuffling...");
            this.deck = setUp(); // Reshuffle the deck
            this.index = 0;       // Reset index
            return this.deck.get(this.index);
        }
    }
}
