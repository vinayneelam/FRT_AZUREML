# FRT_AZUREML

First in my Microsoft Azure Portal i have created a machine learning studio.

In the machine learning studio i've opted for designer to create my machine learning model.First i have created a training pipieline as shown in the image and ran it on compute instance to train it. The pipeline is as shown in this image.
![Web capture_27-2-2022_1113_ml azure com](https://user-images.githubusercontent.com/64788705/155910977-87bca99b-5b4e-4520-8c2f-a7de1c21db33.jpeg)

Then from the training pipeline i have created an real-time inference pipeline. It is as shown in the image.
![Web capture_27-2-2022_1146_ml azure com](https://user-images.githubusercontent.com/64788705/155911133-b6368181-c9c5-4f00-8c4d-e3b1fff2103b.jpeg)

I have included the codependencies and script files of the model in Trained_model file.

To deploy this real-time inference pipeline i've creates an inference cluster asnd AKS(Azure Kubernetes Service).
![Web capture_27-2-2022_1355_ml azure com](https://user-images.githubusercontent.com/64788705/155911417-9bdad9ec-1a37-47a5-929d-25e0d1d32730.jpeg)

Then i have attached the REST endpoint to this inference cluster, and deployed it. This generates a URL link and a primary key to use it for API.
![Web capture_27-2-2022_1428_ml azure com](https://user-images.githubusercontent.com/64788705/155911535-6b8b6bcd-4cf6-4f9b-9521-e0c73a507bc9.jpeg)

Using those API keys i have written a code to use it in Replit platform and then deployed it.
![Web capture_28-2-2022_74525_replit com](https://user-images.githubusercontent.com/64788705/155913261-88bf442f-f5f5-43a7-a4b6-eb761c1f17d3.jpeg)

It looks as follows when deployed.

![Web capture_28-2-2022_7428_replit com](https://user-images.githubusercontent.com/64788705/155913340-1cafdb97-6b48-4885-b88b-713f3ac776ac.jpeg)
![Web capture_28-2-2022_7447_replit com](https://user-images.githubusercontent.com/64788705/155913345-b65778a0-3866-48ed-bda5-d262ad09398d.jpeg)
