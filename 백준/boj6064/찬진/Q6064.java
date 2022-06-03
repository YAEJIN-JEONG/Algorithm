package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/6064
public class Q6064 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        for (int i=0; i<t; i++) {
            String[] str = reader.readLine().split(" ");
            int m = Integer.parseInt(str[0]);
            int n = Integer.parseInt(str[1]);
            int x = Integer.parseInt(str[2]) - 1;
            int y = Integer.parseInt(str[3]) - 1;

            boolean flag = false;
            for (int j=x; j<lcm(m, n); j+=m) {
                if (j % n == y) {
                    System.out.println(j + 1);
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                System.out.println(-1);
            }
        }
    }

    private static int lcm(int m, int n) {
        int multi = m * n;
        if (m >= n) {
            while (n != 0) {
                int temp = m % n;
                m = n;
                n = temp;
            }
            return multi / m;
        } else {
            while (m != 0) {
                int temp = n % m;
                n = m;
                m = temp;
            }
            return multi / n;
        }


    }

}
