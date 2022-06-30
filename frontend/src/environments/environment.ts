/* @TODO replace with your variables
 * ensure all variables on this page match your project
 */

export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url:  'fyyurapi.us.auth0.com', // the auth0 domain prefix
    audience: 'coffee', // the audience set for the auth0 app
    clientId: '10rekXgi7B7d9vrCYkAa7t383Vh27Vyv', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};


// https://fyyurapi.us.auth0.com/authorize?audience=coffee&response_type=token&client_id=10rekXgi7B7d9vrCYkAa7t383Vh27Vyv&redirect_uri=https://127.0.0.1:8100/
// https://fyyurapi.us.auth0.com/authorize?audience=coffee&response_type=token&client_id=10rekXgi7B7d9vrCYkAa7t383Vh27Vyv&redirect_uri=https://127.0.0.1:8100/


// https://127.0.0.1:8100/#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhfNVlEb2pNQ19kY28wLW8yS2lweCJ9.eyJpc3MiOiJodHRwczovL2Z5eXVyYXBpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmJkYTkzYjVlYWIwMmE0MzgyZmQ1NTYiLCJhdWQiOiJjb2ZmZWUiLCJpYXQiOjE2NTY1OTY4MDUsImV4cCI6MTY1NjYwNDAwNSwiYXpwIjoiMTByZWtYZ2k3QjdkOXZyQ1lrQWE3dDM4M1ZoMjdWeXYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbXX0.MgMS-HbkarxmZ0xlcRpwlOagVo_0IQk6IcugCJLpXwn2LA8wIQPpK6Lb_BPznXto7DjunMp5XLB-Gcl0RawkjEW9TrB72gPcpAyCvmXOLvs7dOJMBesvUDIMuEEt03ggSe_nWN67pDIYYi0EU_QzYvwdxbIJFxBBp16bGt1DZlEuJDQfbD1qnxY8ZuM2-s8qQO0LpsPvAAEXLugF1oTvL4zH6azbTdcKQUkBHJD4zPGKZziuIVEo__L3LxIerk5VWstC3cP5eUAYGIlzD9CYbquVtUfTk0aYKhkm6Nr3f814Ioxrj6pJtHH3nSbpMtnAsMmAw1svf-0ipzU0_3bn3g&expires_in=7200&token_type=Bearer