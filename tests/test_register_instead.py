from assertpy import assert_that
from faker import Faker
import pdb
import pytest
fake = Faker()

@pytest.mark.student
def test_valid_student_registration(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email())
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='content'][contains(@id,'message')][contains(.,'Welcome to Math World')]")).is_true()

@pytest.mark.student
def test_invalid_student_registration(page, student_registration):
    page.fill("//input[@id='first_name']", "")
    page.fill("//input[@id='last_name']", "")
    page.fill("//input[@id='school']", "")
    page.fill("//input[@id='email']", "")
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'First name is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Last name is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'School is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()
    assert_that(page.is_visible("//div[contains(@id,'passwordDontMatch')]")).is_true()

@pytest.mark.student
def test_missing_student_first_name(page, student_registration):
    page.fill("//input[@id='first_name']", "")
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Test123!")
    page.fill("//input[@id='repeat_password']", "Test123")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'First name is required')]")).is_true()    

@pytest.mark.student
def test_missing_student_last_name(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", "")    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Test123!")
    page.fill("//input[@id='repeat_password']", "Test123")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Last name is required')]")).is_true()

@pytest.mark.student
def test_missing_student_school(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Test123!")
    page.fill("//input[@id='repeat_password']", "Test123")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'School is required')]")).is_true()

@pytest.mark.student
def test_missing_student_email(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", "") 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()

@pytest.mark.student
def test_invalid_student_email(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email().replace("@", "")) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email must be valid')]")).is_true()

@pytest.mark.student
def test_short_student_email(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()[0:3]) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email must be valid')]")).is_true()

@pytest.mark.student
def test_missing_student_password(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "")
    page.fill("//input[@id='repeat_password']", "")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password is required')]")).is_true()

@pytest.mark.student
def test_invalid_student_password(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "testing")
    page.fill("//input[@id='repeat_password']", "testing")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Password must have uppercase letter.')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Password must have a number.')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Password must have a character.')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Length must be 10 or more.')]")).is_true()

@pytest.mark.student
def test_student_passwords_not_equal(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing321!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[contains(@id,'passwordDontMatch')]")).is_true()

@pytest.mark.student
def test_short_student_password(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Test123!")
    page.fill("//input[@id='repeat_password']", "Test123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Length must be 10 or more.')]")).is_true()

@pytest.mark.student
def test_blank_student_information(page, student_registration):
    page.fill("//input[@id='first_name']", "")
    page.fill("//input[@id='last_name']", "")    
    page.fill("//input[@id='school']", "")
    page.fill("//input[@id='email']", "") 
    page.fill("//input[@id='password']", "")
    page.fill("//input[@id='repeat_password']", "")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'First name is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Last name is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'School is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password is required')]")).is_true()

@pytest.mark.student
def test_student_password_too_long(page, student_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Testing123!-Testing-Testing-Testing")
    page.fill("//input[@id='repeat_password']", "Testing123-Testing-Testing-Testing")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Length must not exceed 25 characters.')]")).is_true()

@pytest.mark.teacher
def test_valid_teacher_registration(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//h1[@class='title2'][contains(.,'World')]")).is_true()
    assert_that(page.is_visible("//h1[@id='main_message']")).is_true()  
    page.click("//span[contains(.,'Log Out')]")

@pytest.mark.teacher
def test_invalid_teacher_registration(page, teacher_registration):
    page.fill("//input[@id='first_name']", "")
    page.fill("//input[@id='last_name']", "")
    page.fill("//input[@id='school']", "")
    page.fill("//input[@id='email']", "")
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'First name is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Last name is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'School is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()
    assert_that(page.is_visible("//div[contains(@id,'passwordDontMatch')]")).is_true()

@pytest.mark.teacher
def test_missing_teacher_first_name(page, teacher_registration):
    page.fill("//input[@id='first_name']", "")
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'First name is required')]")).is_true()

@pytest.mark.teacher
def test_missing_teacher_last_name(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", "")    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Last name is required')]")).is_true()

@pytest.mark.teacher
def test_missing_teacher_school(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'School is required')]")).is_true()

@pytest.mark.teacher
def test_missing_teacher_email(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "")
    page.fill("//input[@id='email']", "") 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()

@pytest.mark.teacher
def test_invalid_teacher_email(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email().replace("@", "")) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email must be valid')]")).is_true()

@pytest.mark.teacher
def test_short_teacher_email(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()[0:3]) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email must be valid')]")).is_true()

@pytest.mark.teacher
def test_missing_teacher_password(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "")
    page.fill("//input[@id='repeat_password']", "")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password is required')]")).is_true()

@pytest.mark.teacher
def test_invalid_teacher_password(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "testing")
    page.fill("//input[@id='repeat_password']", "testing")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Password must have uppercase letter.')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Password must have a number.')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Password must have a character.')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Length must be 10 or more.')]")).is_true()

@pytest.mark.teacher
def test_teacher_password_not_equal(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Testing123!")
    page.fill("//input[@id='repeat_password']", "Testing321!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[contains(@id,'passwordDontMatch')]")).is_true()

@pytest.mark.teacher
def test_short_teacher_password(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Test123!")
    page.fill("//input[@id='repeat_password']", "Test123!")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessageP'][contains(.,'Length must be 10 or more.')]")).is_true()

@pytest.mark.teacher
def test_blank_teacher_information(page, teacher_registration):
    page.fill("//input[@id='first_name']", "")
    page.fill("//input[@id='last_name']", "")    
    page.fill("//input[@id='school']", "")
    page.fill("//input[@id='email']", "") 
    page.fill("//input[@id='password']", "")
    page.fill("//input[@id='repeat_password']", "")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'First name is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Last name is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'School is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password is required')]")).is_true()

@pytest.mark.teacher
def test_teacher_password_too_long(page, teacher_registration):
    page.fill("//input[@id='first_name']", fake.first_name())
    page.fill("//input[@id='last_name']", fake.last_name())    
    page.fill("//input[@id='school']", "fakeschool")
    page.fill("//input[@id='email']", fake.email()) 
    page.fill("//input[@id='password']", "Testing123!-Testing-Testing-Testing")
    page.fill("//input[@id='repeat_password']", "Testing123-Testing-Testing-Testing")
    page.click("//span[contains(.,'Register')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Length must not exceed 25 characters.')]")).is_true()

@pytest.fixture
def student_registration(page):
    page.goto("/") 
    page.is_visible("//h1[contains(.,'Math World')]")  
    page.is_visible("//div[@class='content'][contains(.,'For Teachers and For Students')]")  
    page.click("//span[contains(.,'Register')]")
    page.is_visible("//h1[contains(.,'Register')]")
    page.is_visible("//label[@for='first_name'][contains(.,'First Name *')]")
    page.is_visible("//label[@for='last_name'][contains(.,'Last Name *')]")
    page.is_visible("//label[@for='school'][contains(.,'School *')]")
    page.is_visible("//label[@for='text'][contains(.,'Email *')]")
    page.is_visible("//label[@for='password'][contains(.,'Password *')]")
    page.is_visible("//label[@for='repeat_password'][contains(.,'Repeat Password *')]")

@pytest.fixture
def teacher_registration(page):
    page.goto("/")
    page.is_visible("//div[@class='content'][contains(.,'For Teachers and For Students')]")
    page.click("//span[contains(.,'Register')]")
    page.is_visible("//h1[contains(.,'Register')]")
    page.click("//button[@id='asTeacher']")
    page.is_visible("//label[@for='first_name'][contains(.,'First Name *')]")
    page.is_visible("//label[@for='last_name'][contains(.,'Last Name *')]")
    page.is_visible("//label[@for='school'][contains(.,'School *')]")
    page.is_visible("//label[@for='text'][contains(.,'Email *')]")
    page.is_visible("//label[@for='password'][contains(.,'Password *')]")
    page.is_visible("//label[@for='repeat_password'][contains(.,'Repeat Password *')]")