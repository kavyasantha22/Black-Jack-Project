import java.util.ArrayList;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        BlackJackGame game = new BlackJackGame();
        clearTeminal();
        System.out.println("=".repeat(40));
        String text = "🎲 WELCOME TO BLACKJACK 🎲";
        int padding = (40 - text.length()) / 2;
        String centered = " ".repeat(Math.max(0, padding));
        System.out.println(centered +  text);
        System.out.println("=".repeat(40));
        game.greet();
        System.out.println();

        String playerName = getName();
        getAge(playerName);
        int playerMoney = getMoney();
        System.out.println();
        if (playerMoney >= 1000){
            System.out.println("💼 Ohohoho, we have an important guest here!");
            System.out.println(); // Empty line
            System.out.println();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.err.println("Thread was interrupted: " + e.getMessage());
            }
        }
        game.setUpPlayer(playerName, playerMoney);
        System.out.println("✅ All set up! Ready to play.");
        System.out.println();
        System.out.println();

        int roundCount = 0;
        Scanner scanner = new Scanner(System.in);
        while (game.player.getMoney() > 0){
            if (roundCount > 0){
                System.out.println("Do you want to continue the game? (Yes/No): ");
                String continueGame = scanner.nextLine();
                if (!continueGame.toLowerCase().contains("yes")){
                    break;
                }
            }
            clearTeminal();
            System.out.println("\uD83D\uDCB0 Current Money: $" + game.player.getMoney());
            roundCount++;
            System.out.println("=".repeat(40));
            System.out.println(centered + "\uD83C\uDFB2 ROUND " + roundCount + " \uD83C\uDFB2");
            System.out.println("=".repeat(40));

            int roundBet = getBet(game.player, roundCount);
            game.roundSetUp(roundBet);

            while (!game.player.isBusted() && game.player.playing){
                clearTeminal();
                System.out.println("=".repeat(40));
                System.out.println(centered + "\uD83C\uDFB2 ROUND " + roundCount + " \uD83C\uDFB2");
                System.out.println("=".repeat(40));
                System.out.println();
                ArrayList<Card> playerCards = game.getPlayerCards();
                ArrayList<Card> dealerCards = game.getDealerCards();

                String playerHeader = "🃏 Player's Cards";
                String dealerHeader = "\uD83C\uDCA0 Dealer's Cards";

                System.out.println();
                System.out.printf("%-20s | %-20s%n", playerHeader, dealerHeader);
                System.out.println("-".repeat(21) + "|" + "-".repeat(20));

                int maxLen = Math.max(playerCards.size(), dealerCards.size());

                for (int i = 0; i < maxLen; i++) {
                    String playerCard = (i < playerCards.size()) ? playerCards.get(i).toString() : " ".repeat(20);
                    String dealerCard = (i < dealerCards.size()) ? dealerCards.get(i).toString() : " ".repeat(20);
                    if (i == 1) {
                        dealerCard = "*Hidden*";
                    }
                    System.out.printf("%-20s | %-20s%n", playerCard, dealerCard);
                }
                System.out.println("-".repeat(40));
                chooseAction(game.player, game.deck);
            }
            clearTeminal();
            System.out.println("=".repeat(40));
            System.out.println(centered + "\uD83C\uDFB2 ROUND " + roundCount + " \uD83C\uDFB2");
            System.out.println("=".repeat(40));

            if (game.player.isBusted()){
                System.out.println("🃏 Final Player's Cards:");
                for (Card card : game.player.getCards()){
                    System.out.println(" " + card);
                }
                System.out.println("\nPlayer's value: " + game.player.getValue());
                System.out.println("\\n\uD83D\uDCA5 You Busted! \uD83D\uDCA5\\n");
                game.player.lose();
                System.out.println("😞 You Lose... 😞\n");
                continue;
            }else{
                System.out.println("🃏 Final Player's Cards:");
                for (Card card : game.player){
                    System.out.println(" " + card);
                }
                System.out.println("\nPlayer's value: " + game.player.getValue());
                System.out.println("\nDealer's Turn...");
                System.out.println();
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    System.err.println("Thread was interrupted: " + e.getMessage());
                }
                game.dealer.play(game.deck);
                for (Card card : game.dealer){
                    System.out.println(" " + card);
                    try {
                        Thread.sleep(500);
                    } catch (InterruptedException e) {
                        System.err.println("Thread was interrupted: " + e.getMessage());
                    }
                }
                System.out.println("\nDealer's value: " + game.dealer.getValue());

                if (game.dealer.isBusted()){
                    System.out.println("\n\uD83D\uDCA5 Dealer Busted! \uD83D\uDCA5\n");
                    game.player.win();
                    System.out.println("\uD83C\uDF89 YOU WIN!!! \uD83C\uDF89\n");
                }else if (game.getWinner() == game.player){
                   game.player.win();
                    System.out.println("\n🎉 YOU WIN!!! 🎉\n");
                }else{
                    game.player.lose();
                    System.out.println("\n😞 You Lose... 😞\n");
                }
            }
        }
        if (game.player.getMoney() <= 0){
            System.out.println("Sorry, you don't have enough money left to gamble");
            System.out.println();
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                System.err.println("Thread was interrupted: " + e.getMessage());
            }
        }
        clearTeminal();
        scanner.close();

    }

    private static void clearTeminal(){
        System.out.println("\n".repeat(100));

//        try{
//            String os = System.getProperty("os.name").toLowerCase();
//            if (os.contains("win")) {
//                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
//            }else{
//                System.out.print("\033c");
//                System.out.flush();
//            }
//        } catch (IOException | InterruptedException e){
//            e.printStackTrace();
//        }
    }

    private static String getName(){
        System.out.println("Please input your name: ");
        Scanner scanner = new Scanner(System.in);
        String ret = scanner.nextLine();
        scanner.close();
        return ret;
    }

    private static int getAge(String player_name){
        int age = 0;
        Scanner scanner = new Scanner(System.in);
        while (true){
            System.out.println("Please input your age: ");
            try{
                age = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("\nAge must be a number!\n");
                continue;
            }
            if (age > 120){
                System.out.println("\nI know you are not that old!\n");
                continue;
            }
            if (age < 18){
                System.out.print("\n\uD83D\uDEAB Sorry " + player_name + ", you need to wait " + (18-age) + " more year(s) before playing (gambling). \uD83D\uDEAB\n");
                System.exit(0);
            }
            scanner.close();
            return age;
        }
    }

    private static int getMoney(){
        Scanner scanner = new Scanner(System.in);
        while (true){
            System.out.println("\uD83D\uDCB5 How much money are you gambling today? $");
            try{
                int ret = Integer.parseInt(scanner.nextLine());
                scanner.close();
                return ret;
            } catch (NumberFormatException e) {
                System.out.println("\nAmount of money must be numeric!\n");
            }
        }
    }

    private static int getBet(Player player, int roundCount){
        int bet;

        Scanner scanner = new Scanner(System.in);
        while (true){
            System.out.println("\uD83D\uDCB5 How much are you betting on round " + roundCount + "? $");
            try{
                bet = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e){
                System.out.println("\nAmount of bet must be numeric!\n");
                continue;
            }
            if (player.getMoney() < bet){
                System.out.println("\nNot enought money...\n");
                continue;
            }
            if (bet <= 0){
                System.out.println("\nBet must be a positive amount!\n");
                continue;
            }
            scanner.close();
            return bet;
        }
    }

    private static void chooseAction(Player player, Deck deck){
        System.out.println("\nChoose your action:");
        System.out.println("1. Hit\n2. Double Down\n3. Stand");
        Scanner scanner = new Scanner(System.in);
        while (true){
            int chosenAction = Integer.parseInt(scanner.nextLine());
            System.out.println();
            if (chosenAction == 1){
                player.hit(deck);
                break;
            }else if (chosenAction == 2){
                if (player.doubleDown(deck) == null){
                    System.out.println("\nNot enough money...\n");
                    continue;
                }
                break;
            }else if (chosenAction == 3){
                player.stand();
                break;
            }else{
                System.out.println("\nChoose appropriate action!\n");
            }
        }
        scanner.close();
    }

}