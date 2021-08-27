import { ChakraProvider } from "@chakra-ui/react";
import "./App.css";
import { ApolloClient, ApolloProvider, InMemoryCache } from "@apollo/client";
import { AssetTeamList } from "./pages/asset/TeamList";

export const client = new ApolloClient({
  uri: "/graphql/",
  cache: new InMemoryCache(),
});

function App() {
  return (
    <ChakraProvider>
      <ApolloProvider client={client}>
        <AssetTeamList />
      </ApolloProvider>
    </ChakraProvider>
  );
}

export default App;
