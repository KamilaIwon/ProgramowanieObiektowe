import java.lang.StringBuffer;
import java.io.FileReader;
import java.io.IOException;
import java.io.*;
import java.math.BigInteger;
import java.math.BigDecimal;
import java.math.RoundingMode;

public class zadania {
    public static void main(String[] args) throws Exception {
        String imie = "kamillla";
        System.out.printf("\nzad1a: %d", countChar(imie, 'l'));
        System.out.printf("\nzad1b: %d", countSubStr("alamakmotma", "ma"));
        System.out.printf("\nzad1c: %s", middle("middle"));
        System.out.printf("\nzad1d: %s", repeat("ho", 3));
        int [] tab = where("almaamakotama","ma");
        System.out.print("\nzad1e: ");
        printTab(tab);
        System.out.printf("\nzad1f: %s", change("abcDEF"));
        System.out.printf("\nzad1g: %s", nice("123456"));
        System.out.printf("\nzad1h: %s", nice("12345678",'*',4));
        System.out.printf("\nzad2: %d", zad2("kartka.txt", 'a'));
        System.out.printf("\nzad3: %d", zad3("kartka.txt", "ma"));
        System.out.printf("\nzad4: %d", zad4(2));
        BigDecimal zad = zad5(1000, 2, 4);
        System.out.println("\nzad5: " + zad);
        //System.out.println(napis1.equals(napis2));

    }

    static int countChar(String str, char c) {
        int ile = 0;
        for (int i = 0; i < str.length(); ++i) {
            if(str.charAt(i) == c) ++ile;
        }
        return ile;
    }

    static int countSubStr(String str, String subStr){
        int len = subStr.length();
        int ile = 0;
        for(int i = 0; i<str.length()-len+1; ++i){
            String newstr = str.substring(i,i+len);
            if(newstr.equals(subStr)) ++ile;
        }
        return ile;
    }

    static String middle(String str){
        if(str.length() % 2 != 0){
            int begin = str.length()/2;
            return str.substring(begin, begin+1);
        }
        int begin = str.length()/2 - 1;
        return str.substring(begin,begin+2);
    }

    static String repeat(String str, int n){
        String newstr = "";
        int i = 0;
        while(i != n){
            newstr += str;
            ++i;
        }
        return newstr;
    }

    static int[] where(String str, String subStr){
        int[] tab = new int[10];
        int len = subStr.length();
        int ile = 0;

        for(int i = 0; i<str.length()-len+1; ++i){
            String newStr = str.substring(i,i+len);
            if(newStr.equals(subStr)){
                tab[ile] = i;
                ++ile;
            }
        }
        int[] officialTab = new int[ile];
        System.arraycopy(tab, 0, officialTab, 0, ile);
        return officialTab;
    }

    static void printTab(int[] tab){
        for(int i = 0; i< tab.length; ++i){
            if(i==0){
                System.out.print("\n[");
            }
            if(i==tab.length-1){
                System.out.printf("%d]", tab[i]);
                break;
            }
            System.out.printf("%d, ", tab[i]);
        }
    }

    static String change(String str){
        StringBuffer sb = new StringBuffer().append(str);
        for (int i = 0; i< sb.length(); ++i){
            if (Character.isUpperCase(sb.charAt(i))){
                char c = sb.charAt(i);
                sb.setCharAt(i, Character.toLowerCase(c));
            }
            else if(Character.isLowerCase(sb.charAt(i))){
                char c = sb.charAt(i);
                sb.setCharAt(i, Character.toUpperCase(c));
            }
        }
        return sb.toString();
    }
    static String nice(String str){
        StringBuffer sb = new StringBuffer().append(str);
        int ile = 0;
        for (int i = 0; i<sb.length(); i+=3){
            sb.insert(i+ile,'\'');
            ++ile;
        }
        return sb.toString();
    }

    static String nice(String str, char znak, int idx){
        StringBuffer sb = new StringBuffer().append(str);
        int ile = 0;
        for (int i = 0; i<sb.length(); i+=idx){
            sb.insert(i+ile,znak);
            ++ile;
        }
        return sb.toString();
    }

    static int zad2(String name, char c) throws IOException{
        Reader reader = new FileReader(name);
        int ile = 0;
        int i;
        while((i=reader.read())!=-1)
        {
            if(i==((int)c)) ++ile;
        }
        reader.close();
        return ile;
    }

    static int zad3(String name, String str) throws IOException{
        Reader reader = new FileReader(name);
        int ile = 0;
        int suma = 0;
        int i;
        int j = 0;
        while((i=reader.read())!=-1)
        {
            char c = str.charAt(j);
            if(i!=((int)c)){
                ile = 0;
                j = 0;
            }
            if(i==((int)c))
            {
                ++ile;
                ++j;
            }
            if(ile==str.length()) {
                ++suma;
                ile = 0;
                j = 0;
            }
        }
        reader.close();
        return suma;
    }
    static BigInteger zad4(int n){
        BigInteger suma = BigInteger.ZERO;
        BigInteger i = BigInteger.ONE;
        BigInteger liczbaPol = new BigInteger(String.valueOf(n*n));
        while(!liczbaPol.equals(BigInteger.ZERO)){

            suma = suma.add(i);
            i = i.multiply(BigInteger.valueOf(2));
            liczbaPol = liczbaPol.subtract(BigInteger.ONE);
        }
        return suma;
    }

    static BigDecimal zad5(int k, int p, int n){
        BigDecimal pr = new BigDecimal(p)
                .divide(BigDecimal.TEN)
                .divide(BigDecimal.TEN);
        BigDecimal kap = new BigDecimal(k);
        for(int i =1; i<n; ++i){
            BigDecimal dodatek = kap.multiply(pr);
            kap = kap.add(dodatek);
        }
        return kap.setScale(2, RoundingMode.HALF_UP);
    }

}