package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/11047
public class Q11047 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int k = Integer.parseInt(str[1]);
        int[] money = new int[n];
        int cnt = 0;
        for (int i=0; i<n; i++) {
            int coin = Integer.parseInt(reader.readLine());
            money[i] = coin;
        }
        while (k != 0) {
            n--;
            if (money[n] <= k) {
                int result = k / money[n];
                cnt += result;
                k = k - (money[n] * result);
            }
        }
        System.out.println(cnt);
    }
}
