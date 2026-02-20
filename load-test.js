// The Non-Functional Test (Load Test)
import http from 'k6/http';
import { sleep, check } from 'k6';

// Configuration: Fail the pipeline if 95% of requests take > 500ms
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
  // 1. Send a request to the containerized app (running on localhost in the CI runner)
  const res = http.get('http://localhost:5000/');

  // 2. Validate the response
  check(res, {
    'is status 200': (r) => r.status === 200,
    'text verified': (r) => r.body.includes('DevSecOps'),
  });

  // 3. Pause for 1 second between requests (simulating real user behavior)
  sleep(1);
}