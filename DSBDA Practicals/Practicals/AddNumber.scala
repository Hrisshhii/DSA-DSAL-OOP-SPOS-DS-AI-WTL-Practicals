object AddNumbers {
    def main(args: Array[String]): Unit = {
        val num1 = 10
        val num2 = 20
        val sum = num1 + num2

        println("First Number: " + num1)
        println("Second Number: " + num2)
        println("Sum: " + sum)
    }
}

/*
Step-1: Open Scala Shell
scala

Step-2: Simple Addition Directly
val a = 10
val b = 20
val sum = a + b

println(sum)

*/


/*
USING APACHE SPARK SHELL
STEP 1 — Open Spark Shell: spark-shell

STEP 2 — Run Program
val num1 = 10
val num2 = 20
val sum = num1 + num2
println("Sum = " + sum)

*/


/*
STEP 1 — Open CMD / PowerShell
java -version
scala -version

STEP 2 — Go to Spark Folder
cd C:\spark\spark-3.5.0-bin-hadoop3\bin

STEP 3 — Start Spark Shell
spark-shell

STEP 4 — Run Addition Program

Type:
val num1 = 10
val num2 = 20
val sum = num1 + num2
println("Sum = " + sum)

Install Ubuntu: 
sudo apt update
sudo apt install scala

Windows Install: 

Download:
Java JDK
Scala
Apache Spark
*/
