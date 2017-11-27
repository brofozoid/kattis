package brofozoid.kattis;

import java.util.Scanner;

public class Tarifa {

    public static void main(String[] args) {
        // write your code here
        Scanner reader = new Scanner(System.in);
        int allowance = reader.nextInt();
        int months = reader.nextInt();
        int total = 0;
        for (int i = 0; i < months; i++) {
            int month = reader.nextInt();
            total += allowance - month;
        }
        reader.close();
        total += allowance;
        System.out.println(total);
    }
}

