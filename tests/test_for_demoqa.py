from selene import browser, be, have
from pathlib import Path

def test_for_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Ekaterina')
    browser.element('#lastName').type('Kurinaya')
    browser.element('#userEmail').type('cat@gmail.com')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1995"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="0"]').click()
    browser.element('.react-datepicker__day--017').click()
    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('#subjectsInput').type('Civics').press_enter()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(str(Path(__file__).parent / 'resources' / 'cat.png'))
    browser.element('#currentAddress').type('Eftorius, 5')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('tr').should(have.texts(
        'Label Values',
        'Student Name Ekaterina Kurinaya',
        'Student Email cat@gmail.com',
        'Gender Female',
        'Mobile 1234567890',
        'Date of Birth 17 January,1995',
        'Subjects History, Civics',
        'Hobbies Reading, Music',
        'Picture cat.png',
        'Address Eftorius, 5',
        'State and City NCR Noida'
    ))
