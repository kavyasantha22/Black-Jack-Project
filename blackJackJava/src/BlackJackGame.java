import java.util.ArrayList;

public class BlackJackGame {
    public Dealer dealer = new Dealer("Pablo");
    public Player player;
    public Deck deck;

    public BlackJackGame(){
        setUpDeck();
    }

    public void greet(){
        System.out.println("Welcome to Black Jack Game managed by Pablo");
    }

    public void setUpPlayer(String player_name, int player_money){
        this.player = new Player(player_name, player_money);
    }

    public void setUpDeck(){
        this.deck = new Deck();
        deck.setUp();
    }

    public void roundSetUp(int round_bet){
        setUpDeck();
        this.player.setUp(this.deck);
        this.dealer.setUp(this.deck);
        this.player.playing = true;
        this.player.currentBet = round_bet;
    }

    public ArrayList<Card> getPlayerCards(){
        return this.player.getCards();
    }

    public ArrayList<Card> getDealerCards(){
        return this.dealer.getCards();
    }

    public Person getWinner(){
        if (this.player.getValue() > this.dealer.getValue()){
            return this.player;
        }else{
            return this.dealer;
        }
    }
}
