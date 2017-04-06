import soundcloud

#Authentication
"""
#-----------------------------------------
# create client object with app credentials
client = soundcloud.Client(client_id='YOUR_CLIENT_ID',
	client_secret='YOUR_CLIENT_SECRET',
	redirect_uri='http://example.com/callback')

# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# print out the user's username
print client.get('/me').username

# update the user's profile description
user = client.post('/me', description='I am using the SoundCloud API!')
print user.description
#------------------------------------------
"""
#Uploading Sounds
"""
#------------------------------------------

# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# upload audio file
track = client.post('/tracks', track={
    'title': 'This is my sound',
    'asset_data': open('file.mp3', 'rb')
})
# Updating metadata
# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# fetch a track by it's ID
track = client.get('/tracks/290')

# update the track's metadata
client.put(track.uri, track={
  'description': 'This track was recorded in Berlin',
  'genre': 'Electronic',
  'artwork_data': open('artwork.jpg', 'rb')
})

#Sharing sounds to other social Networks

# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# get a list of connected social networks
connections = client.get('/me/connections')

# print out connection details
for connection in connections:
    print "Connection type: %s" % connection.type
    if connection.post_favorite:
        print "Favorites are posted to this network"
    if connection.post_publish:
        print "New sounds and sets are shared"

#Creating sets

# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# create an array of track ids
tracks = map(lambda id: dict(id=id), [290, 291, 292])

# create the playlist
client.post('/playlists', playlist={
    'title': 'My new album',
    'sharing': 'public',
    'tracks': tracks
})
#------------------------------------------
"""
#Playing Sounds
"""
#------------------------------------------
# create a client object with your app credentials
client = soundcloud.Client(client_id='YOUR_CLIENT_ID')

# get a tracks oembed data
track_url = 'http://soundcloud.com/forss/flickermood'
embed_info = client.get('/oembed', url=track_url)
#------------------------------------------
"""
#Comments
"""
#------------------------------------------
# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# get the latest track from authenticated user
track = client.get('/me/tracks', limit=1)[0]

# create a new timed comment
comment = client.post('/tracks/%d/comments' % track.id, comment={
    'body': 'This is a timed comment',
    'timestamp': 1500
})

OR (getting a list of comments)

# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# get the latest track from authenticated user
track = client.get('/me/tracks', limit=1)[0]

# get a list of comments for the track
comments = client.get('/tracks/%d/comments' % track.id)

# print out each comment
for comment in comments:
    print comment.body
#------------------------------------------
"""
#Follow & Like
"""
#------------------------------------------
# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# Follow user with ID 3207
client.put('/me/followings/3207')

# Unfollow the same user
client.delete('/me/followings/3207')

# check the status of the relationship
try:
    client.get('/me/followings/3207')
except Exception, e:
    if e.response.status == '404':
        print 'You are not following user 3207'

# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# Fetch a track by it's ID
track = client.get('/tracks/290')

# Like the track
client.put('/me/favorites/%d' % track.id)
#------------------------------------------
"""
#Search
"""
#------------------------------------------
# create a client object with your app credentials
client = soundcloud.Client(client_id='YOUR_CLIENT_ID')

# find all sounds of buskers licensed under 'creative commons share alike'
tracks = client.get('/tracks', q='buskers', license='cc-by-sa')

# create a client object with your app credentials
client = soundcloud.Client(client_id='YOUR_CLIENT_ID')

# find all tracks with the genre 'punk' that have a tempo greater than 120 bpm.
tracks = client.get('/tracks', genres='punk', bpm={
    'from': 120
})
#------------------------------------------
"""

