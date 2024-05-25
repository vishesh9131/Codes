#include <iostream>
#include <stack>
#include <string>
#include <cctype> // for isdigit

using namespace std;
bool isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}
int precedence(char op) {
    return (op == '+' || op == '-') ? 1 : 2;  // Ternary for cleaner precedence
}

int pf(string expr) {
    stack<int> s;
    for (char c : expr) {
        if (isdigit(c)) {
            s.push(c - '0');
        } else if (isOperator(c)) { 
            if (s.size() < 2) {
                cerr << "Invalid expression: Too few operands\n";
                return -1;
            }
            int op2 = s.top();
            s.pop();
            int op1 = s.top();
            s.pop();
            switch (c) {
                case '+': s.push(op1 + op2); break;
                case '-': s.push(op1 - op2); break;
                case '*': s.push(op1 * op2); break;
                case '/':
                    if (op2 == 0) {
                        cerr << "Error: Division by zero\n";
                        return -1;
                    }
                    s.push(op1 / op2);
                    break;
            }
        } else {
            cerr << "Invalid character in expression\n";
            return -1;
        }
    }

    if (s.size() != 1) {
        cerr << "Invalid expression: Too many operands\n";
        return -1;
    }

    return s.top();
}

int main() {
    string expr;
    cout << "Enter postfix expression: ";
    cin >> expr;
    int result = pf(expr);
    if (result != -1) {
        cout << result << endl;
    }
    return 0;
}
