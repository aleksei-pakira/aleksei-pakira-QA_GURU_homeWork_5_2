import os.path

from selene import browser, have, be, command


def test_complete_todo():

    browser.open('/automation-practice-form')
    browser.should(have.title('DEMOQA'))

    browser.element('[id="firstName"]').type('Johann').should(have.value('Johann'))
    browser.element('[id="lastName"]').type('Bach').should(have.value('Bach'))
    browser.element('[id="userEmail"]').type('Johann@Bach.com').should(have.value('Johann@Bach.com'))
    browser.element('[id="gender-radio-1"]').perform(command.js.click).should(be.selected)
    browser.element('[id="userNumber"]').type('+493103168').should(have.value('+493103168'))
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1900"]').click().perform(command.js.scroll_into_view)
    browser.element('[select="react-datepicker__month-select"]')
    browser.element('[value="0"]').click().perform(command.js.scroll_into_view)
    browser.element('[class="react-datepicker__day react-datepicker__day--001"]').click()
    browser.element('[id="dateOfBirthInput"]').should(have.value('01 Jan 1900'))
    browser.element('[id="subjectsInput"]').type('genius').should(have.value('genius'))
    browser.element('[id="hobbies-checkbox-3"]').perform(command.js.click).should(be.selected)
    (browser.element('[id="uploadPicture"]').perform(command.js.click)
        .send_keys(os.path.abspath('form_image_Practice_Form/organ.jpeg')))
    (browser.element('[id="currentAddress"]').type('Sophienstraße 41, 99817 Eisenach, Germany')
        .should(have.value('Sophienstraße 41, 99817 Eisenach, Germany')))
    browser.element('[id="state"]').click()
    browser.element('[id="react-select-3-option-3"]').perform(command.js.scroll_into_view).perform(command.js.click)
    browser.element('[id="state"]>div>div').should(have.text('Rajasthan'))
    browser.element('[id="city"]').click()
    (browser.element('[id="react-select-4-option-1"]')
        .perform(command.js.scroll_into_view).perform(command.js.click))
    browser.element('[id="city"]>div>div').should(have.text('Jaiselmer'))
    browser.element('button[id="submit"]').click()
