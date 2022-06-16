package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/1629
public class Q1629 {
    static long c;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        long a = Integer.parseInt(str[0]);
        long b = Integer.parseInt(str[1]);
        c = Integer.parseInt(str[2]);
        System.out.println(pow(a, b));
    }

    // 제곱을 반으로 나눠준다
    public static long pow(long a, long b) {
        if (b == 1) {
            return a % c;
        }
        long temp = pow(a, b/2);
        // 제곱이 홀수일때 a를 한번 더 곱한다
        if (b % 2 == 1) {
            return (temp * temp % c) * a % c;
        }
        return temp * temp % c;
    }
}
