import java.util.HashMap;  
import java.util.Scanner; 

public class Chatbot {  
    public static void main(String[] args) {  
        Scanner scanner = new Scanner(System.in);  
        HashMap<String, String> responses = new HashMap<>();

        responses.put("hello", "Hello! I'm your Movie Chatbot . Ask me for movie recommendations!");  
        responses.put("hi", "Hey there! Ready for some movie suggestions?");  
        responses.put("hey", "Hi! What kind of movie are you in the mood for?");  
        responses.put("who are you", "I am a Movie Recommendation Chatbot built in Java.");  
        responses.put("action", "Action movies: John Wick, Mad Max: Fury Road, The Dark Knight.");  
        responses.put("comedy", "Comedy movies: The Hangover, Superbad, 3 Idiots.");  
        responses.put("romance", "Romantic movies: Titanic, The Notebook, La La Land.");  
        responses.put("horror", "Horror movies: The Conjuring, It, Insidious.");  
        responses.put("thriller", "Thrillers: Se7en, Gone Girl, Shutter Island.");  
        responses.put("sci-fi", "Sci-Fi: Interstellar, Inception, The Matrix.");  
        responses.put("drama", "Drama movies: Forrest Gump, Fight Club, The Pursuit of Happyness.");  
        responses.put("animation", "Animated movies: Toy Story, Frozen, Spider-Man: Into the Spider-Verse.");  
        responses.put("sad", "Feeling sad? Watch: The Pursuit of Happyness, Forrest Gump.");  
        responses.put("happy", "For a good mood: 3 Idiots, Zindagi Na Milegi Dobara.");  
        responses.put("bored", "Try: Inception, The Dark Knight, or Interstellar.");  
        responses.put("best movie", "Top movies: The Shawshank Redemption, The Godfather, Inception.");  
        responses.put("suggest movie", "Try watching: Interstellar or The Dark Knight.");  
        responses.put("latest", "Recent popular movies: Oppenheimer, Dune Part Two.");  
        responses.put("top rated", "Top rated: Shawshank Redemption, The Godfather, The Dark Knight.");  
        responses.put("netflix", "Popular on Netflix: Extraction, Red Notice.");  
        responses.put("amazon", "On Amazon Prime: The Boys, Mirzapur.");  
        responses.put("thanks", "You're welcome! Enjoy your movie!");  
        responses.put("bye", "Goodbye! Enjoy your movies!");  
        System.out.println("Chatbot: Hello! I'm your Movie Bot. Type 'bye' to exit.");  


        while (true){  
            System.out.print("You: ");  
            String userInput = scanner.nextLine().toLowerCase();  
            if (userInput.equals("bye")){  
                System.out.println("Chatbot: " + responses.get("bye"));  
                break;  
            }

            boolean responseFound=false;  

            for (String key : responses.keySet()){  
                if (userInput.contains(key)) {  
                    System.out.println("Chatbot: " + responses.get(key));  
                    responseFound = true;  
                    break;  
                }  
            }  

            if (!responseFound){  
                System.out.println("Chatbot:  Try asking about genres or mood!");  
            }  
        }  
        scanner.close();  
    }  
}
