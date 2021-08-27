import { ChakraProvider } from "@chakra-ui/react";
import "./App.css";
import { OrganizationList } from "./pages/organization/List";
import { ApolloClient, ApolloProvider, InMemoryCache } from "@apollo/client";

export const client = new ApolloClient({
  uri: "/graphql/",
  cache: new InMemoryCache(),
});

function App() {
  return (
    <ChakraProvider>
      <ApolloProvider client={client}>
        <OrganizationList />
      </ApolloProvider>
    </ChakraProvider>
  );
}

export default App;
