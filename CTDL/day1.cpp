#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // For finding/removing items

using namespace std;

// ==========================================
// 1. Abstract Base Class: Document
// ==========================================
class Document {
protected:
    // Protected allows derived classes (Book/Magazine) to access these directly
    int id;
    string title;

public:
    // Constructor
    Document(int id, string title) : id(id), title(title) {}

    // Virtual Destructor: Essential for polymorphism.
    // It ensures the correct destructor is called when deleting a derived object via a base pointer.
    virtual ~Document() {}

    // Getter for ID (needed for search functions)
    int getId() const {
        return id;
    }

    // Pure Virtual Function: Makes this an Abstract Class
    virtual void display() const = 0; 
};

// ==========================================
// 2. Derived Class: Book
// ==========================================
class Book : public Document {
private:
    string author;

public:
    Book(int id, string title, string author) 
        : Document(id, title), author(author) {}

    // Override display to show Book-specific details
    void display() const override {
        cout << "[Book] ID: " << id 
             << " | Title: " << title 
             << " | Author: " << author << endl;
    }
};

// ==========================================
// 3. Derived Class: Magazine
// ==========================================
class Magazine : public Document {
private:
    int issueNumber;

public:
    Magazine(int id, string title, int issueNumber) 
        : Document(id, title), issueNumber(issueNumber) {}

    // Override display to show Magazine-specific details
    void display() const override {
        cout << "[Magazine] ID: " << id 
             << " | Title: " << title 
             << " | Issue #: " << issueNumber << endl;
    }
};

// ==========================================
// 4. Class Library (Manager)
// ==========================================
class Library {
private:
    // Vector of pointers to Document allows us to store both Books and Magazines
    vector<Document*> documents; 

public:
    // Destructor to free memory allocated for documents
    ~Library() {
        for (Document* doc : documents) {
            delete doc;
        }
        documents.clear();
    }

    void addDocument(Document* doc) {
        documents.push_back(doc);
        cout << "Document added successfully.\n";
    }

    void showAll() const {
        if (documents.empty()) {
            cout << "Library is empty.\n";
            return;
        }
        cout << "\n--- Library Contents ---\n";
        for (const auto* doc : documents) {
            doc->display(); // Polymorphism in action!
        }
        cout << "------------------------\n";
    }

    void findById(int id) const {
        bool found = false;
        for (const auto* doc : documents) {
            if (doc->getId() == id) {
                cout << "\nDocument Found:\n";
                doc->display();
                found = true;
                break;
            }
        }
        if (!found) cout << "Document with ID " << id << " not found.\n";
    }

    void removeById(int id) {
        // Iterate through the vector to find the element
        for (auto it = documents.begin(); it != documents.end(); ++it) {
            if ((*it)->getId() == id) {
                delete *it; // Free the memory first!
                documents.erase(it); // Remove the pointer from the vector
                cout << "Document with ID " << id << " removed.\n";
                return;
            }
        }
        cout << "Document with ID " << id << " not found.\n";
    }
};

// ==========================================
// 5. Main Program
// ==========================================
int main() {
    Library lib;
    int choice;
    
    // Variables for input
    int id, issueNum;
    string title, author;

    do {
        cout << "\n=== Library Management System ===\n";
        cout << "1. Add Book\n";
        cout << "2. Add Magazine\n";
        cout << "3. Show All Documents\n";
        cout << "4. Find Document by ID\n";
        cout << "5. Remove Document by ID\n";
        cout << "6. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        // Input validation to prevent infinite loops on bad input
        if(cin.fail()) {
            cin.clear(); cin.ignore(1000, '\n'); 
            continue;
        }

        switch (choice) {
            case 1:
                cout << "Enter ID: "; cin >> id;
                cin.ignore(); // Clear buffer before string input
                cout << "Enter Title: "; getline(cin, title);
                cout << "Enter Author: "; getline(cin, author);
                // Dynamically allocate memory for a new Book
                lib.addDocument(new Book(id, title, author));
                break;

            case 2:
                cout << "Enter ID: "; cin >> id;
                cin.ignore();
                cout << "Enter Title: "; getline(cin, title);
                cout << "Enter Issue Number: "; cin >> issueNum;
                lib.addDocument(new Magazine(id, title, issueNum));
                break;

            case 3:
                lib.showAll();
                break;

            case 4:
                cout << "Enter ID to find: "; cin >> id;
                lib.findById(id);