import java.util.Scanner;

public class main {
	public static void main(String args[]){
		Scanner keyboard = new Scanner(System.in);
		int n = keyboard.nextInt();
		isItPrime(n);
	}
	public static boolean isItPrime(int x){
		return(primes(x) > 2);
	}
	public static int primes(int n){
		int a=0;
		int i=0;
		while(i < n){
			int b = n%i;
			if(b != 0){
				a++;
			}
			i++;
		}
		return a;
	}
}
