# fitbit-run-viz
Custom visualisation of runs logged through Fitbit

## 1. App Setup
### 1.1. App Registration
Go to https://dev.fitbit.com/apps and click "Register a new app". It will have several unpleasant-seeming fields that seem appropriate to a serious company. I just filled them in with details from my personal website and the GitHub repo for this project.

### 1.2. Authentication
1. Scroll to the bottom of the page and click the "OAuth 2.0 tutorial page" link. It will redirect to https://dev.fitbit.com/apps/oauthinteractivetutorial with some added parameters configured for your app.

2. Select "Authorization Code Flow" as the app will only run server-side.
3. In "Select Scopes", choose "activity" and "profile"
4. Click on the hyperlink, select "Allow All" in the page that opens, then click "Allow"
5. Copy the "code=" part from the URL in the redirected page. in notebook 1_get_data, paste this in as the `CODE` variable. Execute all cells in the notebook to generate the access and refresh tokens and save to a secrets file.
