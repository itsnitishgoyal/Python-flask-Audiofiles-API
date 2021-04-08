# Python-flask-Audiofiles-API
This project includes flask REST API's which simulates the behavior of an audio file server
this includes 

Create API:
The request will have the following fields:
- audioFileType – mandatory, one of the 3 audio types possible
- audioFileMetadata – mandatory, dictionary, contains the metadata for one 
of the three audio files (song, podcast, audiobook)
Delete API:- The route will be in the following format: 
“<audioFileType>/<audioFileID>”
Update API:
- The route be in the following format: “<audioFileType>/<audioFileID>”
- The request body will be the same as the upload
Get API:
- The route “<audioFileType>/<audioFileID>” will return the specific audio 
file
- The route “<audioFileType>” will return all the audio files of that type
