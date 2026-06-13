import java.io.*;

public class Solution {
    static String validate(String s){
        String[] p=s.split("\\.",-1);
        if(p.length!=4) return "INVALID";
        for(String g:p){
            if(!g.matches("\\d+")) return "INVALID";
            if(g.length()>1&&g.charAt(0)=='0') return "INVALID";
            if(Integer.parseInt(g)>255) return "INVALID";
        }
        return "VALID";
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine().trim());
        StringBuilder sb=new StringBuilder();
        while(t-->0) sb.append(validate(br.readLine().trim())).append('\n');
        System.out.print(sb);
    }
}