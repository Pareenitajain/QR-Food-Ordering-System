# QR Code-Based Food Ordering System 🍽️

A complete **web-based food ordering system** for restaurants where customers can simply **scan a QR code**, view the digital menu, place orders, and the restaurant admin can manage all orders in **real time**.

---

## 📌 Project Overview

- **Problem:** Traditional ordering requires waiters, paper menus, or phone calls, which is slow and error-prone.  
- **Solution:** A QR code-based web application where customers use their own smartphones to browse the menu and place orders.  
- **Deployment Mode:**  
  - ✅ Fully working on **local Wi‑Fi network**  
  - 🌐 Online deployment using platforms like Render/Railway is planned as **future enhancement**

---

## ✨ Features

### 👤 Customer Side

- Scan QR code to open menu (no app installation needed).  
- View food items in a **card-based menu** with name, price, and description.  
- Add items to cart and see **real-time total amount**.  
- Place order without login.  
- Receive **Order ID and confirmation message** after successful order.

### 👨‍💼 Admin / Owner Side

- **Real-time admin dashboard** to view all orders.  
- Sound notification when a new order is received.  
- View complete order details (items, quantity, total, time).  
- Update order status: `Received → Preparing → Completed`.  
- Auto-refresh dashboard every few seconds for live updates.

---

## 🏗️ System Architecture

```
CUSTOMER
  ↓ (Scan QR Code)
MENU PAGE (HTML/CSS/JS)
  ↓ (Place Order)
FLASK BACKEND (Python)
  ↓ (Save Data)
SQLITE DATABASE
  ↓ (Show Orders)
ADMIN DASHBOARD
  ↓
ADMIN / RESTAURANT OWNER
```

---

## 🛠️ Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5  
- **Backend:** Python, Flask  
- **Database:** SQLite  
- **QR Code Generation:** Python `qrcode` library  
- **Development Tools:** VS Code, Chrome  

---

## 💾 Database Design

### `Food` Table

- `id` – Primary Key  
- `name` – Food item name  
- `price` – Price (in INR)  
- `description` – Short description

### `Order` Table

- `id` – Order ID (Primary Key)  
- `items` – List / JSON of ordered items  
- `total_price` – Total order amount  
- `status` – `Received / Preparing / Completed`  
- `time` – Timestamp when order was placed

---

## 🚀 How to Run (Local Deployment)

1. **Clone the repository**

   ```
   git clone https://github.com/<your-username>/QR-Food-Ordering-System.git
   cd QR-Food-Ordering-System
   ```

2. **Create virtual environment (optional but recommended)**

   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Run the Flask application**

   ```
   python app.py
   ```

5. **Access the app**

   - Customer menu: `http://<your_ip>:5000/`  
   - Admin dashboard: `http://<your_ip>:5000/admin`  

   Make sure **laptop and mobile are on the same Wi‑Fi**. Generate a QR code pointing to `http://<your_ip>:5000/` and scan it from your phone.

---

## 📸 Screenshots (Suggested)



- Menu Page (Customer View)
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/67c88486-a4de-4539-9c09-20628353c38a" />

- Order Confirmation Page
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/28b87178-eb84-406e-a1eb-576f5e86ea0b" />
  
- Admin Dashboard (Orders List)
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/046a3202-2e66-4340-add2-09b188bec980" />
  

---

## ✅ Project Status

- All **functional requirements** for customer and admin modules implemented.  
- Fully working demo on **local network** with QR code-based access.  
- Code is clean, modular, and easy to extend.

---

## 🔮 Future Enhancements

- Online deployment using platforms like Render / Railway / Vercel.  
- Payment gateway integration (Razorpay / PayPal).  
- Table number mapping for dine-in orders.  
- Sales analytics and reports (popular items, peak hours, daily revenue).  
- Multi-language support (English, Hindi, regional languages).  
- Mobile app version with push notifications.

---

## 📧 Contact

- **Developer:** Pareenita Jain  
- **Email:** parineetajain0902@gmail.com  
- **GitHub:** https://github.com/Pareenitajain/QR-Food-Ordering-System

---


[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/89339071/73d878c1-351d-4775-8eb0-1c94aa79c486/WhatsApp-Image-2025-12-25-at-14.25.03_81c911a7.jpg)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/89339071/a48d50be-9b40-4fd6-bfc7-a487c5815b4e/image.jpg)
[3](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/89339071/8878a270-5cb2-4263-a902-1b818e7ccc5b/image.jpg)
[4](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/89339071/9762d4a4-ff31-48f6-bbd4-74717c0ade6f/image.jpg)
[5](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/89339071/ac19949b-1356-4dd3-b5af-e6cadc674419/image.jpg)
[6](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/89339071/77237028-19b3-4772-a981-b1a0a52489ca/image.jpg)
[7](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/89339071/1a3d932d-df5d-48a0-9e72-4c41189731c3/image.jpg)
[8](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/89339071/c918212f-b187-40c0-b6bd-88b38833c410/image.jpg)
