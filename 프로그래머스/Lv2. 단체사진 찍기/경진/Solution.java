package programmers.group_photo;

public class Solution {
    // 사진 찍는 멤버
    private final char[] members = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    private String[] data;
    // 정답 카운트
    private int count;

    public int solution(int n, String[] data) {
        this.data = data;
        permutations("", new boolean[members.length], 0);
        return count;
    }

    // 순열 만들기 (백트래킹)
    public void permutations(String permutation, boolean[] visited, int depth) {
        if (depth == members.length) {
            // 순열이 완성되었으면 조건만족여부 확인 후 종료
            if(isValid(permutation))
                count++;
            return;
        }
        // 순열에 포함되지 않은 멤버를 한 명씩 줄세워보기
        for (int i=0; i<members.length; i++) {
            if(!visited[i]) {
                visited[i] = true;
                permutation += members[i];
                permutations(permutation, visited, depth + 1);
                permutation = permutation.substring(0, permutation.length() - 1);
                visited[i] = false;
            }
        }
    }
    // 조건을 만족하는 순서인지 확인
    public boolean isValid(String permutation) {
        for (String condition : data) {
            char c1 = condition.charAt(0);
            char c2 = condition.charAt(2);
            char comp = condition.charAt(3);
            int num = condition.charAt(4) - '0';
            int diff = Math.abs(permutation.indexOf(c1) - permutation.indexOf(c2));
            switch (comp) {
                case '>':
                    if (diff - 1 <= num)
                        return false;
                    break;
                case '<':
                    if (diff - 1 >= num)
                        return false;
                    break;
                case '=':
                    if (diff - 1 != num)
                        return false;
            }
        }
        return true;
    }
}
