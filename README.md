# 📹 Motion Detection App with Email Alerts

Una aplicación en Python que detecta movimiento usando la cámara web, captura una imagen del objeto en movimiento y envía una alerta por correo electrónico con la imagen adjunta.

---

## 🔧 Tecnologías utilizadas

- Python 3
- OpenCV (`cv2`)
- `smtplib` (envío de correo)
- `threading` (para enviar sin bloquear la app)
- `dotenv` (para ocultar credenciales)
- `imghdr` y `email.message` (para armar el email)

---

## 🚀 ¿Qué hace esta app?

- Abre la webcam y analiza los fotogramas en tiempo real.
- Detecta diferencias significativas en la imagen (movimiento).
- Captura una imagen cuando detecta movimiento.
- Envía un correo electrónico con la imagen adjunta.
- Todo ocurre automáticamente, sin frenar el flujo del video.

---

## 🛠️ Instalación

1. Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/motion-detection-app.git
cd motion-detection-app
