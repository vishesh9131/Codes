import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ServiceRecordCalculator extends JFrame {
    private JTextField passwordField;
    private JLabel messageLabel;

    public ServiceRecordCalculator() {
        setTitle("Password Application");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel passwordPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        JLabel passwordLabel = new JLabel("Enter your password:");
        passwordField = new JTextField(20);
        passwordPanel.add(passwordLabel);
        passwordPanel.add(passwordField);

        JPanel messagePanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        messageLabel = new JLabel();
        messagePanel.add(messageLabel);

        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton setPasswordButton = new JButton("Set Password");
        setPasswordButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                validatePassword();
            }
        });
        buttonPanel.add(setPasswordButton);

        add(passwordPanel, BorderLayout.NORTH);
        add(messagePanel, BorderLayout.CENTER);
        add(buttonPanel, BorderLayout.SOUTH);
    }

    private void validatePassword() {
        String password = passwordField.getText();

        if (password.length() >= 8 &&
            password.matches(".*[A-Z].*") &&
            password.matches(".*[a-z].*") &&
            password.matches(".*\\d.*") &&
            password.matches(".*[!@#$%^&*()-_=+].*")) {
            messageLabel.setText("Password set successfully!");
        } else {
            messageLabel.setText("Your password does not meet the requirements. Please try again.");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                ServiceRecordCalculator app = new ServiceRecordCalculator();
                app.setVisible(true);
            }
        });
    }
}
