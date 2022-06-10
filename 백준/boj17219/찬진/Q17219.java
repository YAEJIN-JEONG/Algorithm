package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Q17219 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);

        Map<String, String> map = new HashMap<>();
        for (int i=0; i<n; i++) {
            str = reader.readLine().split(" ");
            map.put(str[0], str[1]);
        }

        for (int i=0; i<m; i++) {
            String input = reader.readLine();
            System.out.println(map.get(input));
        }

    }
}
