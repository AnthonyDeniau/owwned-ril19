import gql from "graphql-tag";

const QUERIES = gql`
  query GetAssets {
    assets {
      name
      description
      picture
      cost
    }
  }
`;
