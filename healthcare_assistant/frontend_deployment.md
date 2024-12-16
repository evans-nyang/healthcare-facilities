# Frontend Deployment Using Vercel Guide

The front end User Interface was built using React. We're going to deploy our frontend using vercel. It is free and easy to use. Vercel is a cloud platform for static sites and Serverless Functions. It enables web services that deploy instantly, scale automatically, and requires no supervision, all with no configuration.

## Prerequisites

- A Vercel account. To create an account, go to [Vercel](https://vercel.com/account/settings).
- Node.js installed on your local machine. To install Node.js, go to [Node.js](https://nodejs.org/en/download/).

## Deploying the Healthcare Assistant application

Install the Vercel CLI globally by running the following command in your terminal:

```bash
sudo npm install -g vercel
```

Navigate to the root directory of the frontend project and run the following command:

```bash
cd chat-interface
vercel
```

To deploy the project in production mode, run the following command:

```bash
vercel --prod
```

## Issues

You might run into issues while deploying the project. Here are some common issues and their solutions:

- Dependency errors: Ensure that all dependencies are installed and up to date.

```bash
npm install axios
```

## Extras

- [Vercel Documentation](https://vercel.com/docs)
