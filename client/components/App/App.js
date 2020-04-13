import React from 'react';
import { ApolloProvider } from 'react-apollo';
import client from './../../graphql/client.js';
import { RANKING_4X4 } from './../../graphql/queries/ranking.js';

import { Query } from "react-apollo";

const App = (props) => {
  return (
    <ApolloProvider client={client}>
      <div>
        <h3>React Hot Loader</h3>
      </div>
      <div>
        <Query query={ RANKING_4X4 }>
          {
            ({ loading, data, error })=>{
              if( loading ) return <span>loadding...</span>
              if( error ) return <span>Something errors...</span>
              return (
                <ul>
                {
                  data.ranks.map(node=>{
                  return <li key={ node.id }>{ node.name }/{ node.regDttm }</li>
                  })
                }
                </ul>
              )
            }
          }
        </Query>
      </div>
    </ApolloProvider>
  )
}

export default App;