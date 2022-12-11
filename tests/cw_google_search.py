from selene.support.shared import browser
from selene import be, have, by


def test_finds_selene():
    browser.open('/ncr').should(have.title('Google'))
    browser.element('[name=q]').type('selene').press_enter()
    browser.element('#search').should(have.text('User-oriented Web UI browser tests'))

    results = browser.all('#rso>div')
    results.should(have.size_greater_than_or_equal(6))


def test_finds_selene():
    browser.open('/ncr').should(have.title('Google'))
    browser.element('[name=q]').type('selene').press_enter()
    results = browser.all('#rso>div')
    results.should(have.size_greater_than_or_equal(6))

    browser.element('[name=q]').type(' yashaka github').press_enter()
    results.first.element('h3').click()
    browser.should(have.title_containing('yashaka/selene'))