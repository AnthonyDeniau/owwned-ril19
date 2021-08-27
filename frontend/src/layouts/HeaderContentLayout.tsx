import { Center, Flex, Text } from "@chakra-ui/layout";
import React, { FunctionComponent } from "react";
type HeaderContentLayoutProps = {
  header?: React.ReactNode;
};
export const HeaderContentLayout: FunctionComponent<HeaderContentLayoutProps> =
  ({ header, children }) => {
    return (
      <Flex flexDir="column" height="100%" margin="0" bg="gray.100">
        <Flex
          height={"68px"}
          justifyContent="center"
          alignItems="center"
          bg="white"
        >
          <Text fontWeight="black" color="gray.800" fontSize="2xl">
            Owwned
          </Text>
        </Flex>
        <Flex>
          <Center>{children}</Center>
        </Flex>
      </Flex>
    );
  };
