BUDGET BUDDY API

This is a personal project. I created this project because of the money manager app I am currently using. I encounter a limitation in the number of accounts so I decided to create my own project wherein the model will be based from it with additionoal features. As of now, I have not think about any customization but still it is a progress for me to showcase what can I do because of my curiosity.

As of now this is just the backend system. I will try to create a frontend system for this so that I can use it wherever I am either using a mobile application or a web application.

June 2, 2024
- Initialized the project.
- Create Tracker abstract model.
- Create authentication app.
- Create Custom User model and serializer
- Implement simple-jwt for Authentication
    - Create LoginView by customizing TokenObtainPairSerializer
    - Create endpoint for verify and refresh token
    - Create LogoutView using RefreshToken from simple-jwt

June 3, 2024
- Create finance app.
- Create new models:
    - Account = 
    - Account Group = 
    - Cashflow: Income and Expense = 
    - Transaction = 
- Create Serializer class for each model in finance app.
- Initialize finance.views.