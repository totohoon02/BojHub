import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int maxKind = (int) nums.length / 2;
        Set<Integer> kind = new HashSet<>();
        
        for(int num : nums){
            kind.add(num);
            if(kind.size() == maxKind){
                break;
            }
        }
        return kind.size();
    }
}