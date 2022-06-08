package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/11723
public class Q11723 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(reader.readLine());
        StringBuilder sb = new StringBuilder();
        int bit = 0;
        for (int i=0; i<m; i++) {
            String[] str = reader.readLine().split(" ");
            switch (str[0]) {
                case "all":
                    bit = (1 << 21) - 1;
                    break;
                case "empty":
                    bit = 0;
                    break;
                default:
                    int x = Integer.parseInt(str[1]);
                    switch (str[0]) {
                        case "add":
                            bit |= (1 << x);
                            break;
                        case "remove":
                            bit &= ~(1 << x);
                            break;
                        case "toggle":
                            if ((bit & (1 << x)) == 0) {
                                bit |= (1 << x);
                            } else {
                                bit &= ~(1 << x);
                            }
                            break;
                        case "check":
                            if ((bit & (1 << x)) == 0) {
                                sb.append(0 + "\n");
                            } else {
                                sb.append(1 + "\n");
                            }
                            break;
                    }
            }
        }
        System.out.println(sb);
    }
}
