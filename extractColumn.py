import csv
import pandas as pd
data = pd.read_csv('logs\Zookeeper\Zookeeper_2k.log_structured.csv', usecols = ['LineId','EventId'])
log = pd.read_csv('logs\Zookeeper\Zookeeper_2k.log_structured.csv', usecols = ['Content'])

data.to_csv('E:/logData/benchmark/dataSet/Zookeeper/id.csv', index = False)
log.to_csv('E:/logData/benchmark/dataSet/Zookeeper/log.csv', index = False)