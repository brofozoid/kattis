package brofozoid.kattis;

import java.util.Scanner;

public class bijele {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int correct[] = {1,1,2,2,2,8};
        int input[] = new int[6];
        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < correct.length; i++) {
            input[i] = reader.nextInt();
            ans.append(correct[i] - input[i]).append(" ");
        }
        System.out.println(ans);
    }
}
