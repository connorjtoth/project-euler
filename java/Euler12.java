public class Euler12 {

	public static void main(String[] args) {
		long numFactors = 0;
		long tri = 0;
		long i = 3;
		while (numFactors <= 500) {
			tri = getTriangleNumber(i);
			numFactors = numberOfFactors(tri);
			
			i++;			
		}
		System.out.println("------------------------");
		System.out.println("Triangle Number: " + tri);
		System.out.println("Number of Factors: " + numFactors);
		System.out.println("N: "+ i);

		
		
		
	}
	
	public static long getTriangleNumber(long n) {
		long r = 0;
		for (long i = 1; i <= n; i++) {
			r+= i;
		}
		return r;
	}
	
	public static long numberOfFactors(long m) {
		long max = m;
		long count = 0;
		for (long i=1; i < max; i++) {
			if (m % i == 0) {
				max = m / i;
				count+=2;
			}
		}
		//if (n % half == 0) count++;
		return count;
	}

}
