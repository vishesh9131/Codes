#include<iostream>

using namespace std;

class TreeNode {
public:
    int data;
    TreeNode* leftChild;
    TreeNode* rightChild;

    TreeNode(int value) : data(value), leftChild(nullptr), rightChild(nullptr) {}
};

class BinarySearchTree {
public:
    TreeNode* insert(TreeNode* root, int data) {
        if (root == nullptr) {
            TreeNode* newNode = new TreeNode(data);
            return newNode;
        } else if (data < root->data) {
            root->leftChild = insert(root->leftChild, data);
        } else {
            root->rightChild = insert(root->rightChild, data);
        }
        return root;
    }

    void printPreorder(TreeNode* node) {
        if (node == nullptr)
            return;
        printPreorder(node->leftChild);
        cout << node->data << "\t";
        printPreorder(node->rightChild);
    }

    void printInorder(TreeNode* node) {
        if (node == nullptr)
            return;
        printInorder(node->leftChild);
        cout << node->data << "\t";
        printInorder(node->rightChild);
        
    }

    void printPostorder(TreeNode* node) {
        if (node == nullptr)
            return;
        printPostorder(node->leftChild);
        cout << node->data << "\t";
        printPostorder(node->rightChild);
    }
};

int main() {
    BinarySearchTree bst;
    TreeNode* root = nullptr;
    int c = 0, value;
    while (c != 7) {
        cout << "\nEnter 1 for Insertion";
        cout << "\nEnter 2 for Deletion";
        cout << "\nEnter 3 for Searching";
        cout << "\nEnter 4 for Postorder";
        cout << "\nEnter 5 for Preorder";
        cout << "\nEnter 6 for Inorder";
        cout << "\nEnter 7 for Exit";
        cout << "\nEnter your choice: ";
        cin >> c;
        switch (c) {
            case 1: {
                cout << "\nEnter value: ";
                cin >> value;
                root = bst.insert(root, value);
                break;
            }
            case 2: {
                cout << "\nEnter value to delete: ";
                cin >> value;
                // delete(value);
                break;
            }
            case 3: {
                cout << "\nEnter value to search: ";
                cin >> value;
                // search(value);
                break;
            }
            case 4: {
                bst.printPostorder(root);
                break;
            }
            case 5: {
                bst.printPreorder(root);
                break;
            }
            case 6: {
                bst.printInorder(root);
                break;
            }
            case 7: {
                break;
            }
            default: {
                cout << "\nInvalid Choice";
                break;
            }
        }
    }
    return 0;
}
