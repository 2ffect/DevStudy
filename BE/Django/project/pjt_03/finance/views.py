from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import StockComment  # 모델 임포트
from django.shortcuts import redirect
from django.urls import reverse
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager




# 루트 URL에 대한 처리용 home 뷰 추가
def home(request):
    return HttpResponse("<h1>다혜와 재희의 금융금융!</h1>")  # 간단한 텍스트 출력


# index 뷰 수정: 회사 이름에 맞는 댓글을 필터링하여 보여줍니다.
def index(request):
    comments = StockComment.objects.all()
    context = {
        'comments' : comments
    }
    return render(request, 'finance/index.html', context)


def delete_comment(request, comment_id):
    comment = get_object_or_404(StockComment, id=comment_id)
    comment.delete()
    return redirect('finance:index')

def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '').strip()

        if not keyword:
            return redirect(reverse('finance:index'))

        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        try:
            driver.get("https://tossinvest.com/")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys("/")
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']")))

            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input._1x1gpvi6"))
            )
            search_input.clear()
            search_input.send_keys(keyword)
            time.sleep(1)

            results = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button._1jnh59q0"))
            )
            clicked = False
            for item in results:
                if keyword in item.text:
                    item.click()
                    clicked = True
                    break
            if not clicked:
                print("검색 결과 중 종목을 찾지 못했습니다.")
                return redirect(reverse('finance:index'))

            time.sleep(3)

            community_tab = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='커뮤니티']"))
            )
            community_tab.click()
            time.sleep(3)

            soup = BeautifulSoup(driver.page_source, "html.parser")

            company_name_tag = soup.select_one("span.tw-1r5dc8g0[style*='--tds-wts-font-size: 56px']")
            company_name = company_name_tag.get_text(strip=True) if company_name_tag else "N/A"

            code_tag = soup.find("span", string=re.compile(r"\d{6}"))
            company_code = code_tag.get_text(strip=True) if code_tag else "N/A"

            content_spans = soup.select("span.tw-1r5dc8g0._60z0ev1._60z0ev6._60z0ev0._1tvp9v41._1sihfl60")
            content_list = [span.get_text(separator="\n", strip=True) for span in content_spans]

            # DB에 저장
            for content in content_list:
                StockComment.objects.create(
                    company_name=company_name,
                    stock_code=company_code,
                    comment=content
                )

        except Exception as e:
            print("오류 발생:", e)

        finally:
            driver.quit()

    return redirect(reverse('finance:index'))