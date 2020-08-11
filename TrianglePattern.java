import java.util.Scanner;
class TrianglePattern {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.println("***** Enter Height *****");
        n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            for (int j = 1;j <= (n-i);j++) // For Printing Spaces
                System.out.print(" ");
            for (int k = 1;k <= (2*i-1);k++)  // For Printing the Required Character
                System.out.print("*");
            System.out.println();
        }
    }
}
