import pyautogui
import time

def catch(battle):
        print("Fighting...")

        battle = pyautogui.locateOnScreen("images/battle.png", grayscale=True, confidence = 0.7)

        pyautogui.moveTo(battle[0]+50, battle[1]+40, 2)
        pyautogui.click()

        time.sleep(1)

        false_swipe = pyautogui.locateOnScreen("images/false_swipe.png", grayscale=True, confidence = 0.7)

        pyautogui.moveTo(false_swipe[0]+80, false_swipe[1]+20, 2)
        pyautogui.click()

        time.sleep(10)

        print("Attempting to catch...")

        while pyautogui.locateOnScreen("images/battle.png", grayscale=True, confidence = 0.7) != None:

                pyautogui.moveTo(battle[0]+40, battle[1]+110, 2)
                pyautogui.click()

                pokeball = pyautogui.locateOnScreen("images/pokeball.png", grayscale=False, confidence = 0.7)

                pyautogui.moveTo(pokeball[0]+80, pokeball[1]+20, 2)
                pyautogui.click()

                time.sleep(20)

        print("Caught!")

def main():
        while True:
                pyautogui.keyDown('a')
                time.sleep(0.25)
                pyautogui.keyUp('a')
                pyautogui.keyDown('d')
                time.sleep(0.25)
                pyautogui.keyUp('d')

                battle = pyautogui.locateOnScreen("images/battle.png", grayscale = True, confidence = 0.7)

                if battle != None:
                        time.sleep(3)

                        rare_form = pyautogui.locateOnScreen("images/rare_encounter.png", confidence = 0.7)

                        if rare_form != None:
                                print("Rare form found.")
                                pyautogui.moveTo(rare_form[0]+250, rare_form[1]+160, 2)
                                pyautogui.click()
                                catch()

                        pyautogui.press('r')
                        time.sleep(3)

if __name__ == '__main__':
        main()
