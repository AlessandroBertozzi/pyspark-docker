#!/usr/bin/env python3
"""
Test script per verificare il funzionamento del cluster Spark
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg
import time

def test_spark_cluster():
    print("🚀 Inizializzazione Spark Session...")
    
    # Crea Spark session
    spark = SparkSession.builder \
        .appName("ClusterTest") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("WARN")
    
    print(f"✅ Spark Version: {spark.version}")
    print(f"✅ Master: {spark.sparkContext.master}")
    print(f"✅ App Name: {spark.sparkContext.appName}")
    
    # Test parallelismo
    sc = spark.sparkContext
    print(f"✅ Default Parallelism: {sc.defaultParallelism}")
    
    # Test con dati
    print("\n📊 Creazione dataset di test...")
    data = [(i, f"user_{i}", i % 5) for i in range(1000)]
    df = spark.createDataFrame(data, ["id", "name", "group"])
    
    print(f"✅ Dataset creato: {df.count()} righe")
    
    # Test aggregazione
    print("\n⚡ Test aggregazione (verifica parallelismo)...")
    start_time = time.time()
    
    result = df.groupBy("group").agg(
        count("*").alias("count"),
        avg("id").alias("avg_id")
    ).collect()
    
    end_time = time.time()
    
    print(f"✅ Aggregazione completata in {end_time - start_time:.2f} secondi")
    print("📈 Risultati per gruppo:")
    for row in result:
        print(f"   Gruppo {row['group']}: {row['count']} elementi, avg_id = {row['avg_id']:.1f}")
    
    # Test cluster info
    print("\n🖥️ Informazioni Cluster:")
    print(f"✅ Master URL: {sc.master}")
    print(f"✅ Application ID: {sc.applicationId}")
    print(f"✅ Driver Host: {sc.getConf().get('spark.driver.host', 'unknown')}")
    
    # Test partizioni
    print(f"\n📦 Partizioni dataset: {df.rdd.getNumPartitions()}")
    
    # Test caching
    print("\n💾 Test caching...")
    df.cache()
    df.count()  # Trigger caching
    cached_count = df.count()  # Dovrebbe essere più veloce
    print(f"✅ Cache test completato: {cached_count} righe")
    
    spark.stop()
    print("\n🏁 Test completato con successo!")

if __name__ == "__main__":
    test_spark_cluster()