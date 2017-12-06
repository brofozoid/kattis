package brofozoid.kattis;

import java.util.Scanner;

public class ColdputerScience {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int total = 0;
        int amount = reader.nextInt();
        for (int i = 0; i < amount; i++) {
            int temp = reader.nextInt();
            if (temp < 0) {
                total += 1;
            }
        }
        System.out.println(total);
    }
}
