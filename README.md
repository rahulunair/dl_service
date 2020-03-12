## Serverless app for image classification using OpenFaas and PyTorch

- Base Pytorch framework docker image
- An Efficientnet based classification model for image recognition
- A simple web application to upload an image and get result

<p align="center">
  <img src=http://imgur.com/on0ebtc.png alt="screenshot" height="300" width="450">
</p>
Services communication

Web app to image recognition service:
- Event based faas using OpenFaas
- File IO
- REST API using Flask
