
import java.util.ArrayList;
import java.util.Scanner;

class Stock {
    String name;
    double price;
    String trend;
    String volume;
    String rsi;
    String decision;
    String riskLevel;
    String suggestion;

    Stock(String name, double price, String trend, String volume, String rsi) {
        this.name = name;
        this.price = price;
        this.trend = trend.toLowerCase();
        this.volume = volume.toLowerCase();
        this.rsi = rsi.toLowerCase();
    }

    void displayInfo() {
        System.out.println("\nStock Name: " + name);
        System.out.println("Price: ₹" + price);
        System.out.println("Trend: " + trend);
        System.out.println("Volume: " + volume);
        System.out.println("RSI: " + rsi);

        System.out.println("Decision: " + (decision != null ? decision : "Pending"));
        System.out.println("Risk Level: " + (riskLevel != null ? riskLevel : "Unknown"));
        System.out.println("Suggestion: " + (suggestion != null ? suggestion : "None"));
    }
}

class StockExpertSystem {
    ArrayList<Stock> stocks = new ArrayList<>();

    void addStock(Stock stock) {
        stocks.add(stock);
        analyzeStock(stock);
    }

    void analyzeStock(Stock stock) {

        if (stock.trend.equals("bullish") && stock.volume.equals("high") && stock.rsi.equals("normal")) {
            stock.decision = "BUY";
            stock.riskLevel = "Low";
            stock.suggestion = "Strong upward momentum. Good entry point.";
        }
        else if (stock.trend.equals("bullish") && stock.rsi.equals("overbought")) {
            stock.decision = "HOLD";
            stock.riskLevel = "Medium";
            stock.suggestion = "Stock is overbought. Wait for dip.";
        }
        else if (stock.trend.equals("bearish") && stock.volume.equals("high")) {
            stock.decision = "SELL";
            stock.riskLevel = "High";
            stock.suggestion = "Downtrend confirmed. Exit position.";
        }
        else if (stock.rsi.equals("oversold")) {
            stock.decision = "BUY";
            stock.riskLevel = "Medium";
            stock.suggestion = "Possible reversal. Buy cautiously.";
        }
        else if (stock.trend.equals("neutral")) {
            stock.decision = "HOLD";
            stock.riskLevel = "Low";
            stock.suggestion = "No clear direction. Wait.";
        }
        else {
            stock.decision = "HOLD";
            stock.riskLevel = "Unknown";
            stock.suggestion = "Insufficient data.";
        }
    }

    void displayAllStocks() {
        if (stocks.isEmpty()) {
            System.out.println("No stock data available.");
            return;
        }

        System.out.println("\n--- Stock Market Analysis ---");
        for (Stock stock : stocks) {
            stock.displayInfo();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StockExpertSystem system = new StockExpertSystem();

        System.out.println("Stock Market Expert System");
        System.out.println("--------------------------------");

        while (true) {
            System.out.println("\n1. Analyze Stock");
            System.out.println("2. Display All Stocks");
            System.out.println("3. Exit");
            System.out.print("Enter choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter stock name: ");
                    String name = scanner.nextLine();

                    System.out.print("Enter price: ");
                    double price = scanner.nextDouble();
                    scanner.nextLine();

                    System.out.print("Enter trend (bullish/bearish/neutral): ");
                    String trend = scanner.nextLine();

                    System.out.print("Enter volume (high/low): ");
                    String volume = scanner.nextLine();

                    System.out.print("Enter RSI (overbought/oversold/normal): ");
                    String rsi = scanner.nextLine();

                    Stock stock = new Stock(name, price, trend, volume, rsi);
                    system.addStock(stock);

                    System.out.println("Analysis Complete!");
                    stock.displayInfo();
                    break;

                case 2:
                    system.displayAllStocks();
                    break;

                case 3:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;

                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}
