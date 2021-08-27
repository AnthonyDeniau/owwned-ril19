import gql from "graphql-tag";

const QUERIES = gql`
  query GetOrgs {
    organizations {
      name
    }
  }
`;
