import { gql } from '@apollo/client';
import * as ApolloReactCommon from '@apollo/client';
import * as ApolloReactHooks from '@apollo/client';
export type Maybe<T> = T | null;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
const defaultOptions =  {}
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  /** The `Decimal` scalar type represents a python Decimal. */
  Decimal: any;
};

export type AssetType = {
  __typename?: 'AssetType';
  id: Scalars['ID'];
  name: Scalars['String'];
  description: Scalars['String'];
  picture: Scalars['String'];
  cost: Scalars['Decimal'];
  supplier: SupplierType;
};

export type CreateAssetMutation = {
  __typename?: 'CreateAssetMutation';
  asset?: Maybe<AssetType>;
};

export type CreateOrganizationMutation = {
  __typename?: 'CreateOrganizationMutation';
  organization?: Maybe<OrganizationType>;
};

export type CreateSupplierMutation = {
  __typename?: 'CreateSupplierMutation';
  supplier?: Maybe<SupplierType>;
};


export type DeleteAssetMutation = {
  __typename?: 'DeleteAssetMutation';
  deleted?: Maybe<Scalars['Boolean']>;
};

export type DeleteOrganizationMutation = {
  __typename?: 'DeleteOrganizationMutation';
  deleted?: Maybe<Scalars['Boolean']>;
};

export type DeleteSupplierMutation = {
  __typename?: 'DeleteSupplierMutation';
  deleted?: Maybe<Scalars['Boolean']>;
};

export type Mutation = {
  __typename?: 'Mutation';
  createSupplier?: Maybe<CreateSupplierMutation>;
  updateSupplier?: Maybe<UpdateSupplierMutation>;
  deleteSupplier?: Maybe<DeleteSupplierMutation>;
  createAsset?: Maybe<CreateAssetMutation>;
  updateAsset?: Maybe<UpdateAssetMutation>;
  deleteAsset?: Maybe<DeleteAssetMutation>;
  createOrganization?: Maybe<CreateOrganizationMutation>;
  deleteOrganization?: Maybe<DeleteOrganizationMutation>;
};


export type MutationCreateSupplierArgs = {
  login: Scalars['String'];
  name: Scalars['String'];
  password: Scalars['String'];
  website: Scalars['String'];
};


export type MutationUpdateSupplierArgs = {
  id?: Maybe<Scalars['ID']>;
  login?: Maybe<Scalars['String']>;
  name?: Maybe<Scalars['String']>;
  password?: Maybe<Scalars['String']>;
  website?: Maybe<Scalars['String']>;
};


export type MutationDeleteSupplierArgs = {
  id?: Maybe<Scalars['ID']>;
};


export type MutationCreateAssetArgs = {
  cost: Scalars['Float'];
  description: Scalars['String'];
  name: Scalars['String'];
  picture: Scalars['String'];
  supplierId?: Maybe<Scalars['ID']>;
};


export type MutationUpdateAssetArgs = {
  cost: Scalars['Float'];
  description: Scalars['String'];
  name: Scalars['String'];
  picture: Scalars['String'];
  supplierId?: Maybe<Scalars['ID']>;
};


export type MutationDeleteAssetArgs = {
  id?: Maybe<Scalars['ID']>;
};


export type MutationCreateOrganizationArgs = {
  name: Scalars['String'];
};


export type MutationDeleteOrganizationArgs = {
  id?: Maybe<Scalars['ID']>;
};

export type OrganizationType = {
  __typename?: 'OrganizationType';
  id: Scalars['ID'];
  name: Scalars['String'];
};

export type Query = {
  __typename?: 'Query';
  supplier?: Maybe<SupplierType>;
  suppliers?: Maybe<Array<Maybe<SupplierType>>>;
  asset?: Maybe<AssetType>;
  assets?: Maybe<Array<Maybe<AssetType>>>;
  organization?: Maybe<OrganizationType>;
  organizations?: Maybe<Array<Maybe<OrganizationType>>>;
  hello?: Maybe<Scalars['String']>;
};


export type QuerySupplierArgs = {
  id: Scalars['ID'];
};


export type QueryAssetArgs = {
  id: Scalars['ID'];
};


export type QueryOrganizationArgs = {
  id: Scalars['ID'];
};

export type SupplierType = {
  __typename?: 'SupplierType';
  id: Scalars['ID'];
  name: Scalars['String'];
  website: Scalars['String'];
  login: Scalars['String'];
  password: Scalars['String'];
  assetSet: Array<AssetType>;
};

export type UpdateAssetMutation = {
  __typename?: 'UpdateAssetMutation';
  asset?: Maybe<AssetType>;
};

export type UpdateSupplierMutation = {
  __typename?: 'UpdateSupplierMutation';
  supplier?: Maybe<SupplierType>;
};

export type GetAssetsQueryVariables = Exact<{ [key: string]: never; }>;


export type GetAssetsQuery = (
  { __typename?: 'Query' }
  & { assets?: Maybe<Array<Maybe<(
    { __typename?: 'AssetType' }
    & Pick<AssetType, 'name' | 'description' | 'picture' | 'cost'>
  )>>> }
);

export type GetOrgsQueryVariables = Exact<{ [key: string]: never; }>;


export type GetOrgsQuery = (
  { __typename?: 'Query' }
  & { organizations?: Maybe<Array<Maybe<(
    { __typename?: 'OrganizationType' }
    & Pick<OrganizationType, 'name'>
  )>>> }
);


export const GetAssetsDocument = gql`
    query GetAssets {
  assets {
    name
    description
    picture
    cost
  }
}
    `;

/**
 * __useGetAssetsQuery__
 *
 * To run a query within a React component, call `useGetAssetsQuery` and pass it any options that fit your needs.
 * When your component renders, `useGetAssetsQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useGetAssetsQuery({
 *   variables: {
 *   },
 * });
 */
export function useGetAssetsQuery(baseOptions?: ApolloReactHooks.QueryHookOptions<GetAssetsQuery, GetAssetsQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return ApolloReactHooks.useQuery<GetAssetsQuery, GetAssetsQueryVariables>(GetAssetsDocument, options);
      }
export function useGetAssetsLazyQuery(baseOptions?: ApolloReactHooks.LazyQueryHookOptions<GetAssetsQuery, GetAssetsQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return ApolloReactHooks.useLazyQuery<GetAssetsQuery, GetAssetsQueryVariables>(GetAssetsDocument, options);
        }
export type GetAssetsQueryHookResult = ReturnType<typeof useGetAssetsQuery>;
export type GetAssetsLazyQueryHookResult = ReturnType<typeof useGetAssetsLazyQuery>;
export type GetAssetsQueryResult = ApolloReactCommon.QueryResult<GetAssetsQuery, GetAssetsQueryVariables>;
export const GetOrgsDocument = gql`
    query GetOrgs {
  organizations {
    name
  }
}
    `;

/**
 * __useGetOrgsQuery__
 *
 * To run a query within a React component, call `useGetOrgsQuery` and pass it any options that fit your needs.
 * When your component renders, `useGetOrgsQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = useGetOrgsQuery({
 *   variables: {
 *   },
 * });
 */
export function useGetOrgsQuery(baseOptions?: ApolloReactHooks.QueryHookOptions<GetOrgsQuery, GetOrgsQueryVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return ApolloReactHooks.useQuery<GetOrgsQuery, GetOrgsQueryVariables>(GetOrgsDocument, options);
      }
export function useGetOrgsLazyQuery(baseOptions?: ApolloReactHooks.LazyQueryHookOptions<GetOrgsQuery, GetOrgsQueryVariables>) {
          const options = {...defaultOptions, ...baseOptions}
          return ApolloReactHooks.useLazyQuery<GetOrgsQuery, GetOrgsQueryVariables>(GetOrgsDocument, options);
        }
export type GetOrgsQueryHookResult = ReturnType<typeof useGetOrgsQuery>;
export type GetOrgsLazyQueryHookResult = ReturnType<typeof useGetOrgsLazyQuery>;
export type GetOrgsQueryResult = ApolloReactCommon.QueryResult<GetOrgsQuery, GetOrgsQueryVariables>;