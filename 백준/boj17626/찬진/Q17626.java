package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/17626
public class Q17626 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i=2; i<=n; i++) {
            int min = 1000000000;
            for (int j=1; j*j <= i; j++) {
                min = Math.min(min, dp[i - j*j]);
            }
            dp[i] = min + 1;
        }
        System.out.println(dp[n]);
    }
}
