public class ReverseInteger {
    public static int reverse(int x){
        long result = 0;
        while (Math.abs(x)>0){
            result = 10 * result + x % 10;
            if (Math.abs(result)<=2147483647) {
                x /= 10;
            }
            else{
                result = 0;
                break;
            }
        }
        return (int)result;
    }
    public static void main(String[] args) {
        int result = reverse(1534236469);
        System.out.println(result);
    }
}
