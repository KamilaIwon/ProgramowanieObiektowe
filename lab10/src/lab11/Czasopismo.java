package lab11;

public class Czasopismo extends Publikacja{
    private int numer;

    public Czasopismo(String tytul, double cena, int rok, int miesiac, int dzien, int numer) {
        super(tytul, cena, rok, miesiac, dzien);
        this.numer = numer;
    }

    public int getNumer() {
        return numer;
    }

    public void setNumer(int numer) {
        if (numer > 0){
            this.numer = numer;
        }
    }

    @Override
    public String toString() {
        return super.toString() + ", [" + numer + "]";
    }

    @Override
    public boolean equals(Object otherObject){
        if(!super.equals(otherObject)){return false;}

        Czasopismo other = (Czasopismo) otherObject;
        return numer == other.numer;
    }
}
