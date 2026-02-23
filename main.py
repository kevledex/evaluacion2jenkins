import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def esperar_elemento(driver, by, locator, condicion="clickable", timeout=15):
    wait = WebDriverWait(driver, timeout)
    if condicion == "clickable":
        return wait.until(EC.element_to_be_clickable((by, locator)))
    elif condicion == "invisible":
        return wait.until(EC.invisibility_of_element_located((by, locator)))
    elif condicion == "visible":
        return wait.until(EC.visibility_of_element_located((by, locator)))
    else:
        return wait.until(EC.presence_of_element_located((by, locator)))

service = Service("chromedriver.exe") 
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://webdriveruniversity.com/Ajax-Loader/index.html")
    driver.maximize_window()

    print("Esperando a que el loader desaparezca...")
    tiempo_inicio = time.time()

    esperar_elemento(driver, By.ID, "loader", condicion="invisible")
    
    boton_click_me = esperar_elemento(driver, By.XPATH, "//*[@id='button1']/p", condicion="clickable")
    
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    
    print(f"¡Listo! El loader desapareció en {tiempo_total:.2f} segundos.")
    
    boton_click_me.click()

    modal = esperar_elemento(driver, By.CLASS_NAME, "modal-content", condicion="visible")
    
    assert modal.is_displayed(), "Error: El modal no apareció después de hacer clic."
    print("Validación exitosa: El modal se desplegó correctamente en pantalla.")

finally:
    print("Cerrando el navegador...")
    driver.quit()