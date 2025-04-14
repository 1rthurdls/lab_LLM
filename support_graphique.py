import pygame 
import arthurLLm as LLm
import sys
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        # Check if the line fits within max_width
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)  # append last line
    return lines
pygame.init()

WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chat")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE_CHAT = (135, 206, 235)
BLUE = (0, 120, 215)
LIGHT_GREEN = (144, 238, 144)
GRAY = (200, 200, 200)

FONT = pygame.font.SysFont("arial", 20)

# Log de chat + entrée
chat_log = []
input_text = ""
current_model = "mistral"
provider = LLm.Provider(current_model)

# Définition des boutons
button_gemini = pygame.Rect(10, 10, 100, 30)
button_mistral = pygame.Rect(120, 10, 100, 30)

def draw_chat():
    win.fill(WHITE)

    # Affichage des boutons
    pygame.draw.rect(win, BLUE if current_model == "gemini" else GRAY, button_gemini)
    pygame.draw.rect(win, BLUE if current_model == "mistral" else GRAY, button_mistral)

    win.blit(FONT.render("Gemini", True, WHITE), (button_gemini.x + 15, button_gemini.y + 5))
    win.blit(FONT.render("Mistral", True, WHITE), (button_mistral.x + 15, button_mistral.y + 5))

    # Affichage du modèle sélectionné
    model_text = FONT.render(f"Modèle actuel : {current_model}", True, BLACK)
    win.blit(model_text, (250, 15))

    # Affichage du chat
    y = 60
    max_width = WIDTH - 40  # espace sur les côtés

    for msg in chat_log[-20:]:
        lines = wrap_text(msg, FONT, max_width)
        for line in lines:
            rendered_text = FONT.render(line, True, BLACK)
            win.blit(rendered_text, (20, y))
            y += 22  # hauteur entre les lignes


    # Champ de texte utilisateur
    pygame.draw.rect(win, BLUE_CHAT, (10, HEIGHT - 40, WIDTH - 20, 30))
    input_surface = FONT.render(input_text, True, BLACK)
    win.blit(input_surface, (15, HEIGHT - 35))

    pygame.display.flip()

def fake_bot_response(user_msg):
    global provider
    provider = LLm.Provider(current_model)
    llm = LLm.ArthurLLM(provider, user_msg)
    response = llm.answer()
    return f"Bot ({current_model}): {response}"

# Boucle principale
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_gemini.collidepoint(event.pos):
                current_model = "gemini"
            elif button_mistral.collidepoint(event.pos):
                current_model = "mistral"

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.strip():
                    chat_log.append("Moi: " + input_text)
                    response = fake_bot_response(input_text)
                    chat_log.append(response)
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    draw_chat()

pygame.quit()
sys.exit()
