public class Main {

    public static boolean isPalindrome1(int x){
        if (x <0)return false;
        if (x == 0) return true;
        StringBuffer sb = new StringBuffer();
        sb.append(x);
        System.out.println(sb);
        int i=0;
        int j = sb.length()-1;
        while (i<j){
            if (sb.charAt(i)!=sb.charAt(j)){
                return false;
            }else {
                i++;
                j--;
            }
        }
        return true;

    }

    public static boolean isPalindrome(int x) {
        if (x == 0)return true;
        if (x <0 ||x%10==0)return false;
        int result=0;
        while (x>result){
            result = result*10+x%10;
            x = x/10;
        }
        return (result==x||x==result/10);

    }


    public static void main(String[] args) {
        int x = 12321;
        boolean result = isPalindrome(x);
        System.out.println(result);
    }
}
