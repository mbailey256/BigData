pipe data into mapper and reducer code

echo "foo foo quux labs foo bar quux" | ./mapper.py | sort -k1,1 | ./reducer.py


submit to Hadoop via streams

bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar -file ~/dev/mapper.py -mapper ~/dev/mapper.py -file ~/dev/reducer.py -reducer ~/dev/reducer.py -input /user/hduser/gutenberg/* -output /user/hduser/gutenberg-output-py


