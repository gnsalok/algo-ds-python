import java.util.*;

public class swap {
    public static void swapValues(int n1, int n2){
        int temp;
        temp = n1;
        n1 = n2;
        n2 = temp;
    }
    public static void main(String[] args) {

        int n1 = 12;
        int n2 = 13;

        swapValues(n1, n2);
        System.out.println(n1 + " -- "+ n2);  
    }
}
