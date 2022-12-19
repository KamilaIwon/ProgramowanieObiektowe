public class zad1 {
    public static void main(String[] args) {
        String imie = "kamillla";
        System.out.printf("\nzad1a: %d", countChar(imie, 'l'));
        System.out.printf("\nzad1b: %d", countSubStr("kamila", "kamil"));
    }

    static int countChar(String str, char c) {
        int ile = 0;
        for (int i = 0; i < str.length(); ++i) {
            if(str.charAt(i) == c) ++ile;
        }
        return ile;
    }

    static int countSubStr(String str, String subStr){
        int ile = 0;
        int j = 0;
        if (str.contains(subStr)){
            for (int i = 0; i < str.length(); ++i) {

            }
        }


        return ile;
    }
}