#include<iostream>
using namespace std;

class icecream {
public:
    int prn;
    icecream* next;

    icecream* adding(icecream* head, int roll) {
        icecream* flavour = new icecream;
        flavour->prn = roll;
        flavour->next = NULL;
        if (head == NULL) {
            return flavour;
        }

        icecream* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = flavour;
        return head;
    }

    void display(icecream* head) {
        if (head == NULL) {
            cout << "List is empty!" << endl;
            return;
        }
        icecream* temp = head;
        while (temp != NULL) {
            cout << temp->prn;
            if (temp->next != NULL)
                cout << "->";
            temp = temp->next;
        }
        cout << endl;
    }

    icecream* intersection(icecream* van, icecream* but) {
        icecream* result = NULL;
        icecream* p = van;
        while (p != NULL) {
            icecream* q = but;  // Reset q for each p
            while (q != NULL) {
                if (p->prn == q->prn) {
                    result = adding(result, p->prn);
                    break;
                }
                q = q->next;
            }
            p = p->next;
        }
        return result;
    }

    icecream* Unionset(icecream* van, icecream* but) {
        icecream* result = NULL;
        icecream* p = van;
        while (p != NULL) {
            result = adding(result, p->prn);
            p = p->next;
        }
        icecream* q = but;
        while (q != NULL) {
            p = van;
            bool found = false;
            while (p != NULL) {
                if (q->prn == p->prn) {
                    found = true;
                    break;
                }
                p = p->next;
            }
            if (!found) {
                result = adding(result, q->prn);
            }
            q = q->next;
        }
        return result;
    }

    int count(icecream* head) {
        int cnt = 0;
        icecream* i = head;
        while (i != NULL) {
            cnt++;
            i = i->next;
        }
        return cnt;
    }

    int countneither(icecream* van, icecream* but, int total) {
        icecream* uni = Unionset(van, but);
        int counter = count(uni);
        return total - counter;
    }
};

int main() {
    icecream* vanilla = NULL, * butterscotch = NULL;
    icecream flav;
    int roll, total, choice, option;
    cout << "Enter the Total number of students: ";
    cin >> total;
    do {
        cout << "\n*******************MENU*******************\n"
            << "1. ADD MEMBER\n2. DISPLAY MEMBERS\n3. WHO LIKE BOTH\n4. WHO LIKE EITHER\n5. WHO LIKE NEITHER\n6. EXIT\n";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "\nWhat flavour to add?\n1. Vanilla\n2. Butterscotch\n";
            cin >> option;
            if (option == 1) {
                cout << "Enter the roll no of student who likes Vanilla: ";
                cin >> roll;
                vanilla = flav.adding(vanilla, roll);
            }
            else if (option == 2) {
                cout << "Enter the roll no of student who likes Butterscotch: ";
                cin >> roll;
                butterscotch = flav.adding(butterscotch, roll);
            }
            else {
                cout << "Invalid choice!" << endl;
            }
            break;

        case 2:
            cout << "Whom to display?\n1. People who like Vanilla\n2. People who like Butterscotch\n";
            cin >> option;
            if (option == 1) {
                flav.display(vanilla);
            }
            else if (option == 2) {
                flav.display(butterscotch);
            }
            else {
                cout << "Invalid choice!" << endl;
            }
            break;

        case 3: {
            icecream* both = flav.intersection(vanilla, butterscotch);
            cout << "\nStudents who like both Vanilla and Butterscotch: ";
            flav.display(both);
            break;
        }
        case 4: {
            icecream* either = flav.Unionset(vanilla, butterscotch);
            cout << "Students who like either Vanilla or Butterscotch or both: ";
            flav.display(either);
            break;
        }
        case 5: {
            int neither = flav.countneither(vanilla, butterscotch, total);
            cout << "Number of students who like neither Vanilla nor Butterscotch: " << neither << endl;
            break;
        }
        case 6: {
            cout << "Exiting the program. Goodbye!" << endl;
            break;
        }
        default:
            cout << "INVALID CHOICE. PLEASE TRY AGAIN!" << endl;
        }
    } while (choice != 6);

    return 0;
}
