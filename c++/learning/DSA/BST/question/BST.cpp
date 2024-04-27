#include <iostream>

using namespace std;

// Node class for the binary search tree
class Node {
public:
    int data;
    Node* left;
    Node* right;

    // Constructor
    Node(int value) {
        data = value;
        left = nullptr;
        right = nullptr;
    }
};

// Binary Search Tree class
class BST {
private:
    Node* root;

    // Helper function for insertion
    Node* insertRec(Node* root, int value) {
        if (root == nullptr) {
            return new Node(value);
        }
        if (value < root->data) {
            root->left = insertRec(root->left, value);
        }
        else if (value > root->data) {
            root->right = insertRec(root->right, value);
        }
        return root;
    }

    // Helper function for inorder traversal
    void inorderRec(Node* root) {
        if (root != nullptr) {
            inorderRec(root->left);
            cout << root->data << " ";
            inorderRec(root->right);
        }
    }

public:
    // Constructor
    BST() {
        root = nullptr;
    }

    // Function to insert a node
    void insert(int value) {
        root = insertRec(root, value);
    }

    // Function to perform inorder traversal
    void inorderTraversal() {
        inorderRec(root);
    }
};

// Main function
int main() {
    BST bst;

    // Insert elements into the BST
    bst.insert(50);
    bst.insert(30);
    bst.insert(20);
    bst.insert(40);
    bst.insert(70);
    bst.insert(60);
    bst.insert(80);

    // Perform inorder traversal
    cout << "Inorder Traversal of the BST: ";
    bst.inorderTraversal();
    cout << endl;

    return 0;
}
