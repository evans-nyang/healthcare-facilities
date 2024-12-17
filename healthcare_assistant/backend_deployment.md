# Heroku Deployment Setup

This document outlines the steps to deploy the Healthcare Assistant application to Heroku using Docker and Heroku Postgres. It includes environment variable configuration, Docker setup, and troubleshooting common issues.

## Prerequisites

- A Heroku account
- Heroku CLI installed in terminal

### Creating Heroku account

1. Go to [Heroku](https://www.heroku.com/) and sign up for an account.
2. Verify your email address and log in to your account.

### Installing Heroku CLI

Run the following command in your terminal to install the Heroku CLI:

```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

To login to your Heroku account, run the following command:

```bash
heroku login
```

Go to the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) page.

## Deploying the Healthcare Assistant application

- Create a new heroku app:

```bash
heroku create healthcare-assistant-app
```

- Set the Heroku stack to container:

```bash
heroku stack:set container --app healthcare-assistant-app
```

- Add the Heroku Postgres add-on:

```bash
heroku addons:create heroku-postgresql:essential-0 --app healthcare-assistant-app
```

- Get the Heroku Postgres database URL:

```bash
heroku config:get DATABASE_URL --app healthcare-assistant-app
```

- Set the environment variables:

```bash
heroku config:set DATABASE_URL=$(heroku config:get DATABASE_URL --app healthcare-assistant-app) --app healthcare-assistant-app
heroku config:set OPENAI_API_KEY='your-api-key-here' -a healthcare-assistant-app
heroku config:set GITHUB_TOKEN='your-github-token-here' -a healthcare-assistant-app
```

- Retrieve the set environment variables:

```bash
heroku config -a healthcare-assistant-app
```

- Push the code to Heroku:

```bash
git push heroku main
```

- Create a heroku yaml file as in [heroku.yml](./heroku.yml) or copy and paste the content below in your heroku.yml file.

```yaml
setup:
  addons:
    - plan: heroku-postgresql
build:
  docker:
    web: Dockerfile
```

- Build the Docker image and push it to Heroku:

```bash
heroku container:push web -a healthcare-assistant-app
```

- Release the Docker image:

```bash
heroku container:release web -a healthcare-assistant-app
```

- Check the logs to ensure the application is running correctly:

```bash
heroku logs --tail -a healthcare-assistant-app
```

- Open the deployed application:

```bash
heroku open -a healthcare-assistant-app
```

- To restart the application:

```bash
heroku restart -a healthcare-assistant-app
```

- To remove the deployed container and destroy the Heroku app:

```bash
heroku container:rm web -a healthcare-assistant-app
heroku apps
heroku apps:destroy healthcare-assistant-app
```
