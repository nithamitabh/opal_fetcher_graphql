import os
from typing import Optional, Any, Dict
import aiohttp
from pydantic import BaseModel, Field
from opal_common.fetcher.fetch_provider import BaseFetchProvider
from opal_common.fetcher.events import FetcherConfig, FetchEvent
from opal_common.logger import logger
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class GraphQLConnectionParams(BaseModel):
    url: str = Field(..., description="GraphQL endpoint URL")
    token: Optional[str] = Field(None, description="GraphQL API token for authentication")

class GraphQLFetcherConfig(FetcherConfig):
    fetcher: str = "GraphQLFetchProvider"
    connection_params: GraphQLConnectionParams = Field(...)
    query: str = Field(..., description="GraphQL query")

class GraphQLFetchEvent(FetchEvent):
    fetcher: str = "GraphQLFetchProvider"
    config: GraphQLFetcherConfig = None

class GraphQLFetchProvider(BaseFetchProvider):
    def __init__(self, event: GraphQLFetchEvent) -> None:
        super().__init__(event)
        self._event: GraphQLFetchEvent = event
        self._connection_params = self._event.config.connection_params

    def parse_event(self, event: FetchEvent) -> GraphQLFetchEvent:
        return GraphQLFetchEvent(**event.dict(exclude={"config"}), config=event.config)

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()

    async def _fetch_(self) -> Dict[str, Any]:
        headers = {}
        if self._connection_params.token:
            headers['Authorization'] = f"Bearer {self._connection_params.token}"
        
        async with self._session.post(
            self._connection_params.url,
            json={'query': self._event.config.query},
            headers=headers
        ) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch data: {response.status}")
            data = await response.json()
            return data

    async def _process_(self, data: Dict[str, Any]) -> Any:
        return data

