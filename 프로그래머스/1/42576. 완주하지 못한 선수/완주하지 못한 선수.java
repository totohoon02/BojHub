import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> p = counter(participant);
        Map<String, Integer> c = counter(completion);

        for (String key : p.keySet()) {
            if(!c.containsKey(key)){
                return key;
            }
            if(p.get(key) - c.get(key) > 0){
                return key;
            }
        }
        return null;
    }
    
    public Map<String, Integer> counter(String[] strArray) {
        Map<String, Integer> c = new HashMap<>();
       
        for (String s : strArray) {
            if (c.containsKey(s)) {
                c.put(s, c.get(s) + 1);
            } else {
                c.put(s, 0);
            }
        }
        return c;
    }
}