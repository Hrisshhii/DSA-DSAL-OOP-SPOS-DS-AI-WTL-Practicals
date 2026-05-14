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

public class LogProcessor {

    // Mapper Class
    public static class LogMapper
            extends Mapper<Object, Text, Text, IntWritable> {

        private final static IntWritable one = new IntWritable(1);

        private Text logType = new Text();

        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {

            String line = value.toString();

            StringTokenizer itr = new StringTokenizer(line);

            if (itr.hasMoreTokens()) {

                String type = itr.nextToken();

                logType.set(type);

                context.write(logType, one);
            }
        }
    }

    // Reducer Class
    public static class LogReducer
            extends Reducer<Text, IntWritable, Text, IntWritable> {

        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values,
                           Context context)
                throws IOException, InterruptedException {

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

        Job job = Job.getInstance(conf, "log processor");

        job.setJarByClass(LogProcessor.class);

        job.setMapperClass(LogMapper.class);

        job.setCombinerClass(LogReducer.class);

        job.setReducerClass(LogReducer.class);

        job.setOutputKeyClass(Text.class);

        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));

        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}


/*
STEP 1 — Compile
hadoop com.sun.tools.javac.Main LogProcessor.java

STEP 2 — Create JAR
jar cf log.jar LogProcessor*.class

STEP 3 — Create Log File

logfile.txt
INFO System started
ERROR Disk failure
INFO User login
WARNING Memory low
ERROR Network issue
INFO Shutdown

STEP 4 — Create Input Folder
hdfs dfs -mkdir /loginput

STEP 5 — Put File into HDFS
hdfs dfs -put logfile.txt /loginput

STEP 6 — Run Program
hadoop jar log.jar LogProcessor /loginput /logoutput

STEP 7 — View Output
hdfs dfs -cat /logoutput/part-r-00000
*/
