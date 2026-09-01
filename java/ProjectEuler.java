import java.util.Scanner;
public class ProjectEuler {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String str = "";
		
		System.out.println("Enter a number.");
		str = scan.next();
		
		int[] arr = new int[str.length()];
		
		for (int i = 0; i < arr.length; i++)
			arr[i] = Integer.valueOf(str.substring(i,i+1));
		
		scan.close();
		long largest = greatestProduct(arr, 13);
		System.out.println("Maximum Value Possible: " + Math.pow(9, 13));
		System.out.println("Largest product: " + largest);
	}
	
	public static long greatestProduct(int[] arr, int amt) {
		//int ind = 0;
		long largest = Integer.MIN_VALUE;
		
		for (int i = 0; i < arr.length - amt; i++) {
			long product = 1;
			for(int j = 0; j < amt; j++) {
				product *= arr[i+j];
			}
			if (product > largest) {
				//ind = i;
				largest = product;
			}
		}
		return largest;		
	}

}
