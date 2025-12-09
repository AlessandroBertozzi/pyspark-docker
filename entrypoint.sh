#!/bin/bash

SPARK_WORKLOAD=$1

echo "SPARK_WORKLOAD: $SPARK_WORKLOAD"

if [ "$SPARK_WORKLOAD" == "master" ];
then
  start-master.sh -p 7077 &
  cd /opt/spark/notebooks
  jupyter notebook --no-browser --allow-root --ip=0.0.0.0 --port=8889
elif [[ $SPARK_WORKLOAD =~ "worker" ]];
# if $SPARK_WORKLOAD contains substring "worker". try 
# try "worker-1", "worker-2" etc.
then
  start-worker.sh spark://spark-master:7077
elif [ "$SPARK_WORKLOAD" == "history" ]
then
  start-history-server.sh
fi
