public class MyAtoi {
    public static int myAtoi(String str) {
        int strLength = str.length();
        if (strLength == 0) {
            System.out.println(1);
            return 0;
        }

        char[] strList = str.toCharArray();
        long result = 0;
        int start = 0;
//        while (Character.isSpaceChar(strList[start])){
        while (strList[start] == ' '){
            if (start==strLength-1){
                System.out.println(2);
                return 0;
            }else{start++;}
        }
        int numSymbol = 1;
        int end = 0;
        if (strList[start]=='-'){
            numSymbol = -1;
            start ++;
            end = start;
        }else if (strList[start]=='+'){
            start++;
            end = start;
        }else if (Character.isDigit(strList[start])){
            end = start;
        }else {
            System.out.println("start"+' '+start);
            return 0;}
        while (end<strLength&&Character.isDigit(strList[end])){
            result = 10*result + strList[end]-'0';
            long temp = result*numSymbol;
            if (temp>Integer.MAX_VALUE){return Integer.MAX_VALUE;}
            else if (temp<Integer.MIN_VALUE){return Integer.MIN_VALUE;}
            end++;
        }
        result=result*numSymbol;
        return (int)result;
    }
    public static void main(String[] args) {
        String str = "9223372036854775809";
        int result = myAtoi(str);
        System.out.println(result);
    }
}
