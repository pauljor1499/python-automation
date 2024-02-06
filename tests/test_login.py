from turtle import pd
from assertpy import assert_that
import pdb
import pytest

@pytest.mark.student
def test_valid_student_login(page, student_login):        
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "Testing123!")    
    page.click("//span[contains(.,'Log In')]")  
    assert_that(page.is_visible("//div[@class='content'][contains(@id,'message')][contains(.,'Welcome to Math World')]")).is_true()    

@pytest.mark.student
def test_invalid_student_username(page, student_login):        
    page.fill("//input[@id='email']", "wrong_email@gmail.com")
    page.fill("//input[@id='password']", "Testing123!")
    page.click("//span[contains(.,'Log In')]")    
    assert_that(page.is_visible("//h3[contains(.,'Email or Password is incorrect.')]")).is_true()

@pytest.mark.student
def test_invalid_student_password(page, student_login):        
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "wdTest123!")
    page.click("//span[contains(.,'Log In')]")    
    assert_that(page.is_visible("//h3[contains(.,'Email or Password is incorrect.')]")).is_true()

@pytest.mark.student
def test_blank_student_username(page, student_login):  
    page.fill("//input[@id='email']", "")
    page.fill("//input[@id='password']", "Testing123!")
    page.click("//span[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()

@pytest.mark.student
def test_blank_student_password(page, student_login):        
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "")   
    page.click("//span[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password is required')]")).is_true()    

@pytest.mark.student
def test_blank_student_login(page, student_login):
    page.fill("//input[@id='email']", "")    
    page.fill("//input[@id='password']", "")
    page.click("//span[contains(.,'Log In')]")        
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password length should be 10 or more.')]")).is_true()

@pytest.mark.student
def test_short_student_username(page, student_login):
    page.fill("//input[@id='email']", "a@gmail.com")
    page.fill("//input[@id='password']", "Testing123!")
    page.click("//span[contains(.,'Log In')]")
    assert_that(page.is_visible("//h3[contains(.,'Email or Password is incorrect.')]")).is_true()

@pytest.mark.student
def test_short_student_password(page, student_login):
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "t")
    page.click("//span[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password length should be 10 or more.')]")).is_true()

@pytest.mark.student
def test_student_password_too_long(page, student_login):
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "Testing-Testing-Testing-Testing")
    page.click("//span[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Exceeded Number of Characters Allowed')]")).is_true()
    
@pytest.mark.teacher
def test_valid_teacher_login(page, teacher_login):    
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "Testing123!")
    page.click("//button[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='content'][contains(@id,'message')][contains(.,'Welcome to Math World')]")).is_true()

@pytest.mark.teacher
def test_invalid_teacher_username(page, teacher_login):    
    page.fill("//input[@id='email']", "wrong_email@gmail.com")
    page.fill("//input[@id='password']", "Testing123!")
    page.click("//button[contains(.,'Log In')]")
    assert_that(page.is_visible("//h3[contains(.,'Email or Password is incorrect.')]")).is_true()

@pytest.mark.teacher
def test_invalid_teacher_password(page, teacher_login):    
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "Testing123")
    page.click("//button[contains(.,'Log In')]")
    assert_that(page.is_visible("//h3[contains(.,'Email or Password is incorrect.')]")).is_true()
    
@pytest.mark.teacher
def test_blank_teacher_username(page, teacher_login):        
    page.fill("//input[@id='email']", "")
    page.fill("//input[@id='password']", "Testing123!")
    page.click("//button[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()

@pytest.mark.teacher
def test_blank_teacher_password(page, teacher_login):    
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "")  
    page.click("//button[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password is required')]")).is_true()

@pytest.mark.teacher
def test_blank_teacher_login(page, teacher_login):
    page.fill("//input[@id='email']", "")
    page.fill("//input[@id='password']", "")
    page.click("//button[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Email is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password is required')]")).is_true()
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password length should be 10 or more.')]")).is_true()

@pytest.mark.teacher
def test_short_teacher_username(page, teacher_login):
    page.fill("//input[@id='email']", "a@gmail.com")
    page.fill("//input[@id='password']", "Testing123!")
    page.click("//button[contains(.,'Log In')]")
    assert_that(page.is_visible("//h3[contains(.,'Email or Password is incorrect.')]")).is_true()

@pytest.mark.teacher
def test_short_teacher_password(page, teacher_login):
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "t")
    page.click("//button[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Password length should be 10 or more.')]")).is_true()

@pytest.mark.teacher
def test_teacher_password_too_long(page, teacher_login):
    page.fill("//input[@id='email']", "user123@gmail.com")
    page.fill("//input[@id='password']", "Testing-Testing-Testing-Testing")
    page.click("//span[contains(.,'Log In')]")
    assert_that(page.is_visible("//div[@class='errorMessage'][contains(.,'Exceeded Number of Characters Allowed')]")).is_true()

@pytest.fixture
def student_login(page):
    page.goto("/") 
    page.is_visible("//h1[contains(.,'Math World')]")  
    page.is_visible("//div[@class='content'][contains(.,'For Teachers and For Students')]")  
    page.click("//button[contains(.,'Log In')]")
    page.is_visible("//span[contains(.,'Student')]")    
    page.is_visible("//span[contains(.,'Teacher')]")    
   
@pytest.fixture
def teacher_login(page):
    page.goto("/")
    page.is_visible("//div[@class='content'][contains(.,'For Teachers and For Students')]")
    page.click("//span[contains(.,'Log In')]")
    page.is_visible("//h1[contains(.,'Log In')]")
    page.click("//button[@id='asTeacher']")
    page.is_visible("//label[@for='code'][contains(.,'Code')]")

