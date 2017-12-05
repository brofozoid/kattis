package brofozoid.kattis;

import java.util.Scanner;

public class fizzbuzz {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int fizz = reader.nextInt();
        int buzz = reader.nextInt();
        int n = reader.nextInt();
        for (int i = 1; i <= n; i++) {
            if (i % fizz == 0 && i % buzz == 0) {
                System.out.println("FizzBuzz");
            } else if (i % fizz == 0) {
                System.out.println("Fizz");
            } else if (i % buzz == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }
}