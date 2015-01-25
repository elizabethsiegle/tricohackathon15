#!/usr/bin/env python
# encoding: utf-8
 
import tweepy #https://github.com/tweepy/tweepy
import csv
import string
#Twitter API credentials
consumer_key = "ij4VtO4hHboL3FqjFgoITcS9q"
consumer_secret = "G0E8w8GyU75rjAPtErvYsDGVWLJx7Xxrm0lfCKMomgDYU4HINH"
access_key = "2948645217-fZ24m4IcL45ZusI0eVRx7EOr7nPrAMNYWUIaNnD"
access_secret = "dDTNyPQpdTFfY5DLlpJRUMNimUDhbN1FfG8jSc2GEWRqN"

def get_all_tweets(screen_name, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	tweets = [tweet.text.encode("utf-8") for tweet in alltweets]
	
	#write the csv	
	#with open('%s_tweets.csv' % screen_name, 'wb') as f:
	#	writer = csv.writer(f)
	#	writer.writerow(["id","created_at","text"])
	#	writer.writerows(outtweets)
	
	lstNum = []
	lst = []
	n = 0
	word = ""
	hashcount = 0
	end = False
	for i in range(0, len(tweets)):
		s = tweets[i].lower() 
		s = s + " "
		s = ''.join([c for c in s if c not in ('\'', '.', ',', '?', '\\', '$', '/', '*', '!', '\"', ';', ':', '”', '(', ')')]) 
		for x in range(0, len(s)):
			if s[x] == "#":
				hashcount += 1
				x += 1
				while s[x] != " ":
					word += s[x]
					x += 1
				for y in range(0, len(lst)):
					if word == lst[y]:
						lstNum[y] += 1
						end = True
				if not end:
					lst.append(word)
					lstNum.append(1)
				else:
					end = False
				word = ""
				n += 1
	if hashcount < 25:
		print "here"
		return "You do not have enough hastags in your tweets to make an accurate prediction. Please come back when you have more hashtags."
	#for i in range(0, len(lst)):
	#	print lst[i]
	
	# find hastag job
	twittertype = ""
	hashjob = list( csv.reader(open('hashtojob.csv', 'rU')))
	job1 = "Architecture, Planning & Environmental Design"
	njob1 = 0
	job2 = "Arts & Entertainment"
	njob2 = 0
	job3 = "Business"
	njob3 = 0
	job4 = "Communications"
	njob4 = 0
	job5 = "Education"
	njob5 = 0
	job6 = "Engineering & Computer Science"
	njob6 = 0
	job7 = "Environment"
	njob7 = 0
	job8 = "Government"
	njob8 = 0
	job9 = "Health & Medicine"
	njob9 = 0
	job10 = "International"
	njob10 = 0
	job11 = "Law & Public Policy"
	njob11 = 0
	job12 = "Nonprofit"
	njob12 = 0
	job13 = "Sciences-Biological & Physical"
	njob13 = 0
	job14 = "Athletics"
	njob14 = 0
	for job in range(0, len(hashjob)):
		for hash in range(0, len(lst)):
			if lst[hash] == hashjob[job][0]:
				if hashjob[job][1] == job1:
					njob1 += lstNum[hash]
				elif hashjob[job][1] == job2:
					njob2 += lstNum[hash]
				elif hashjob[job][1] == job3:
					njob3 += lstNum[hash]
				elif hashjob[job][1] == job4:
					njob4 += lstNum[hash]
				elif hashjob[job][1] == job5:
					njob5 += lstNum[hash]
				elif hashjob[job][1] == job6:
					njob6 += lstNum[hash]
				elif hashjob[job][1] == job7:
					njob7 += lstNum[hash]
				elif hashjob[job][1] == job8:
					njob8 += lstNum[hash]
				elif hashjob[job][1] == job9:
					njob9 += lstNum[hash]
				elif hashjob[job][1] == job10:
					njob10 += lstNum[hash]
				elif hashjob[job][1] == job11:
					njob11 += lstNum[hash]
				elif hashjob[job][1] == job12:
					njob12 += lstNum[hash]
				elif hashjob[job][1] == job13:
					njob13 += lstNum[hash]
				elif hashjob[job][1] == job14:
					njob14 += lstNum[hash]
				break
	maxn = njob1;
	maxs = job1
	if njob2 > maxn:
		maxn = njob2
		maxs = job2
	if njob3 > maxn:
		maxn = njob3
		maxs = job3	
	if njob4 > maxn:
		maxn = njob4
		maxs = job4	
	if njob5 > maxn:
		maxn = njob5
		maxs = job5
	if njob6 > maxn:
		maxn = njob6
		maxs = job6
	if njob7 > maxn:
		maxn = njob7
		maxs = job7	
	if njob8 > maxn:
		maxn = njob8
		maxs = job8	
	if njob9 > maxn:
		maxn = njob9
		maxs = job9
	if njob10 > maxn:
		maxn = njob10
		maxs = job10	
	if njob11 > maxn:
		maxn = njob11
		maxs = job11	
	if njob12 > maxn:
		maxn = njob12
		maxs = job12	
	if njob13 > maxn:
		maxn = njob13
		maxs = job13				
	if njob14 > maxn:
		maxn = njob14
		maxs = job14	
	twittertype = maxs
	print twittertype
	
	
	
	
	
	
	#print lstNum
	max(lstNum)
	index = lstNum.index(max(lstNum))
	one = lst[index]
	del lst[index]
	del lstNum[index]
	index = lstNum.index(max(lstNum))
	two = lst[index]
	del lst[index]
	del lstNum[index]
	index = lstNum.index(max(lstNum))
	three = lst[index]
	print one
	print two
	print three
	
	
	
	e=0
	i=0
	s=0
	n=0
	t=0
	f=0
	p=0
	j=0
	if a1 == 'a':
		e += 1
	else:
		i += 1
	if a2 == 'a':
		i += 1
	else:
		e +=1
	if a3 == 'a':
		e += 1
	else:
		i +=1
	if a4 == 'a':
		s += 1
	else:
		n +=1
	if a5 == 'a':
		n += 1
	else:
		s +=1
	if a6 == 'a':
		n += 1
	else:
		s +=1
	if a7 == 'a':
		t += 1
	else:
		f +=1
	if a8 == 'a':
		t += 1
	else:
		f +=1
	if a9 == 'a':
		f += 1
	else:
		t +=1
	if a10 == 'a':
		j += 1
	else:
		p +=1
	if a11 == 'a':
		p += 1
	else:
		j +=1
	if a12 == 'a':
		p += 1
	else:
		j +=1
	type = ""
	if e >= 2:
		type += "E"
	else:
		type += "I"
	if s >= 2:
		type += "S"
	else:
		type += "N"
	if t >= 2:
		type += "T"
	else:
		type += "F"
	if p >= 2:
		type += "P"
	else:
		type += "J"
	print type
	xindex = 0
	yindex = 0
	array = list( csv.reader(open('jobs.csv', 'rU')))
	for i in range(0, len(array[1])):
		if type == array[1][i]:
			xindex = i
			print "x"
			print xindex
			break
	for i in range(0, len(array)):
		if twittertype == array[i][0]:
			yindex = i
			print "y"
			print yindex
			break
	
	print array[yindex][xindex]
	
	return array[yindex][xindex]
	 
 
"""if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("lizziepika",'a', 'b', 'b', 'b', 'b', 'a', 'b', 'b', 'b', 'a', 'b', 'a',)"""
