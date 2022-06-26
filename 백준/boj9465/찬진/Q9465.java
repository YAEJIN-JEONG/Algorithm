package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

//https://www.acmicpc.net/problem/9465
public class Q9465 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        for (int i=0; i<t; i++) {
            int n = Integer.parseInt(reader.readLine());
            int[][] arr = new int[2][n];
            int[][] dp = new int[2][n];
            for (int j=0; j<2; j++) {
                arr[j] = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }
            dp[0][0] = arr[0][0];
            dp[1][0] = arr[1][0];
            if (n > 1) {
                dp[0][1] = dp[1][0] + arr[0][1];
                dp[1][1] = dp[0][0] + arr[1][1];

                for (int j=2; j<n; j++) {
                    dp[0][j] = Math.max(dp[1][j-1], dp[1][j-2]) + arr[0][j];
                    dp[1][j] = Math.max(dp[0][j-1], dp[0][j-2]) + arr[1][j];
                }
            }
            System.out.println(Math.max(dp[0][n-1], dp[1][n-1]));
        }
    }
}
