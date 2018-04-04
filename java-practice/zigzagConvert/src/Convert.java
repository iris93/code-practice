public class Convert {
//    和 String 类不同的是，StringBuffer 和 StringBuilder 类的对象能够被多次的修改，并且不产生新的未使用对象.
//    执行效率从17%飞跃到95.05%

    public static String convert(String s,int numRows){
        int totalLen;
        totalLen = s.length();
        if (totalLen < 2 || numRows==1) {
            return s;
        }
//        String result = new String();
//        用StringBuffer替换
        StringBuffer result = new StringBuffer();
        int itemLen = 2*numRows-2;
        int numColunm;
        numColunm = totalLen/itemLen+1;
        for (int i=0;i<numRows;i++){
            for (int j=0;j<numColunm;j++){
                int item1Index = itemLen*j+i;
                if (item1Index < totalLen){
//                    result += s.charAt(item1Index);
                    result.append(s.charAt(item1Index));
                    if (i>0 && i<numRows-1){
                        int item2Index = item1Index+itemLen-2*i;
                        if (item2Index<totalLen){
//                            result += s.charAt(item2Index);
                            result.append(s.charAt(item2Index));
                        }
                    }
                }
            }
        }
        return result.toString();
    }
    public static void main(String args[]){
        String s = "PAYPALISHIRING";
        String result = convert(s,3);
        System.out.println(result);
    }
}
