package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

//https://www.acmicpc.net/problem/2407
public class Q2407 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);
        BigInteger n1 = BigInteger.ONE;
        BigInteger m1 = BigInteger.ONE;
        for (int i=0; i<m; i++) {
            n1 = n1.multiply(new BigInteger(String.valueOf(n-i)));
            m1 = m1.multiply(new BigInteger(String.valueOf(i+1)));
        }
        System.out.println(n1.divide(m1));
    }
}
