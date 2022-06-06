package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q9461 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        long[] num = new long[101];
        num[0] = num[1] = num[2] = 1;
        for (int i=3; i<101; i++) {
            num[i] = num[i-2] + num[i-3];
        }

        for (int i=0; i<t; i++) {
            System.out.println(num[Integer.parseInt(reader.readLine()) - 1]);
        }
    }
}
