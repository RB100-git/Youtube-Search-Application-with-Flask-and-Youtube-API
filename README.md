# Youtube-Search-Application-with-Flask-and-Youtube-API



https://user-images.githubusercontent.com/102472369/229731473-9aed0d40-0ada-4f6e-ab75-f61f8be62155.mp4


## Introduction
A Python web application has been created using Flask that allows users to search for YouTube videos based on a given topic and retrieves relevant video data such as video Id, video title, channel name, view count, likes count, duration and the published date. The YouTube API gives us access to YouTube’s data in a more comprehensive, scalable way than standalone YouTube embed codes would. The data is then saved to a CSV file for further analysis and can be downloaded by the user. 

![image](https://user-images.githubusercontent.com/102472369/229737807-7d0563c1-051c-4c85-ab8a-4cb074b85cfb.png)
![image](https://user-images.githubusercontent.com/102472369/229738188-e8b1cee9-a7d7-4645-9b6a-d13acfe1e37e.png)
                              
*Source: Visualmodo*

## Installation
To interact with the YouTube API from the Flask application, we need the **google-api-python-client library**.

```
pip install google-api-python-client
```

## Getting an API key
Firstly sign in here **[Google Cloud Platform](https://console.cloud.google.com/)** with your google account. Click on **select a project** and then click **New Project**.

![image](https://user-images.githubusercontent.com/102472369/229764003-05213c2d-49e7-45be-bf39-352c7d53462b.png)

You will be then redirected to **new projec**t page. Name your project and click **create**.

![image](https://user-images.githubusercontent.com/102472369/229765047-9a91201f-e494-495e-993a-b8610c68af60.png)

Now you need to enable your API in the **Dashboard** window and click on **explore and enable APIs**.
![image](https://user-images.githubusercontent.com/102472369/229766889-ca14cdf6-1629-4e33-b9cb-3ee3dd362c79.png)

Next, click on **ENABLE APIS AND SERVICES**. And then choose **Youtube Data API V3** from **API library**
![image](https://user-images.githubusercontent.com/102472369/229767686-30d6a353-c3ac-4403-88bd-cd46e48b775c.png)
After that, the informations of **Youtube Data API V3** will be visible to you. You need click on **Enable** option there.
Then you will be redirected to API overview window and you have to click on **create credentials** option. After clicking on it, you can see **credential type**
where you you have to select credential type as **Youtube Data API V3** and check the **Public Data** box and then click **Next** to finish. The API Key will finally be visible to you.

## Project Execution
![image](https://user-images.githubusercontent.com/102472369/229835736-047504de-c3e8-4b27-bdf4-7373c3c65b67.png)

## Summary

The application has three routes:

The first route is the home page, which displays the index.html template(with main.css file).
The second route is the search results page, which is the output page, displays the result.html template(with style.css file).
The third route is the download file page, which helps to download the relevant informations in a CSV format.

When the user enters a search query on the home page and submits the form, the search results page is loaded with the search results based on the user's query.

The code first stores the API Informations of Youtube API V3(such as service name, version and API Key).The **build** function from google api client Construct a Resource for interacting with an API. Then we have created an instance of the Flask class and sets the template and static folders. Then, it defines the three routes using the @app.route decorator. 

In the code, I have used **while loop**. Without the while loop, the code would just make a single request to get the first page of results and return whatever videos are returned in that one request. We have nextpagetoken to get unique results or a new set of results everytime the API make requests.

The code then retrieves the video statistics and content details for each video in the search results and stores the relevant information (video ID, title, channel name, views, likes, duration, and published datetime) in a dictionary called 'info'. It keeps making API requests using nextPageToken to get the next page of results until it has collected at least 50 videos.If we don't use the nextPageToken to iterate through the pages and the API returns fewer than 50 results, the code will not enter the while loop and will continue to execute the remaining code. Though the API has no expiration but it has a limited quota usage. The quota allocation for everyone is of 10,000 units per day. The consumption of this units is based on the methods you execute and the result size does not matter(the parameter maxresults is basically the maximum number of items per query, which is 50 and by default 5).

Finally, the code renders the result.html template, passing in the 'info' dictionary as a parameter to be used for displaying the search results.
