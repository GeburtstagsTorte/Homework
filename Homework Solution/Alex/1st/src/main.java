
public class one{
private int i;
private int s;
	public void median(int a){
		s = s+a;
		i= s/2;
		System.out.println(i);
	}
}
public class two{
private int e;
	public void evens(int n){
		int i=0;
		System.out.println(0);
		while(i < n-1){
			System.out.println(i*2);
			i--;
		}
		/*or
		 * while(n!=0){
		 * 	System.out.println(n*2);
		 * 	n--;
		 * }
		 * */
	}
}
public class three{
	public boolean isItPrime(int x){
		return(primes(x) > 2);
	}
	public int primes(int n){
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