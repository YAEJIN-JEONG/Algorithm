package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

//https://www.acmicpc.net/problem/2096
public class Q2096 {
    static int[][] arr;
    static Integer[][] dp_max;
    static Integer[][] dp_min;
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        arr = new int[n][3];
        dp_max = new Integer[n][3];
        dp_min = new Integer[n][3];

        for (int i=0; i<n; i++) {
            arr[i] = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        for (int i=0; i<3; i++) {
            dp_min[0][i] = dp_max[0][i] = arr[0][i];

        }
        int max = 0;
        int min = Integer.MAX_VALUE;
        for (int i=0; i<3; i++) {
            dp_max[n-1][i] = checkMax(n-1, i);
            max = Math.max(dp_max[n-1][i], max);
            dp_min[n-1][i] = checkMin(n-1, i);
            min = Math.min(dp_min[n-1][i], min);
        }
        System.out.println(max + " " + min);

    }
    
    //작은값 dp 구하기
    private static Integer checkMin(int x, int y) {
        if (x == 0) {
            return dp_min[x][y];
        }
        if (dp_min[x][y] == null) {
            if (y == 0) {
                dp_min[x][y] = Math.min(checkMin(x-1, y), checkMin(x-1, y+1)) + arr[x][y];
                return dp_min[x][y];
            } else if (y == 1) {
                dp_min[x][y] = Math.min(Math.min(checkMin(x-1, y), checkMin(x-1, y+1)), checkMin(x-1, y-1)) + arr[x][y];
                return dp_min[x][y];
            } else {
                dp_min[x][y] = Math.min(checkMin(x-1, y), checkMin(x-1, y-1)) + arr[x][y];
                return dp_min[x][y];
            }
        } else {
            return dp_min[x][y];
        }
    }
    
    //큰값 dp 구하기
    private static int checkMax(int x, int y) {
        if (x == 0) {
            return dp_max[x][y];
        }
        if (dp_max[x][y] == null) {
            if (y == 0) {
                dp_max[x][y] = Math.max(checkMax(x-1, y), checkMax(x-1, y+1)) + arr[x][y];
                return dp_max[x][y];
            } else if (y == 1) {
                dp_max[x][y] = Math.max(Math.max(checkMax(x-1, y), checkMax(x-1, y+1)), checkMax(x-1, y-1)) + arr[x][y];
                return dp_max[x][y];
            } else {
                dp_max[x][y] = Math.max(checkMax(x-1, y), checkMax(x-1, y-1)) + arr[x][y];
                return dp_max[x][y];
            }
        } else {
            return dp_max[x][y];
        }

    }
}
