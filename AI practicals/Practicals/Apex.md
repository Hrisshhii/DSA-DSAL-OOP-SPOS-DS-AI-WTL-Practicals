1. Open Salesforce Setup: Gear Icon → Setup
2. Create Custom Object: Setup → Object Manager → Create → Custom Object
3. Create Custom Fields
4. Create tabs for app interface: Setup → Tabs
   - Under Custom Object Tabs
   - Select New Tab
   - Select the object
5. Add Student Tab to App: Setup → App Manager
6. Open Developer Console: Gear Icon → Developer Console
7. File → New → Apex Class
8. Apex code: 
```
public class HelloWorld {

    public static void sayHello() {

        Student__c s = new Student__c();

        s.Name = 'Hrishi';
        s.Roll_No__c = 101;
        s.Branch__c = 'Computer';

        insert s;

        System.debug('Student Record Inserted');
    }
}
```

9. Execute Apex Code: Debug → Open Execute Anonymous Window and write: HelloWorld.sayHello();
10. View Inserted Record
