# Importing modules
from googleapiclient.discovery import build
import pandas as pd
from flask import Flask, render_template, request, send_file

# API information
api_service_name = "youtube"
api_version = "v3"
api_key = "YOUR_API_KEY"

# API client
youtube = build(api_service_name, api_version, developerKey=api_key)

# Declare a Flask app
app = Flask(__name__, template_folder='./templates', static_folder='./static')

# route to display the home page
@app.route('/',methods=['GET'])
def homePage():
    return render_template("index.html")

# route to display the output page
@app.route('/SearchResults', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            topic_name = request.form['topic'].strip()
            if not topic_name or topic_name.isspace():
                return render_template('index.html')

            nextPageToken = None
            info = {'id':[],'title':[],'channelTitle':[],'views':[],'likes':[],'duration':[],'datetime':[]}

            while len(info['id']) < 50:
                request_yt = youtube.search().list(part="id,snippet",
                                                type='video',
                                                order='relevance',
                                                q=topic_name,
                                                maxResults=50,
                                                fields="items(id(videoId),snippet(publishedAt,channelTitle,title))",
                                                pageToken=nextPageToken).execute()

                for item in request_yt['items']:
                    # Getting the id
                    if 'videoId' in item['id']:
                        vidId = item['id']['videoId']
                    # Getting stats of the video
                        r = youtube.videos().list(part="statistics,contentDetails",
                                                  id=vidId,
                                                  fields="items(statistics," + "contentDetails(duration))").execute()
                    try:
                        video_info = r['items'][0]
                        if 'videoId' in item['id']:
                            vidId = item['id']['videoId']
                            info['id'].append('https://www.youtube.com/watch?v=' + vidId)
                        else:
                            info['id'].append('')
                        if 'title' in item['snippet']:
                            info['title'].append(item['snippet']['title'])
                        else:
                            info['title'].append('')
                        if 'channelTitle' in item['snippet']:
                            info['channelTitle'].append(item['snippet']['channelTitle'])
                        else:
                            info['channelTitle'].append('')
                        if 'viewCount' in video_info['statistics']:
                            info['views'].append(video_info['statistics']['viewCount'])
                        else:
                            info['views'].append('')
                        if 'likeCount' in video_info['statistics']:
                            info['likes'].append(video_info['statistics']['likeCount'])
                        else:
                            info['likes'].append('')
                        if 'duration' in video_info['contentDetails']:
                            info['duration'].append(video_info['contentDetails']['duration'].replace('PT', ''))
                        else:
                            info['duration'].append('')
                        if 'publishedAt' in item['snippet']:
                            info['datetime'].append(item['snippet']['publishedAt'][:10])
                        else:
                            info['datetime'].append('')
                    except:
                        pass

                nextPageToken = request_yt.get('nextPageToken')
                if not nextPageToken:
                    break

            pd.DataFrame(data=info).to_csv("info.csv", index=False)
            return render_template('result.html', info=info)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    else:
        return render_template('index.html')

@app.route('/download')
def download_file():
    return send_file('info.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
