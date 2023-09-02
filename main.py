from datetime import date, timedelta
import requests

query_url = 'https://api.github.com/search/repositories?q=pushed%3A%3C{}+language%3ASolidity&type=Repositories&ref=advsearch&l=Solidity&l='


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)



if __name__ == '__main__':
    with open("dataset.csv", "w") as f:
        f.write("date,count\n")
        r = requests.get(query_url.format('2022-12-31')).json()
        count = r['total_count']
        f.write("2022-12-31,{}\n".format(count))



