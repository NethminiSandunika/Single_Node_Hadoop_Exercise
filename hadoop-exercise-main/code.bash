# Create a directory in HDFS (Hadoop Distributed File System) for input data
hdfs dfs -mkdir -p /user/hadoop/input

# Upload the local file `input.txt` to the HDFS directory `/user/hadoop/input`
hdfs dfs -put input.txt /user/hadoop/input

# Execute a Hadoop streaming job using the Hadoop Streaming JAR file
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input /user/hadoop/input/* \       # Specify the input directory in HDFS containing the data for the job
    -output /user/hadoop/output \      # Specify the output directory in HDFS to store the results
    -mapper mapper.py \                # Define the Python script (mapper.py) to be used as the Mapper
    -reducer reducer.py                # Define the Python script (reducer.py) to be used as the Reducer
