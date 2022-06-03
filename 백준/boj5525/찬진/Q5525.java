package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/5525
public class Q5525 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        int m = Integer.parseInt(reader.readLine());
        String s = reader.readLine();
        int[] dp = new int[m];

        int cnt = 0;
        for (int i=2; i<m; i++) {
            String temp = s.substring(i-2, i+1);
            if (temp.equals("IOI")) {
                dp[i] = dp[i-2] + 1;
            }
            if (dp[i] >= n) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
