package edu.gatech.cse6242

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object Q2 {
  def main(args: Array[String]) {
    val sc = new SparkContext(new SparkConf().setAppName("Q2"))

    // read the file
    val file = sc.textFile("hdfs://localhost:8020" + args(0))

    /* TODO: Needs to be implemented */
    
    val data = file.map(line=>line.split("\t")).filter(_.last != "1")
    val outbound = data.map(line => (line(0), line(2).toInt*(-1))).reduceByKey(_+_,1)
    val inbound = data.map(line => (line(1), line(2).toInt)).reduceByKey(_+_,1)
    val bound = inbound.join(outbound)
    val bounds = bound.mapValues{case (x,y) => x+y}
    val output = bounds.collect.map(line => line._1 + "\t" + line._2)
    
    // store output on given HDFS path.
    // YOU NEED TO CHANGE THIS
    sc.makeRDD(output).saveAsTextFile("hdfs://localhost:8020" + args(1))
  }
}
