package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/1991
public class Q1991 {
    static Map<String, String[]> map;
    static String re = "";
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        map = new HashMap<>();
        for (int i=0; i<n; i++) {
            String[] str = reader.readLine().split(" ");map.put(str[0], new String[] {str[1], str[2]});

        }
        // 전위 순회
        before("A");
        System.out.println(re);
        // 중위 순회
        re = "";
        middle("A");
        System.out.println(re);
        // 후위 순회
        re = "";
        after("A");
        System.out.println(re);

    }

    private static void after(String start) {
        if (start.equals(".")) {
            return;
        }
        String[] result = map.get(start);
        after(result[0]);
        after(result[1]);
        // 왼쪽, 오른쪽 먼저 재귀 호출하고 저장
        re += start;
    }
    private static void middle(String start) {
        if (start.equals(".")) {
            return;
        }
        String[] result = map.get(start);

        middle(result[0]);
        // 왼쪽 재귀 호출하고 값 저장
        re += start;
        middle(result[1]);
        // 오른쪽 재귀 호출하고 값이 없으면 저장
        if (!re.contains(start)) {
            re += start;
        }
    }
    private static void before(String start) {
        if (start.equals(".")) {
            return;
        }
        // 먼저 추가 한 후 재귀
        re += start;
        String[] result = map.get(start);
        before(result[0]);
        before(result[1]);

    }
}
