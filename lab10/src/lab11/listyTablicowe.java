package lab11;

import java.util.ArrayList;
import java.util.Arrays;

public class listyTablicowe {
    public static ArrayList<Integer> append(ArrayList<Integer> a, ArrayList<Integer> b) {
        ArrayList<Integer> result = new ArrayList<>(a);
        result.addAll(b);
        return result;
    }

    public static ArrayList<Integer> merge(ArrayList<Integer> a, ArrayList<Integer> b){
        ArrayList<Integer> tab = new ArrayList<>();
        int r = 0;
        int length = a.size() + b.size();
        int i =0;
        int p = 0;
        while (i < length){

            if (r >= a.size()){
                while (p< b.size()){
                    tab.add(b.get(p));
                    p += 1;
                }
                return tab;
            }

            if (p >= b.size()){
                while (r < a.size()){
                    tab.add(a.get(r));
                    r += 1;
                }
                return tab;
            }

            if (i % 2 == 0){
                tab.add(a.get(r));
                r += 1;
            }

            if (i % 2 != 0) {
                tab.add(b.get(p));
                p += 1;
            }
            i += 1;
        }
        return tab;
    }

    public static void Sort(ArrayList<Integer> a){
        int j;
        int s = -1;
        for (int i = 0; i < a.size(); ++i){
            s += 1;
            for ( j = s; j < a.size(); ++j){
                if (a.get(i).compareTo(a.get(j)) > 0){
                    int tmp = a.get(i);
                    a.set(i, a.get(j));
                    a.set(j, tmp);
                }
            }
        }
    }

    public static ArrayList<Integer> mergeSorted(ArrayList<Integer> a, ArrayList<Integer> b){
        ArrayList<Integer> tab = new ArrayList<>();
        Sort(a);
        Sort(b);
        int r = 0;
        int p = 0;
        int length = a.size() + b.size();
        int i = 0;
        while (i < length){

            if (r >= a.size()){
                while (p < b.size()){
                    tab.add(b.get(p));
                    p += 1;
                }
                return tab;
            }

            if (p >= b.size()){
                while (r < a.size()){
                    tab.add(a.get(r));
                    r += 1;
                }
                return tab;
            }
            if (a.get(r) < b.get(p)){
                tab.add(a.get(r));
                r += 1;
            }
            else {
                tab.add(b.get(p));
                p += 1;
            }
            i += 1;
        }
        return tab;
    }

    public static ArrayList<Integer> reversed(ArrayList<Integer> a){
        ArrayList<Integer> tab = new ArrayList<>();
        for(int i = a.size() - 1; i >= 0; --i){
            tab.add(a.get(i));
        }
        return tab;
    }

    public static void reverse (ArrayList<Integer> a){
        for(int i = 0; i < a.size()/2; ++i){
            int tmp = a.get(i);
            a.set(i,a.get(a.size()-i-1));
            a.set(a.size()-i-1, tmp);
        }
    }
    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>(Arrays.asList(1, 4, 9, 16, 5));
        ArrayList<Integer> b = new ArrayList<>(Arrays.asList(9, 7, 4, 9, 11));
        ArrayList<Integer> c = mergeSorted(a, b);
        ArrayList<Integer> d = reversed(a);
        System.out.println(c);
        System.out.println(d);
        reverse(d);
        System.out.println(d);
    }
}
