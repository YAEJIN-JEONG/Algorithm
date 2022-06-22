package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

//https://www.acmicpc.net/problem/2448
public class Q2448 {
    static String[][] stars;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        stars = new String[n][2*n-1];
        for (int i=0; i<n; i++) {
            Arrays.fill(stars[i], " ");
        }
        star(0, n-1, n);

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++) {
            for (int j=0; j<2*n-1; j++) {
                sb.append(stars[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    private static void star(int x, int y, int n) {
        if (n == 3) {
            stars[x][y] = "*";
            stars[x+1][y-1] = stars[x+1][y+1] = "*";
            stars[x+2][y-2] = stars[x+2][y-1] = stars[x+2][y] = stars[x+2][y+1] = stars[x+2][y+2] = "*";
        } else {
            star(x, y, n/2);
            star(x + (n/2), y + (n/2), n/2);
            star(x + (n/2), y - (n/2), n/2);
        }
    }
}
