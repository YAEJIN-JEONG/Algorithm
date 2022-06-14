package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/9663
public class Q9663 {
    static int n;
    static boolean[] col;
    static int count;
    static boolean[] slash, back;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        col = new boolean[n];
        slash = new boolean[2*n+1];
        back = new boolean[2*n+1];
        backtrack(0);
        System.out.println(count);
    }
    private static void backtrack(int depth) {
        if (depth == n) {
            count++;
            return;
        } else {
            for (int i=0; i<n; i++) {
                if (!col[i] && !slash[depth-i+n] && !back[depth+i]) {
                    col[i] = slash[depth-i+n] = back[depth+i] = true;
                    backtrack(depth+1);
                    col[i] = slash[depth-i+n] = back[depth+i] = false;
                }
            }
        }
    }
}
