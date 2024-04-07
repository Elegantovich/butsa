from pages.main import MainPage


def test_case_01(app):
    main_page = MainPage(app)
    app.wd.get(main_page.url)
    print(1)
