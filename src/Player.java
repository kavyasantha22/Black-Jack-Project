public class Player extends Person{
    public int money;
    public int currentBet;
    public boolean playing = true;


    public Player(String name, int money){
        super(name);
        this.money = money;
    }

    public Integer getMoney(){
        return this.money;
    }

    public void hit(Deck deck){
        Card newCard = deck.dealCard();
        addCard(newCard);
    }

    public void stand(){
        this.playing = false;
    }

    public Integer doubleDown(Deck deck){
        if (2*this.currentBet > this.money){
            return null;
        }else{
            this.currentBet *= 2;
            hit(deck);
            stand();
            return 1;
        }
    }

    public Integer placeBet(int betAmount){
        if (betAmount > this.money){
            System.out.println("Not enough money!");
            return null;
        }else{
            this.currentBet = betAmount;
            return 1;
        }
    }

    public void lose(){
        this.money -= this.currentBet;
    }

    public void win(){
        this.money += this.currentBet;
    }
}
