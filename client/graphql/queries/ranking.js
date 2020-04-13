import gql from 'graphql-tag';

export const RANKING_4X4 = gql(`
  query {
    ranks(mode: "4x4") {
      name
      mode
      score
      id
      regDttm
    }
  }
`);