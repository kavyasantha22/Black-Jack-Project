import java.util.HashMap;
import java.util.Map;

public class Card {
    private static final Map<String, Integer> rankValues = new HashMap<>();
    private final String suit;
    private final String rank;
    private final int value;

    static {
        for (int n = 2; n <= 10; n++){
            rankValues.put(String.valueOf(n), n);
        }
        for (String x : new String[]{"Jack", "Queen", "King"}){
            rankValues.put(x, 10);
        }
        rankValues.put("Ace", 11);
    }

    public Card(String suit, String rank){
        this.suit = suit;
        this.rank = rank;
        this.value = calculate_value();

    }

    private int calculate_value(){
        Integer x = rankValues.get(this.rank);
        if (x == null){
            throw new IllegalArgumentException("Card rank not found!");
        }else{
            return x;
        }
    }

    public int getValue(){
        return this.value;
    }

    public String getRank(){
        return this.rank;
    }

    public String getSuit(){
        return this.suit;
    }

    @Override
    public String toString(){
        return this.rank + " of " + this.suit;
    }
}




