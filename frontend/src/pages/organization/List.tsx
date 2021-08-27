import {
  Box,
  /*List,
  ListItem,*/
  Table,
  TableCaption,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react";
import React from "react";
import { useGetOrgsQuery } from "../../generated/graphql";

export const OrganizationList = () => {
  const { data, error } = useGetOrgsQuery();
  console.log(error?.message);
  console.log(data);
  return (
    <Box padding="200px">
      <Table variant="simple">
        <TableCaption>Imperial to metric conversion factors</TableCaption>
        <Thead>
          <Tr>
            <Th>Name</Th>
          </Tr>
        </Thead>
        <Tbody>
          {data?.organizations?.map((organization) => (
            <Tr>
              <Td>{organization?.name}</Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
    </Box>
  );
};
