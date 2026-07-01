import cv2
import mediapipe as mp
import os
import math

# 1. Siapkan Kamera & Mesin MediaPipe
cap = cv2.VideoCapture(0)

# Mesin 1: Pelacak Wajah
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)

# Mesin 2: Pelacak Tangan
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)

# 2. Fungsi memuat gambar avatar
def load_avatar(emotion):
    filename = f"{emotion}.png" 
    if os.path.exists(filename):
        return cv2.imread(filename)
    else:
        import numpy as np
        return np.zeros((300, 300, 3), dtype="uint8")

avatars = {
    "happy": load_avatar("happy"),
    "angry": load_avatar("angry"),
    "neutral": load_avatar("neutral"),
    "fear": load_avatar("fear"),
    "sad": load_avatar("sad")
}

# Fungsi pembantu untuk mengukur jarak
def hitung_jarak(titik1, titik2, landmarks, lebar_frame, tinggi_frame):
    x1, y1 = int(landmarks[titik1].x * lebar_frame), int(landmarks[titik1].y * tinggi_frame)
    x2, y2 = int(landmarks[titik2].x * lebar_frame), int(landmarks[titik2].y * tinggi_frame)
    return math.hypot(x2 - x1, y2 - y1)

# Fungsi pembantu khusus untuk hitung jarak pixel langsung
def hitung_jarak_pixel(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    tinggi, lebar, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # AI Memproses Wajah dan Tangan secara bersamaan
    hasil_wajah = face_mesh.process(rgb_frame)
    hasil_tangan = hands.process(rgb_frame)

    current_emotion = "neutral"

    # Bendera (Flag) untuk Gestur Tangan
    tangan_di_atas_kepala = False
    tangan_di_mata = False

    # Pastikan AI melihat wajah DAN tangan sekaligus
    if hasil_tangan.multi_hand_landmarks and hasil_wajah.multi_face_landmarks:
        face_landmarks = hasil_wajah.multi_face_landmarks[0].landmark
        
        dahi_y = face_landmarks[10].y
        
        mata_kiri_x = int(face_landmarks[159].x * lebar)
        mata_kiri_y = int(face_landmarks[159].y * tinggi)
        mata_kanan_x = int(face_landmarks[386].x * lebar)
        mata_kanan_y = int(face_landmarks[386].y * tinggi)

        tinggi_wajah_ref = hitung_jarak(10, 152, face_landmarks, lebar, tinggi)
        
        for hand_landmarks in hasil_tangan.multi_hand_landmarks:
            hand_9_y = hand_landmarks.landmark[9].y
            hand_9_pixel_x = int(hand_landmarks.landmark[9].x * lebar)
            hand_9_pixel_y = int(hand_landmarks.landmark[9].y * tinggi)
            
            # GESTUR 1: ANGRY (Tangan di atas dahi)
            if hand_9_y < dahi_y:
                tangan_di_atas_kepala = True
                
            # GESTUR 2: SAD (Tangan Dekat Mata)
            jarak_ke_mata_kiri = hitung_jarak_pixel(hand_9_pixel_x, hand_9_pixel_y, mata_kiri_x, mata_kiri_y)
            jarak_ke_mata_kanan = hitung_jarak_pixel(hand_9_pixel_x, hand_9_pixel_y, mata_kanan_x, mata_kanan_y)
            
            threshold_sad = 0.25 * tinggi_wajah_ref
            
            if jarak_ke_mata_kiri < threshold_sad or jarak_ke_mata_kanan < threshold_sad:
                tangan_di_mata = True
                break 

    # --- MENGUKUR LOGIKA WAJAH ---
    if hasil_wajah.multi_face_landmarks:
        for face_landmarks in hasil_wajah.multi_face_landmarks:
            lebar_wajah_ref = hitung_jarak(234, 454, face_landmarks.landmark, lebar, tinggi)
            if lebar_wajah_ref == 0: lebar_wajah_ref = 0.1 
            
            mangap = hitung_jarak(13, 14, face_landmarks.landmark, lebar, tinggi) / lebar_wajah_ref
            lebar_bibir = hitung_jarak(61, 291, face_landmarks.landmark, lebar, tinggi) / lebar_wajah_ref
            
            # --- PENENTUAN EMOSI (PRIORITAS) ---
            if tangan_di_mata:
                current_emotion = "sad"
            elif tangan_di_atas_kepala:
                current_emotion = "angry"
            elif mangap > 0.15:
                current_emotion = "fear"
            elif lebar_bibir > 0.45:
                current_emotion = "happy"
            else:
                current_emotion = "neutral"
                
            # TEKS BANTUAN KALIBRASI DIHAPUS DARI SINI

    # --- MENAMPILKAN HASIL ---
    avatar_image = avatars[current_emotion]
    avatar_image = cv2.resize(avatar_image, (300, 300), interpolation=cv2.INTER_CUBIC)
    
    # Teks diubah menjadi "Emosi: ..."
    cv2.putText(frame, f"Emosi: {current_emotion}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

    cv2.imshow('Kamera Asli', frame)
    cv2.imshow('Avatar 2D', avatar_image)

    # Tekan 'q' untuk mematikan program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()