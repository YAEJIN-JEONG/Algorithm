import java.util.HashSet;
import java.util.Set;

public class Solution {

    public int solution(String[][] relation) {
        int cols = relation[0].length;
        Set<Integer> candidates = new HashSet<>();

        loop:
        // 조합을 비트로 표현 1: 포함, 0: 미포함
        for (int i=1; i < (1 << cols); i++) {
            for (int candidate : candidates) {
                // 부분 집합 여부 (최소성)
                if ((i & candidate) == candidate)
                    continue loop;
            }

            // 선택된 속성만 사용한 튜플 개수 (중복 제외)
            Set<String> tuples = new HashSet<>();

            for (String[] tuple : relation) {
                StringBuilder sb = new StringBuilder();
                for (int j=0; j<relation[0].length; j++) {
                    if ((i & (1 << j)) > 0) {
                        sb.append(tuple[j]);
                    }
                }
                tuples.add(sb.toString());
            }

            // 기존 튜플 개수와 선택된 속성만 사용한 튜플 개수가 같으면 후보키 (유일성)
            if (tuples.size() == relation.length) {
                candidates.add(i);
            }
        }

        return candidates.size();
    }
}
