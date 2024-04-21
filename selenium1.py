import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:5000/")

    def tearDown(self):
        self.driver.quit()

    def test_add_task(self):
        print("Adding tasks...")
        # Find the input field and submit button for adding a task
        input_field = self.driver.find_element(By.XPATH, "//*[@id='taskContent']")
        submit_button = self.driver.find_element(By.XPATH, "//*[@id='addTaskForm']/button")

        # Add three tasks
        for i in range(3):
            task_name = f"New task {i+1}"
            input_field.send_keys(task_name)
            submit_button.click()
            print(f"Added task: {task_name}")

            # Add a small delay to ensure the task is added before adding the next one
            time.sleep(1)

            # Re-find the input field after clicking the submit button
            input_field = self.driver.find_element(By.XPATH, "//*[@id='taskContent']")
            submit_button = self.driver.find_element(By.XPATH, "//*[@id='addTaskForm']/button")

        # Check if the tasks are added
        task_elements = self.driver.find_elements(By.CLASS_NAME, "taskContent")
        self.assertEqual(len(task_elements), 3)
        print("Tasks added successfully.")

        # Find all "Mark as Complete" buttons and click on them
        complete_buttons = self.driver.find_elements(By.CLASS_NAME, "completeButton")
        print(f"Total Mark as Complete buttons: {len(complete_buttons)}")
        for _ in range(len(complete_buttons)):
            complete_buttons = self.driver.find_elements(By.CLASS_NAME, "completeButton")  # Re-find the buttons
            complete_buttons[0].click()
            print("Clicked on Mark as Complete button.")

        # Verify if all tasks are marked as completed
        completed_tasks = self.driver.find_elements(By.CLASS_NAME, "completed")
        self.assertEqual(len(completed_tasks), 3)
        print("All tasks marked as completed.")

        # Find all "Delete" buttons and click on them
        delete_buttons = self.driver.find_elements(By.CLASS_NAME, "deleteButton")
        print(f"Total Delete buttons: {len(delete_buttons)}")
        
        for _ in range(len(delete_buttons)):
            #task_name = _.find_element(By.XPATH, "./preceding-sibling::span").text   
            delete_buttons = self.driver.find_elements(By.CLASS_NAME, "deleteButton")
            
            #print(f"Deleting task: {task_name}")
            delete_buttons[0].click()
            print("Clicked on Delete button.")
           

            # Add a small delay to ensure the task is deleted before checking for remaining tasks
        
        # Verify if all tasks are deleted
        remaining_tasks = self.driver.find_elements(By.CLASS_NAME, "taskContent")
        self.assertEqual(len(remaining_tasks), 0)
        print("All tasks deleted.")

if __name__ == "__main__":
    unittest.main()
