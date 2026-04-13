window.BENCHMARK_DATA = {
  "lastUpdate": 1776073960661,
  "repoUrl": "https://github.com/jack-laverty/arinc424",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "jacktlaverty@gmail.com",
            "name": "Jack Laverty",
            "username": "jack-laverty"
          },
          "committer": {
            "email": "jacktlaverty@gmail.com",
            "name": "Jack Laverty",
            "username": "jack-laverty"
          },
          "distinct": true,
          "id": "bef18334b4ca82933b78f08eb9597e6b1e14b965",
          "message": "benchmark only linux on main push",
          "timestamp": "2026-04-13T18:08:25+10:00",
          "tree_id": "4444d33ac7debb6ad9260b7d40d472ee4d08c8b9",
          "url": "https://github.com/jack-laverty/arinc424/commit/bef18334b4ca82933b78f08eb9597e6b1e14b965"
        },
        "date": 1776067744235,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_benchmark.py::test_decode_airport_benchmark",
            "value": 1446.5927359714246,
            "unit": "iter/sec",
            "range": "stddev: 0.000017880792160419195",
            "extra": "mean: 691.2795668979176 usec\nrounds: 1009"
          },
          {
            "name": "tests/test_benchmark.py::test_read_file_benchmark",
            "value": 98.4760671253661,
            "unit": "iter/sec",
            "range": "stddev: 0.00011201629859935269",
            "extra": "mean: 10.154751597938393 msec\nrounds: 97"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jacktlaverty@gmail.com",
            "name": "Jack Laverty",
            "username": "jack-laverty"
          },
          "committer": {
            "email": "jacktlaverty@gmail.com",
            "name": "Jack Laverty",
            "username": "jack-laverty"
          },
          "distinct": true,
          "id": "cbf014dbb957c8fcfe2c1ed6feeb80f6337ad61e",
          "message": "tqdm to deps",
          "timestamp": "2026-04-13T19:51:59+10:00",
          "tree_id": "504f67537c1d52e8d04bfe06123011a192e626df",
          "url": "https://github.com/jack-laverty/arinc424/commit/cbf014dbb957c8fcfe2c1ed6feeb80f6337ad61e"
        },
        "date": 1776073960372,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_benchmark.py::test_decode_airport_benchmark",
            "value": 3148338.182179905,
            "unit": "iter/sec",
            "range": "stddev: 1.7850380614839713e-7",
            "extra": "mean: 317.62788561284776 nsec\nrounds: 179598"
          },
          {
            "name": "tests/test_benchmark.py::test_read_file_benchmark",
            "value": 801.2614419138056,
            "unit": "iter/sec",
            "range": "stddev: 0.00010532319968802071",
            "extra": "mean: 1.248032099999108 msec\nrounds: 10"
          }
        ]
      }
    ]
  }
}