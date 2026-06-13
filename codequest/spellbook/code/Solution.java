import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); sc.nextLine();
        while (t-- > 0) {
            String s = sc.nextLine();
            Stack<Character> stk = new Stack<>();
            boolean ok = true;
            for (char c : s.toCharArray()) {
                if ("([{".indexOf(c) >= 0) { stk.push(c); continue; }
                if (")]}".indexOf(c) >= 0) {
                    if (stk.isEmpty()) { ok = false; break; }
                    char top = stk.pop();
                    if ((c==')' && top!='(') || (c==']' && top!='[') || (c=='}' && top!='{'))
                    { ok = false; break; }
                }
            }
            System.out.println((ok && stk.isEmpty()) ? "SAFE" : "DANGEROUS");
        }
    }
}