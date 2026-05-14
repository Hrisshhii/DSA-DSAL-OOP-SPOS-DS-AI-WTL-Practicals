import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    // Mapper Class
    public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();

        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {

            StringTokenizer itr = new StringTokenizer(value.toString());

            while (itr.hasMoreTokens()) {
                word.set(itr.nextToken());
                context.write(word, one);
            }
        }
    }

    // Reducer Class
    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values,Context context) throws IOException, InterruptedException {
            int sum = 0;

            for (IntWritable val : values) {
                sum += val.get();
            }

            result.set(sum);
            context.write(key, result);
        }
    }

    // Main Method
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word count");
        job.setJarByClass(WordCount.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}


/*
hadoop version
1. Create directory:
mkdir wordcount
cd wordcount

2. Create Java File:
gedit WordCount.java or nano WordCount.java

3. Set Hadoop Classpath
export HADOOP_CLASSPATH=$(hadoop classpath)

4. Compile Java Program
hadoop com.sun.tools.javac.Main WordCount.java
check (.class file): ls

5. Create JAR File
jar cf wc.jar WordCount*.class
check (wc.jar file): ls

6. Create Input File
gedit input.txt
add data: 
hello world
hello hadoop
hello big data

7. Create Input Directory in HDFS
hdfs dfs -mkdir /input

8. Copy File to HDFS
hdfs dfs -put input.txt /input

9. Run WordCount Program
hadoop jar wc.jar WordCount /input /output
if output file already existed: hdfs dfs -rm -r /output

10. View Output
hdfs dfs -cat /output/part-r-00000

*/



/*
COMPLETE COMMAND FLOW

mkdir wordcount
cd wordcount

gedit WordCount.java
export HADOOP_CLASSPATH=$(hadoop classpath)
hadoop com.sun.tools.javac.Main WordCount.java
jar cf wc.jar WordCount*.class

gedit input.txt
hdfs dfs -mkdir /input
hdfs dfs -put input.txt /input
hadoop jar wc.jar WordCount /input /output
hdfs dfs -cat /output/part-r-00000
*/

/*
IF HDFS COMMANDS FAIL:
start hadoop services:
start-dfs.sh
start-yarn.sh
*/
