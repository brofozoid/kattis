package brofozoid.kattis;

import java.util.Scanner;

public class pot {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int total = 0;
        int amount = reader.nextInt();
        for (int i = 0; i < amount; i ++) {
            int number = reader.nextInt();
            int pow = number % 10;
            total += Math.pow(number / 10, pow);
        }
        System.out.println(total);
    }
}
