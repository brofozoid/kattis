package brofozoid.kattis;
import java.util.Hashtable;
import java.util.Scanner;

public class no_duplicates {
    public static void main(String[] args) {
        Hashtable<String, Integer> words = new Hashtable<>();
        Scanner reader = new Scanner(System.in);
        String line = reader.nextLine();
        String[] input = line.split(" ");
        for (String word : input) {
            if (!words.containsKey(word)) {
                words.put(word, 1);
            } else {
                System.out.println("no");
                return;
            }
        }
        System.out.println("yes");
    }
}
