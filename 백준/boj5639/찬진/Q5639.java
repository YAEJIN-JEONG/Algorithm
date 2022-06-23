package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

//https://www.acmicpc.net/problem/5639
public class Q5639 {
    static List<Integer> list = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String str = reader.readLine();
            if (str == null || str.equals("")) break;
            list.add(Integer.parseInt(str));
        }

        post(0, list.size()-1);

    }

    private static void post(int start, int end) {
        if (start > end) return;
        System.out.println("시작:" + start + "," + "끝:" + end);

        int mid = start+1;

        while (mid<=end && list.get(mid)<list.get(start)) {
            mid++;
        }
        post(start+1, mid-1);
        post(mid, end);
        System.out.println(list.get(start));
    }
}
