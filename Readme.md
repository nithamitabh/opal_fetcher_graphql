# OPAL GraphQL Fetcher

This repository provides a custom OPAL fetch provider for GraphQL, allowing you to fetch data from a GraphQL endpoint and sync it with the OPAL policy engine.
## Things I used
- `OPAL` - This is authorization method but i used here for fetching custom data.
- `Neon` - A serverless Postgress Service help to ship faster postgress thing.
- `pydantic` -Data validation using Python type hints.

## How to Use

### Prerequisites
- Docker
- Docker Compose
- Python

### Build and Run

1. **Clone the Repository**:
    ```sh
    git clone <repo_url>
    cd opal-fetcher-graphql
    ```
- `Note`  Make a new Python new environment so you have clean package install from `requirements.txt`.
2. **Create a .env File**:
    Create a `.env` file in the root directory and add the following content:
    ```env
    GRAPHQL_ENDPOINT=https://yourgraphqlendpoint.com/graphql
    GRAPHQL_QUERY={ yourGraphQLQuery }
    GRAPHQL_API_TOKEN=your_api_token
    DATABASE_URL=postgres://user:password@neon.tech:5432/dbname
    ```

3. **Build the Docker Image**:
    ```sh
    docker compose build
    ```

4. **Run the Docker Container**:
    ```sh
    docker compose up
    ```

This will start the OPAL client with the custom GraphQL fetch provider.

### Configuration

- **GraphQL Endpoint**: Configure your GraphQL endpoint in the `.env` file.

Example `.env` file:
```env
GRAPHQL_ENDPOINT=https://api.github.com/graphql
GRAPHQL_QUERY={ viewer { login name repositories(first: 5) { nodes { name url } } } }
GRAPHQL_API_TOKEN=your_github_personal_access_token
DATABASE_URL=postgres://user:password@neon.tech:5432/dbname

```

### Implementation Detail
- The `GraphQLFetchProvider` class in `provider.py` handles fetching data from the GraphQL endpoint using an async HTTP request.
- The `GraphQLFetchEvent` and `GraphQLFetcherConfig` classes define the structure of the fetch event and fetcher configuration.
For more details on writing custom fetch providers, refer to the  [OPAL Documentation](https://opal.ac/tutorials/write_your_own_fetch_provider/).

 By following this guide, you can create a custom GraphQL data fetcher for OPAL, utilizing environment variables for configuration, and integrating seamlessly with a Docker setup. This should make your project more flexible and easier to configure for different environments.
