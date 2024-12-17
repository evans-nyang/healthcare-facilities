# Frontend Deployment Using Vercel Guide

The front end User Interface was built using React. We're going to deploy our frontend using vercel. It is free and easy to use. Vercel is a cloud platform for static sites and Serverless Functions. It enables web services that deploy instantly, scale automatically, and requires no supervision, all with no configuration.

## Prerequisites

- A Vercel account. To create an account, go to [Vercel](https://vercel.com/account/settings).
- Node.js installed on your local machine. To install Node.js, go to [Node.js](https://nodejs.org/en/download/).

## Deploying the Healthcare Assistant application

Before starting the deployment make sure to run build command in the frontend project. This will create a build folder in the project directory.

```bash
npm run build
```

Install the Vercel CLI globally by running the following command in your terminal:

```bash
sudo npm install -g vercel
```

Navigate to the root directory of the frontend project and run the following command:

```bash
vercel
```

To deploy a project in development mode, run the following command:

```bash
vercel dev
```

To deploy the project in production mode, run the following command:

```bash
vercel --prod
```

Deploy with Environment Variables

```bash
vercel -e NODE_ENV=production
```

List all deployments for the currently linked project

```bash
vercel list
```

## Issues

You might run into issues while deploying the project. Here are some common issues and their solutions:

- Dependency errors: Ensure that all dependencies are installed and up to date.

```bash
npm install axios
npm install @material-ui/core
npm install @material-ui/icons
```

## Extras

- [Vercel Documentation](https://vercel.com/docs)
