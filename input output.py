def input_pekerjaan():
    pekerjaan = input("Masukan pekerjaan :")
    return pekerjaan


def input_lokasi():
    lokasi = input("Masukan lokasi pekerjaan :")
    return lokasi


def input_halaman():
    halaman = input("Masukan halaman :")
    return int(halaman)


def calculate(n):
    if n == 1:
        return 1
    else:
        return (n - 1) * 10


def set_url(job, loc, pp):  # job = pekerjaan, loc = lokasi, pp = halaman
    url = f"https://id.indeed.com/jobs?q={job}&l={loc}&start={pp}"
    return url


if __name__ == "__main__":
    pekerjaan = input_pekerjaan()
    lokasi = input_lokasi()
    halaman = input_halaman()
    kalkulasi_halaman = calculate(n=halaman)
    url = set_url(pekerjaan, lokasi, kalkulasi_halaman)

print(url)

def driver():
  driver = webdriver.Edge()
  driver.set_page_load_timeout(200)
  driver.implicitly_wait(120)


def target_url(url):
  driver.get(url)
  html_content = driver.page_source
  with open('target.html' ,'w') as file:
    soup = BeautifulSoup(html_content, 'html.parser')
    file.writelines(soup.prettify())

time.sleep(30)