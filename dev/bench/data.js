window.BENCHMARK_DATA = {
  "lastUpdate": 1776076891872,
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
          "id": "284b9c2cd7d30a358880a47f345222826f2349ce",
          "message": "todone",
          "timestamp": "2026-04-13T19:59:39+10:00",
          "tree_id": "96dca9108735756bb43f41e99493a16e544a9d3f",
          "url": "https://github.com/jack-laverty/arinc424/commit/284b9c2cd7d30a358880a47f345222826f2349ce"
        },
        "date": 1776074417303,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_benchmark.py::test_decode_airport_benchmark",
            "value": 3860001.618182924,
            "unit": "iter/sec",
            "range": "stddev: 1.0044994871833259e-7",
            "extra": "mean: 259.0672489072025 nsec\nrounds: 71964"
          },
          {
            "name": "tests/test_benchmark.py::test_read_file_benchmark",
            "value": 636.8696582563563,
            "unit": "iter/sec",
            "range": "stddev: 0.00008027759204833023",
            "extra": "mean: 1.5701799999984838 msec\nrounds: 9"
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
          "id": "c1b5da86c0db01c687c714c74cbeaae9db50e79a",
          "message": "more benchmarks",
          "timestamp": "2026-04-13T20:23:14+10:00",
          "tree_id": "5a87da965c49366049fcb035541adda58be06cce",
          "url": "https://github.com/jack-laverty/arinc424/commit/c1b5da86c0db01c687c714c74cbeaae9db50e79a"
        },
        "date": 1776076009020,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_benchmark.py::test_read_benchmark",
            "value": 140934.17621041476,
            "unit": "iter/sec",
            "range": "stddev: 0.00000207194920548048",
            "extra": "mean: 7.095511017192875 usec\nrounds: 17745"
          },
          {
            "name": "tests/test_benchmark.py::test_json_benchmark",
            "value": 87406.96076258607,
            "unit": "iter/sec",
            "range": "stddev: 0.000001565045995064145",
            "extra": "mean: 11.440736427344616 usec\nrounds: 25124"
          },
          {
            "name": "tests/test_benchmark.py::test_decode_benchmark",
            "value": 1142.0114018407896,
            "unit": "iter/sec",
            "range": "stddev: 0.00002900451782287786",
            "extra": "mean: 875.6480000008023 usec\nrounds: 48"
          },
          {
            "name": "tests/test_benchmark.py::test_read_file_benchmark",
            "value": 644.9574421607111,
            "unit": "iter/sec",
            "range": "stddev: 0.00005886906808087646",
            "extra": "mean: 1.5504898999999739 msec\nrounds: 10"
          },
          {
            "name": "tests/test_benchmark.py::test_faacifp_benchmark",
            "value": 0.04003654545317591,
            "unit": "iter/sec",
            "range": "stddev: 0.13294795778187127",
            "extra": "mean: 24.977179940999996 sec\nrounds: 5"
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
          "id": "f8c65377e38551c15d6429658bdfde891af1c01c",
          "message": "its not fast",
          "timestamp": "2026-04-13T20:38:50+10:00",
          "tree_id": "a7887e65eb4fe8868f86a857867cd4331cf1be2b",
          "url": "https://github.com/jack-laverty/arinc424/commit/f8c65377e38551c15d6429658bdfde891af1c01c"
        },
        "date": 1776076891575,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_benchmark.py::test_read_benchmark",
            "value": 154033.2642896148,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010082346542510767",
            "extra": "mean: 6.492104186792994 usec\nrounds: 14474"
          },
          {
            "name": "tests/test_benchmark.py::test_json_benchmark",
            "value": 89745.2401369155,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011532253001550184",
            "extra": "mean: 11.142652228401174 usec\nrounds: 22348"
          },
          {
            "name": "tests/test_benchmark.py::test_decode_benchmark",
            "value": 1301.5723540377062,
            "unit": "iter/sec",
            "range": "stddev: 0.00002139779499864621",
            "extra": "mean: 768.3015061727643 usec\nrounds: 81"
          },
          {
            "name": "tests/test_benchmark.py::test_read_file_benchmark",
            "value": 829.9559783827755,
            "unit": "iter/sec",
            "range": "stddev: 0.00007583128117446224",
            "extra": "mean: 1.204883181814735 msec\nrounds: 11"
          },
          {
            "name": "tests/test_benchmark.py::test_faacifp_benchmark",
            "value": 0.056146642583120666,
            "unit": "iter/sec",
            "range": "stddev: 0.02353870339515237",
            "extra": "mean: 17.810503958800012 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}