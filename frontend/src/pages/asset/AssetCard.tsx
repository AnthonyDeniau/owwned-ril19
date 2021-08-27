import { Badge, Box, Heading, HStack, Image } from "@chakra-ui/react";
import { FunctionComponent } from "react";
import { AssetType } from "../../generated/graphql";
// import { useGetAssetQuery } from "../../generated/graphql";

type AssetCardProps = {
  asset: AssetType;
};

export const AssetCard: FunctionComponent<AssetCardProps> = ({ asset }) => {
  return (
    <Box maxW="xs" borderWidth="1px" borderRadius="lg" overflow="hidden">
      <Heading as="h1" size="md" isTruncated pl="2" pt="2">
        {asset.name}
      </Heading>

      <HStack pl="2">
        <Image
          src={asset.picture}
          alt={asset.name}
          maxWidth="100px"
          maxHeight="100px"
        />
        <Box>
          <Box p="2">
            <Box d="flex" alignItems="baseline">
              <Badge borderRadius="full" px="2" colorScheme="teal">
                Loaned
              </Badge>
              <Box
                color="gray.500"
                fontWeight="semibold"
                letterSpacing="wide"
                fontSize="xs"
                textTransform="uppercase"
                ml="2"
              >
                {asset.name}
              </Box>
            </Box>

            <Box
              mt="1"
              fontWeight="semibold"
              as="h4"
              lineHeight="tight"
              isTruncated
            >
              {asset.description}
            </Box>

            <Box>
              {asset.cost}
              <Box as="span" color="gray.600" fontSize="sm">
                €
              </Box>
            </Box>
          </Box>
        </Box>
      </HStack>
    </Box>
  );
};
