/*The Load functions was taken from the assignment write up.  Not sure how comments work in pig?
I was getting errors trying to get the first two steps on Hadoop, saying I can't write to a file. I know I have them completed, with the test work in Grunt. My code for this bonus assignment is below.

My counts also was shooting out an error in grunt; saying there was too many values.  Not sure if that was just a warning or if there was actually an error. If it was just a warning, then Step 3 should be done (but same writing files problem).

As far as Step 4,  I know that it is wrong, I grabbed the code from the assignment writeup, and am unsure if that's how it is supposed to look in pig.

But I think I used the STORE function correctly at the end? I would actually be interesting in seeing how Step 4 is actually done. 

Danny helped me figure out my approach in office hours.
Thanks Danny!!!!!

2014-02-28 21:53:13,357 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Failed!
2014-02-28 21:53:13,371 [main] ERROR org.apache.pig.tools.grunt.GruntParser - ERROR 2244: Job failed, hadoop does not return any error message
2014-02-28 21:53:13,371 [main] WARN  org.apache.pig.tools.grunt.GruntParser - Could not write to log file: ~/apache-pig.log :~/apache-pig.log (No such file or directory)
2014-02-28 21:53:13,371 [main] ERROR org.apache.pig.tools.grunt.GruntParser - org.apache.pig.backend.executionengine.ExecException: ERROR 2244: Job failed, hadoop does not return any error message 

I think this is how you comment code in Pig?
*/
yelps = LOAD 'yelp_review.json' USING JsonLoader('votes:map[], user_id:chararray, review_id:chararray, stars:int, date:chararray, text:chararray, type:chararray, business_id:chararray');
yelptext = FOREACH yelps GENERATE flatten(TOKENIZE(text)) AS word, stars;
positive = FILTER yelptext by stars >=5;
negative = FILTER yelptext by stars <=2;
positiveGroup = GROUP positive BY (word);
negativeGroup = GROUP negative BY (word);
all_review = GROUP yelptext BY (word);
positive2 = FOREACH positiveGroup GENERATE COUNT(positive) as countPositive, group;
negative2 = FOREACH negativeGroup GENERATE COUNT(negative) as countNegative, group;
all_reviews = FOREACH all_review GENERATE COUNT(yelptext) as countAll, group;
STORE all_reviews INTO 'output-step-1a';
STORE positive2 INTO 'output-step-1b';
STORE negative2 INTO 'output-step-1c';
all_reviews2 = FILTER all_reviews by countAll >= 1000;
positiveJoin = JOIN all_reviews by (group, countAll), positive2 by (group, countPositive);
negativeJoin = JOIN all_reviews by (group, countAll), negative2 by (group, countNegative);
STORE positiveJoin INTO 'output-step-2a';
STORE negativeJoin INTO 'output-step-2b';
positivity = LOAD 'output-step-2a' AS (word, countAll, word, CountPositive);
negativity = LOAD 'output-step-2b' AS (word, countAll, word, CountNegative);
Positivity(word) = log P(word in positivity) – log P(word in all_reviews); 
Negativity(word) = log P(word in negativity) - log P(word in all_reviews);
STORE Positivity(word) INTO 'output-positive';
STORE Negativity(word) INTO 'output-negative';






