package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q9095 {

    public static void main(String[] args) throws IOException {
        int[] num = new int[11];
        num[0] = 0;
        num[1] = 1;
        num[2] = 2;
        num[3] = 4;
        for (int i=4; i<11; i++) {
            num[i] = num[i-1] + num[i-2] + num[i-3];
        }
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        for (int i=0; i<t; i++) {
            System.out.println(num[Integer.parseInt(reader.readLine())]);
        }
    }
}
