package lab11;

public class klasy {

    public static void main(String[] args){
        RachunekBankowy.setRocznaStopaProcentowa(0.04);
    }
    public class RachunekBankowy{
        private static double rocznaStopaProcentowa;

        public RachunekBankowy(){

        }

        public static void setRocznaStopaProcentowa(double value){
            RachunekBankowy.rocznaStopaProcentowa = value;
        }

    }
}
