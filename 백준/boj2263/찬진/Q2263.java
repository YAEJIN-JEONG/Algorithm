package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

//https://www.acmicpc.net/problem/2263
public class Q2263 {
    static int n;
    static int[] in, post, pre;
    static int index;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        in = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        post = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        pre = new int[n];
        getPre(0, n-1, 0, n-1);
        for (int i : pre) {
            System.out.print(i + " ");
        }

    }

    private static void getPre(int is, int ie, int ps, int pe) {
        if (is <= ie && ps <= pe) {
            pre[index] = post[pe];
            index++;

            int start = is;
            for (int i=is; i<=ie; i++) {
                if (in[i] == post[pe]) {
                    start = i;
                    break;
                }
            }
            getPre(is, start-1, ps, ps+start-is-1);
            getPre(start+1, ie, ps+start-is, pe-1);
        }
    }
}
