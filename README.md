# Youtube-Search-Application-with-Flask-and-Youtube-API



https://user-images.githubusercontent.com/102472369/229731473-9aed0d40-0ada-4f6e-ab75-f61f8be62155.mp4


## Introduction
A Python web application has been created using Flask that allows users to search for YouTube videos based on a given topic and retrieves relevant video data such as video Id, video title, channel name, view count, likes count, duration and the published date. The YouTube API gives us access to YouTube’s data in a more comprehensive, scalable way than standalone YouTube embed codes would. The data is then saved to a CSV file for further analysis and can be downloaded by the user. 

![image](https://user-images.githubusercontent.com/102472369/229737807-7d0563c1-051c-4c85-ab8a-4cb074b85cfb.png)
![image](https://user-images.githubusercontent.com/102472369/229738188-e8b1cee9-a7d7-4645-9b6a-d13acfe1e37e.png)
                              
*Source: Visualmodo*

## Installation
```pip install google-api-python-client```

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
