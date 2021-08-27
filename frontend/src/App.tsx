import { ChakraProvider } from "@chakra-ui/react";
import "./App.css";
import { ApolloClient, ApolloProvider, InMemoryCache } from "@apollo/client";
import { AssetTeamList } from "./pages/asset/TeamList";
import { HeaderContentLayout } from "./layouts/HeaderContentLayout";

export const client = new ApolloClient({
  uri: "/graphql/",
  cache: new InMemoryCache(),
});

function App() {
  return (
    <ChakraProvider>
      <ApolloProvider client={client}>
        <HeaderContentLayout>
          <AssetTeamList />
        </HeaderContentLayout>
      </ApolloProvider>
    </ChakraProvider>
  );
}

export default App;
