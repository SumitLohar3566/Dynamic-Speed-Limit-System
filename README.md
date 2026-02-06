### Dynamic Speed Limit System 

The Dynamic Speed Limit System is an interactive Streamlit web application that dynamically determines speed limits for light and heavy vehicles based on time of day, weather conditions, and selected highways.

It is designed to promote road safety, smart driving, and traffic awareness using a visually rich and intuitive interface.

# Key Features:

- Select from 20+ major Indian highways

- Time-based speed limit calculation

- Weather-aware driving conditions

- Separate limits for light & heavy vehicles

- Automatic safety warnings for risky conditions

- Speed-limit trends table

- Downloadable CSV speed report

- Premium animated UI with modern styling

# Tech Stack:

- Language: Python

- Framework: Streamlit

- Data Handling: Pandas, NumPy

- UI Styling: Custom HTML + CSS

- Export: CSV report generation

# Project Structure:
Dynamic-Speed-Limit-System/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── README.md               # Documentation
├── screenshots/            # (Optional) UI screenshots
│   ├── home.png
│   ├── result.png
│   └── report.png

# Installation & Setup
1. Clone the Repository
git clone https://https://github.com/SumitLohar3566/Dynamic-Speed-Limit-System/tree/master

2. Install Dependencies
pip install -r requirements.txt

3. Run the Application
streamlit run app.py

# How It Works

- Select a highway

- Choose time slot and date

- Click Calculate Speed Limits

# The system:

- Determines weather & road condition

- Assigns safe speed limits

- Displays warnings if required

- Download a CSV speed limit report

# Speed Logic (Algorithm):
Time Slot	Light Vehicles	Heavy Vehicles	Condition
6–9 AM	60 km/h	40 km/h	Fog
9–12 PM	100 km/h	80 km/h	Clear
12–3 PM	80 km/h	60 km/h	Light Rain
3–7 PM	60 km/h	40 km/h	Heavy Rain
7 PM+	100 km/h	80 km/h	Clear Night

- Algorithm is constant & deterministic
- No random values used

## Screenshots:
<img width="1656" height="717" alt="Screenshot 2026-01-15 090027" src="https://github.com/user-attachments/assets/82f91211-3e2a-4581-83cf-0f1fa4c6fcfb" />
<img width="1905" height="615" alt="Screenshot 2026-01-15 090040" src="https://github.com/user-attachments/assets/fc61ac51-6e47-4611-acdc-231d5b498610" />
<img width="1809" height="650" alt="Screenshot 2026-01-15 090054" src="https://github.com/user-attachments/assets/2576d8c7-d166-4862-97e8-2ceb0cb79227" />
<img width="1849" height="773" alt="Screenshot 2026-01-15 090105" src="https://github.com/user-attachments/assets/d04edf54-ee65-423e-9bbc-5a7d537c9f24" />
<img width="1883" height="728" alt="Screenshot 2026-01-15 090118" src="https://github.com/user-attachments/assets/05fac7f7-4258-4dfe-a3af-4449e9a4c7fa" />
<img width="1898" height="750" alt="Screenshot 2026-01-15 090131" src="https://github.com/user-attachments/assets/96048aee-5e9a-40c8-9479-031018b46c6e" />
<img width="1876" height="772" alt="Screenshot 2026-01-15 090146" src="https://github.com/user-attachments/assets/a331b2aa-f5ec-4f7d-a8c4-0fd99dae02e6" />
<img width="1483" height="833" alt="Screenshot 2026-01-15 090309" src="https://github.com/user-attachments/assets/c53d4094-f023-4c40-bdc6-1e1a3b9e619e" />
<img width="1486" height="870" alt="Screenshot 2026-01-15 090320" src="https://github.com/user-attachments/assets/48deefe7-7dc6-41b1-9486-e51cead8eec2" />

- Disclaimer

This application is a simulation tool for awareness and educational purposes.
Actual speed limits are governed by local traffic authorities.

# Future Enhancements

- Real-time weather API integration

- GPS-based automatic highway detection

- Mobile-optimized layout

- AI-based traffic prediction

- Cloud deployment dashboard

- Contact Developer: Sumit Lohar
- Email:sumitlohar063@gmail.com
- GitHub: https://github.com/SumitLohar3566
- LinkedIn:(https://www.linkedin.com/in/sumit-lohar-498341317/)
