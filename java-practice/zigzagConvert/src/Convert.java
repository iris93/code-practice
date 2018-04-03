public class Convert {

    public static String convert(String s,int numRows){
        int totalLen;
        totalLen = s.length();
        if (totalLen < 2 || numRows==1) {
            return s;
        }
        int itemLen = 2*numRows-2
        int numColunm;
        numColunm = totalLen/itemLen+1
    }
    public static void main(String args[]){
        String s = "Thisistest";
        String result = convert(s,1);
        System.out.println(result);
    }
}
