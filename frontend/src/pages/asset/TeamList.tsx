import { Box, Wrap, WrapItem } from "@chakra-ui/react";
import { AssetType, useGetAssetsQuery } from "../../generated/graphql";
import { AssetCard } from "./AssetCard";

export const AssetTeamList = () => {
  const { data } = useGetAssetsQuery();
  return (
    <Wrap>
      {data?.assets?.map((asset) => (
        <WrapItem>
          <AssetCard asset={asset as AssetType} />
        </WrapItem>
      ))}
    </Wrap>
  );
};
