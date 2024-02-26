import os.path

from selene import browser, have, be, command


def test_complete_todo():

    browser.open('/automation-practice-form')
    browser.should(have.title('DEMOQA'))

    browser.element('#firstName').type('Johann')
    browser.element('#lastName').type('Bach')
    browser.element('#userEmail').type('Johann@Bach.com')
    browser.element('#gender-radio-1').perform(command.js.click).should(be.selected)
    browser.element('#userNumber').type('4931031680')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1900"]').click().perform(command.js.scroll_into_view)
    browser.element('.react-datepicker__month-select')
    browser.element('[value="0"]').click().perform(command.js.scroll_into_view)
    browser.element('.react-datepicker__week .react-datepicker__day--001').click()
    browser.element('#subjectsInput').type('art')
    browser.element('[id="react-select-2-option-0"]').click()
    browser.element('#hobbies-checkbox-3').perform(command.js.click).should(be.selected)
    (browser.element('#uploadPicture').perform(command.js.click)
        .send_keys(os.path.abspath('resource/organ.jpeg')))
    browser.element('#currentAddress').type('Sophienstraße 41, 99817 Eisenach, Germany')
    browser.element('#state').click()
    browser.element('#react-select-3-option-3').perform(command.js.scroll_into_view).perform(command.js.click)
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').perform(command.js.scroll_into_view).perform(command.js.click)
    browser.element('button#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table>tbody>tr')[0].should(have.text('Student Name Johann Bach'))
    browser.all('.table>tbody>tr')[1].should(have.text('Student Email Johann@Bach.com'))
    browser.all('.table>tbody>tr')[2].should(have.text('Gender Male'))
    browser.all('.table>tbody>tr')[3].should(have.text('Mobile 4931031680'))
    browser.all('.table>tbody>tr')[4].should(have.text('Date of Birth 01 January,1900'))
    browser.all('.table>tbody>tr')[5].should(have.text('Subjects Arts'))
    browser.all('.table>tbody>tr')[6].should(have.text('Hobbies Music'))
    browser.all('.table>tbody>tr')[7].should(have.text('Picture organ.jpeg'))
    browser.all('.table>tbody>tr')[8].should(have.text('Address Sophienstraße 41, 99817 Eisenach, Germany'))
    browser.all('.table>tbody>tr')[9].should(have.text('State and City Rajasthan Jaiselmer'))