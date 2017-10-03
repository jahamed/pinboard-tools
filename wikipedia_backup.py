import credentials
import pinboard

api_token = credentials.login['token']
pb = pinboard.Pinboard(api_token)

# Don't know why this library returns a map for recent() and a list for all()
# wikimarks = pb.posts.recent(tag=["wikipedia"])
# print(wikimarks['posts'][0].url)

# output_file = open('wikipedia.txt', 'w')

# for wikimark in wikimarks['posts']:
# 	output_file.write("%s\n" % wikimark.url)

# output_file.close()

wikimarks = pb.posts.all(tag=["wikipedia"])
# print(wikimarks)

output_file = open('wikipedia.txt', 'w')

for wikimark in wikimarks:
	output_file.write("%s\n" % wikimark.url)

output_file.close()