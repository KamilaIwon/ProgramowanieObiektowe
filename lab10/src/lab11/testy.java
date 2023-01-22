package lab11;

public class testy {

    public static void main(String[] args){
        Publikacja gazeta1 = new Publikacja("Publikacja ", 20, 2000, 12, 3);
        System.out.println(gazeta1);
        Publikacja gazeta2 = new Publikacja("Publikacja ", 20, 2000, 12, 3);
        Publikacja gazeta3 = new Publikacja("Publikacja ", 20);
        System.out.println(gazeta3.getDataWydania());
        System.out.println(gazeta1.equals(gazeta2));
        System.out.println(gazeta1.equals(gazeta3));
        gazeta3.setDataWydania(2021, 30, 10);
        System.out.println(gazeta3.getDataWydania());
        gazeta3.setDataWydania(2021, 1, 10);
        System.out.println(gazeta3.getDataWydania());
        System.out.println(Publikacja.getIle()+ "\n------------------------\n");
        Czasopismo czas1 = new Czasopismo("Pub", 21, 2000, 11, 23, 1);
        Czasopismo czas2 = new Czasopismo("Pub", 21, 2000, 11, 23, 1);
        Czasopismo czas3 = new Czasopismo("Publikacja nieznana", 21, 2000, 11, 23, 1);
        System.out.println(czas1.equals(czas2));
        czas2.setNumer(0);
        System.out.println(czas1.equals(czas2));
        czas2.setNumer(2);
        System.out.println(czas1.equals(czas2));
        System.out.println(gazeta1.equals(czas1));
        System.out.println(czas1);
        System.out.println(czas3);
        System.out.println(Publikacja.getIle());
        System.out.println(czas3.equals(czas1));

    }
}
