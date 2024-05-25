// Vishesh Yadav (enroll.:1232214)(roll.:23)
// Alloted Q7. suppose youre being assigned to write the code for applying for password on the login page . 
// the user can apply the conditions by itself to apply the password

import java.util.Scanner;

public class PasswordApplication {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the password application!");
        System.out.println("Please create your password.");

        String password;
        boolean validPassword = false;

        do {
            System.out.println("Your password must meet the following conditions:");
            System.out.println("- At least 8 characters long");
            System.out.println("- Contains at least one uppercase letter");
            System.out.println("- Contains at least one lowercase letter");
            System.out.println("- Contains at least one digit");
            System.out.println("- Contains at least one special character (!@#$%^&*()-_=+)");
            System.out.print("Enter your password: ");
            password = scanner.nextLine();

            if (password.length() >= 8 &&
                password.matches(".*[A-Z].*") &&
                password.matches(".*[a-z].*") &&
                password.matches(".*\\d.*") &&
                password.matches(".*[!@#$%^&*()-_=+].*")) {
                validPassword = true;
            } else {
                System.out.println("Your password does not meet the requirements. Please try again.");
            }
        } while (!validPassword);

        System.out.println("Congratulations! Your password has been set successfully.");
        System.out.println("You can now use it to log in.");
        
    }
}
