package lab11;

public class klasy2 {
    public static void main(String[] args){
        IntegerSet set = new IntegerSet();
        set.insertElement(5);
        set.insertElement(6);
        set.insertElement(5);
        set.insertElement(3);
        set.insertElement(7);
        set.deleteElement(6);
        System.out.println(set);
        IntegerSet set1 = new IntegerSet();
        set1.insertElement(1);
        set1.insertElement(3);
        set1.insertElement(5);

        IntegerSet set2 = new IntegerSet();
        set2.insertElement(1);
        set2.insertElement(3);
        set2.insertElement(5);

        System.out.println(set1.equals(set2));

        set2.insertElement(6);
        System.out.println(set1.equals(set2));
    }
}

class IntegerSet{
    private boolean[] set;

    public IntegerSet(){
        set = new boolean[101];
    }

    public static IntegerSet union(IntegerSet a, IntegerSet b){
        IntegerSet result = new IntegerSet();
        for(int i = 1; i<=100; ++i){
            if(a.set[i] == true || b.set[i] == true){
                result.set[i] = true;
            }
            else {
                result.set[i] = false;
            }
        }
        return result;
    }

    public static IntegerSet intersetion(IntegerSet a, IntegerSet b){
        IntegerSet result = new IntegerSet();
        for(int i = 1; i<=100; ++i){
            if(a.set[i] == true && b.set[i] == true){
                result.set[i] = true;
            }
            else {
                result.set[i] = false;
            }
        }
        return result;
    }

    public void insertElement(int element){
        if(element >= 1 && element <= 100){
            this.set[element] = true;
        }

    }

    public void deleteElement(int element){
        if(element >= 1 && element <= 100){
            this.set[element] = false;
        }

    }

    public String toString(){
        String result = "";
        for(int i = 1; i<= 100; ++i){
            if(this.set[i]==true){
                result += i + " ";
            }
        }
        return result;
    }

    public boolean equals(IntegerSet b){
        for(int i = 1; i<= 100; ++i){
            if(this.set[i] != b.set[i]) return false;
        }
        return true;
    }
}
