from flask import Flask, render_template, request, jsonify
from flask_caching import Cache

from src.config import BASE_URL 
from src.crawl import CrawlingManager

app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "simple"})

@app.route('/')
def hello():
    return render_template('index.html', base_url=BASE_URL)

@app.route('/crawling', methods=['GET', 'POST'])
def crawling():
    if request.method == "POST":    
        keyword = request.form.get("keyword", "")
        if keyword:
            crawlingManager = CrawlingManager(BASE_URL, keyword, hidden_browser_option=True)
            print('크롤링 시작')
            crawlingManager.start_crawling(
                start_page=1, 
                end_page=99,
                progress_callback=lambda msg: cache.set('crawling_progress', msg)
            )
            crawlingManager.save_csv(dir_name='data')
            return jsonify({'result': True})
        else:
            return jsonify({'result': False})
    else:
        # 다운로드 진행상태 조회
        crawling_progress = cache.get("crawling_progress")
        if crawling_progress is None:
            crawling_progress = ''
        return jsonify({"progress": crawling_progress})

if __name__ == '__main__':
    app.run(debug=True)