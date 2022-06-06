package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Q9375 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        for (int i=0; i<t; i++) {
            Map<String, List<String>> map = new HashMap<>();
            int n = Integer.parseInt(reader.readLine());
            for (int j=0; j<n; j++) {
                String[] str = reader.readLine().split(" ");
                List<String> list = map.getOrDefault(str[1], new ArrayList<>());
                list.add(str[0]);
                map.put(str[1], list);
            }
            int sum = 1;
            for (String s : map.keySet()) {
                sum = sum * (map.get(s).size() + 1);
            }
            System.out.println(sum - 1);
        }

    }
}
