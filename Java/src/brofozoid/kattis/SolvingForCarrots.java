package brofozoid.kattis;

import java.util.Scanner;

public class SolvingForCarrots {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        String input = reader.nextLine();
        String[] inputList = input.split(" ");
        int answer = Integer.parseInt(inputList[1]);

        System.out.println(answer);
    }
}
