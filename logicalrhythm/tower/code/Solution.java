import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            Stack<Integer> tower = new Stack<>();
            List<Integer> discard = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                int b = sc.nextInt();
                if (tower.isEmpty() || b < tower.peek()) tower.push(b);
                else discard.add(b);
            }
            if (discard.isEmpty()) { System.out.println("EMPTY DISCARD"); continue; }
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < discard.size(); i++) {
                if (i > 0) sb.append(' ');
                sb.append(discard.get(i));
            }
            System.out.println(sb);
        }
    }
}