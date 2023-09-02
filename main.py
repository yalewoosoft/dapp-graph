from datetime import date, timedelta
import requests
import time
import os

query_url = 'https://api.github.com/search/repositories?q=pushed%3A%3C{}+language%3ASolidity&type=Repositories&ref=advsearch&l=Solidity&l='


def daterange(start_date: date, end_date: date) -> str:
    for n in range(int((end_date - start_date).days)):
        yield (start_date + timedelta(n)).strftime("%Y-%m-%d")



if __name__ == '__main__':
    # read token
    token_file = open("token.txt","r")
    token = token_file.readline()
    token_file.close()
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    write_header = False
    if not os.path.exists('dataset.csv'):
        write_header = True
    # api access
    with open("dataset.csv", "a+") as f:
        counter = 0
        first_line = f.readline()
        if write_header:
            f.write("date,count\n")
        for i in daterange(date(2020, 1, 1), date(2023, 9, 1)):
            r: requests.Response = None
            try:
                r = requests.get(query_url.format(i), headers=headers).json()
                count = r['total_count']
                f.write("{},{}\n".format(i, count))
                print('Done: {}'.format(i))
                counter += 1
                if counter == 28:
                    # rate limit reached; sleep 1min
                    print('Rate limit reached; sleep 1min')
                    counter = 0
                    time.sleep(60)
            except Exception:
                print(r.content)
