# # from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
# # from werkzeug.utils import secure_filename
# # from flask_sqlalchemy import SQLAlchemy
# # import os
# #
# # app = Flask(__name__)
# # app.secret_key = 'your_secret_key'  # Replace with a strong secret key
# # app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #
# # db = SQLAlchemy(app)
# #
# # # Create the upload folder if it doesn't exist
# # if not os.path.exists(app.config['UPLOAD_FOLDER']):
# #     os.makedirs(app.config['UPLOAD_FOLDER'])
# #
# # # Admin credentials
# # ADMIN_USERNAME = "Okechukwu"
# # ADMIN_PASSWORD = "Ebube"
# #
# # # Database model for user registration data
# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     fullname = db.Column(db.String(100), nullable=False)
# #     state_of_origin = db.Column(db.String(50), nullable=False)
# #     country = db.Column(db.String(50), nullable=False)
# #     gender = db.Column(db.String(10), nullable=False)
# #     dob = db.Column(db.String(20), nullable=False)
# #     picture_path = db.Column(db.String(100), nullable=True)
# #     video_path = db.Column(db.String(100), nullable=True)
# #
# # # Initialize the database
# # with app.app_context():
# #     db.create_all()
# #
# # @app.route('/')
# # def index():
# #     return redirect(url_for('register'))
# #
# # @app.route('/register', methods=['GET', 'POST'])
# # def register():
# #     if request.method == 'POST':
# #         # Get form data
# #         fullname = request.form.get('fullname')
# #         state_of_origin = request.form.get('state_of_origin')
# #         country = request.form.get('country')
# #         gender = request.form.get('gender')
# #         dob = request.form.get('dob')
# #
# #         # Handle file uploads
# #         picture = request.files.get('picture')
# #         video = request.files.get('video')
# #
# #         picture_path = None
# #         video_path = None
# #
# #         # Save picture if uploaded
# #         if picture:
# #             picture_filename = secure_filename(picture.filename)
# #             picture_path = picture_filename  # Save only filename
# #             picture.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_filename))
# #
# #         # Save video if uploaded
# #         if video:
# #             video_filename = secure_filename(video.filename)
# #             video_path = video_filename  # Save only filename
# #             video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))
# #
# #         # Create a new user record in the database
# #         new_user = User(
# #             fullname=fullname,
# #             state_of_origin=state_of_origin,
# #             country=country,
# #             gender=gender,
# #             dob=dob,
# #             picture_path=picture_path,
# #             video_path=video_path
# #         )
# #         db.session.add(new_user)
# #         db.session.commit()
# #
# #         flash('Registration successful!')
# #         return redirect(url_for('register'))
# #
# #     return render_template('register.html')
# #
# # @app.route('/admin_login', methods=['GET', 'POST'])
# # def admin():
# #     if request.method == 'POST':
# #         username = request.form.get('username')
# #         password = request.form.get('password')
# #
# #         if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
# #             session['admin_logged_in'] = True
# #             return redirect(url_for('admin_dashboard'))
# #         else:
# #             flash('Invalid credentials, please try again.')
# #             return redirect(url_for('admin'))
# #
# #     return render_template('admin_login.html')
# #
# #
# # @app.route('/admin_dashboard')
# # def admin_dashboard():
# #     # Check if the admin is logged in
# #     if not session.get('admin_logged_in'):
# #         flash('Please log in to access the admin dashboard.')
# #         return redirect(url_for('admin'))
# #
# #     # Retrieve all users from the database
# #     users = User.query.all()
# #     return render_template('admin.html', users=users)
# #
# # @app.route('/logout')
# # def logout():
# #     session.pop('admin_logged_in', None)
# #     flash('Logged out successfully.')
# #     return redirect(url_for('admin'))
# #
# # # Serve uploaded files (pictures and videos)
# # @app.route('/uploads/<filename>')
# # def uploaded_file(filename):
# #     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
#
# from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
# from werkzeug.utils import secure_filename
# from flask_sqlalchemy import SQLAlchemy
# import os
#
# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace with a strong secret key
# app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# # Create the upload folder if it doesn't exist
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
#
# # Admin credentials
# ADMIN_USERNAME = "Okechukwu"
# ADMIN_PASSWORD = "Ebube"
#
#
# # Database model for user registration data
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fullname = db.Column(db.String(100), nullable=False)
#     state_of_origin = db.Column(db.String(50), nullable=False)
#     country = db.Column(db.String(50), nullable=False)
#     gender = db.Column(db.String(10), nullable=False)
#     dob = db.Column(db.String(20), nullable=False)
#     title = db.Column(db.String(50), nullable=True)
#     company = db.Column(db.String(100), nullable=True)
#     area_of_expertise = db.Column(db.String(100), nullable=True)
#     picture_path = db.Column(db.String(100), nullable=True)
#     video_path = db.Column(db.String(100), nullable=True)
#
#
# # Initialize the database
# with app.app_context():
#     db.create_all()
#
#
# @app.route('/')
# def index():
#     return redirect(url_for('register'))
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         fullname = request.form.get('fullname')
#         state_of_origin = request.form.get('state_of_origin')
#         country = request.form.get('country')
#         gender = request.form.get('gender')
#         dob = request.form.get('dob')
#         title = request.form.get('title')
#         company = request.form.get('company')
#         area_of_expertise = request.form.get('area_of_expertise')
#
#         picture = request.files.get('picture')
#         video = request.files.get('video')
#
#         picture_path = None
#         video_path = None
#
#         if picture:
#             picture_filename = secure_filename(picture.filename)
#             picture_path = picture_filename
#             picture.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_filename))
#
#         if video:
#             video_filename = secure_filename(video.filename)
#             video_path = video_filename
#             video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))
#
#         new_user = User(
#             fullname=fullname,
#             state_of_origin=state_of_origin,
#             country=country,
#             gender=gender,
#             dob=dob,
#             title=title,
#             company=company,
#             area_of_expertise=area_of_expertise,
#             picture_path=picture_path,
#             video_path=video_path
#         )
#         db.session.add(new_user)
#         db.session.commit()
#
#         flash('Registration successful!')
#         return redirect(url_for('register'))
#
#     return render_template('register.html')
#
#
# @app.route('/admin_login', methods=['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#
#         if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#             session['admin_logged_in'] = True
#             return redirect(url_for('admin_dashboard'))
#         else:
#             flash('Invalid credentials, please try again.')
#             return redirect(url_for('admin'))
#
#     return render_template('admin_login.html')
#
#
# @app.route('/admin_dashboard')
# def admin_dashboard():
#     if not session.get('admin_logged_in'):
#         flash('Please log in to access the admin dashboard.')
#         return redirect(url_for('admin'))
#
#     users = User.query.all()
#     return render_template('admin.html', users=users)
#
#
# @app.route('/logout')
# def logout():
#     session.pop('admin_logged_in', None)
#     flash('Logged out successfully.')
#     return redirect(url_for('admin'))
#
#
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Admin credentials
ADMIN_USERNAME = "Okechukwu"
ADMIN_PASSWORD = "Ebube"

# Countries and states data
countries_and_states = {
    "United States": [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
        "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
        "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
        "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
        "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
        "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
        "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ],
"Italy": [
        "Abruzzo", "Basilicata", "Calabria", "Campania", "Emilia-Romagna", "Friuli Venezia Giulia", "Lazio", "Liguria",
        "Lombardy", "Marche", "Molise", "Piedmont", "Apulia", "Sardinia", "Sicily", "Tuscany", "Trentino-Alto Adige/Südtirol",
        "Umbria", "Aosta Valley", "Veneto"
    ],
    "Japan": [
        "Aichi", "Akita", "Aomori", "Chiba", "Ehime", "Fukui", "Fukuoka", "Fukushima", "Gifu", "Gunma", "Hiroshima", "Hokkaido",
        "Hyogo", "Ibaraki", "Ishikawa", "Ishikawa", "Iwate", "Kagawa", "Kagoshima", "Kanagawa", "Kochi", "Kumamoto", "Kyoto", "Mie",
        "Miyagi", "Miyazaki", "Nagano", "Nagasaki", "Nara", "Niigata", "Okinawa", "Osaka", "Saga", "Saitama", "Shiga", "Shimane",
        "Shizuoka", "Tochigi", "Tokushima", "Tokyo", "Tottori", "Toyama", "Wakayama", "Yamagata", "Yamaguchi", "Yokohama"
    ],
    "South Korea": [
        "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Ulsan", "Gyeonggi", "Gangwon", "Chungcheongbuk",
        "Chungcheongnam", "Jeollabuk", "Jeollanam", "Gyeongsangbuk", "Gyeongsangnam", "Jeju"
    ],
    "Argentina": [
        "Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa",
        "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe",
        "Santiago del Estero", "Tierra del Fuego", "Tucumán"
    ],
    "Italy": [
        "Abruzzo", "Basilicata", "Calabria", "Campania", "Emilia-Romagna", "Friuli Venezia Giulia", "Lazio", "Liguria",
        "Lombardy", "Marche", "Molise", "Piedmont", "Apulia", "Sardinia", "Sicily", "Tuscany", "Trentino-Alto Adige/Südtirol",
        "Umbria", "Aosta Valley", "Veneto"
    ],
    "Egypt": [
        "Alexandria", "Aswan", "Asyut", "Beheira", "Beni Suef", "Cairo", "Dakahlia", "Damietta", "Faiyum", "Gharbia",
        "Giza", "Ismailia", "Kafr el-Sheikh", "Luxor", "Matruh", "Minya", "Monufia", "New Valley", "North Sinai", "Port Said",
        "Qalyubia", "Qena", "Red Sea", "Sharqia", "Sohag", "South Sinai", "Suez"
    ],
    "Saudi Arabia": [
        "Al Bahah", "Al Hudud ash Shamaliyah", "Al Jawf", "Asir", "Eastern Province", "Jizan", "Makkah", "Medina",
        "Mintaqat al-Qasim", "Mintaqat Riyad", "Mintaqat Tabuk", "Najran", "Northern Borders", "Riyadh", "Sharqiyah", "Southern Province"
    ],
    "United Arab Emirates": [
        "Abu Dhabi", "Ajman", "Dubai", "Fujairah", "Ras al-Khaimah", "Sharjah", "Umm al-Quwain"
    ],
    "Turkey": [
        "Adana", "Adiyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin",
        "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale",
        "Çorum", "Denizli", "Diyarbakir", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep",
        "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman",
        "Kastamonu", "Kayseri", "Kilis", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla",
        "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Sivas",
        "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat"
    ],
    "Spain": [
        "Andalusia", "Aragon", "Asturias", "Balearic Islands", "Basque Country", "Canary Islands", "Cantabria", "Castile and Leon",
        "Castilla-La Mancha", "Catalonia", "Extremadura", "Galicia", "Madrid", "Murcia", "Navarre", "La Rioja", "Valencia"
    ],
"France": [
        "Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Brittany", "Centre-Val de Loire", "Corsica", "Grand Est", "Hauts-de-France",
        "Île-de-France", "Normandy", "Nouvelle-Aquitaine", "Occitanie", "Pays de la Loire", "Provence-Alpes-Côte d'Azur"
    ],
    "Germany": [
        "Baden-Württemberg", "Bavaria", "Berlin", "Brandenburg", "Bremen", "Hamburg", "Hesse", "Lower Saxony", "Mecklenburg-Vorpommern",
        "North Rhine-Westphalia", "Rhineland-Palatinate", "Saarland", "Saxony", "Saxony-Anhalt", "Schleswig-Holstein", "Thuringia"
    ],
    "Mexico": [
        "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Coahuila", "Colima",
        "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Mexico City", "Mexico State", "Michoacán", "Morelos", "Nayarit",
        "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco",
        "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
    ],
    "Brazil": [
        "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
        "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul",
        "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
    ],
    "China": [
        "Anhui", "Beijing", "Chongqing", "Fujian", "Gansu", "Guangdong", "Guangxi", "Guizhou", "Hainan", "Hebei", "Heilongjiang",
        "Henan", "Hubei", "Hunan", "Jiangsu", "Jiangxi", "Jilin", "Liaoning", "Ningxia", "Qinghai", "Shaanxi", "Shandong", "Shanghai",
        "Shanxi", "Sichuan", "Tianjin", "Tibet", "Xinjiang", "Yunnan", "Zhejiang"
    ],
    "South Africa": [
        "Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "North West", "Northern Cape", "Western Cape"
    ],
    "United Kingdom": [
        "England", "Northern Ireland", "Scotland", "Wales"
    ],
    "Russia": [
        "Adygea", "Altai", "Amur", "Arkhangelsk", "Astrakhan", "Bashkortostan", "Belgorod", "Bryansk", "Buryatia", "Chechnya",
        "Chelyabinsk", "Chukchi", "Chuvashia", "Dagestan", "Ingushetia", "Irkutsk", "Ivanovo", "Jewish Autonomous", "Kabardino-Balkaria",
        "Kaliningrad", "Kaluga", "Kamchatka", "Karachay-Cherkessia", "Kemerovo", "Kirov", "Komi", "Kostroma", "Krasnodar", "Krasnoyarsk",
        "Kurgan", "Kursk", "Leningrad", "Lipetsk", "Magadan", "Mordovia", "Moscow", "Moscow City", "Murmansk", "Nizhny Novgorod",
        "North Ossetia", "Omsk", "Orenburg", "Oryol", "Penza", "Perm", "Primorye", "Pskov", "Rostov", "Ryazan", "Sakhalin",
        "Samara", "Saratov", "Smolensk", "St. Petersburg", "Stavropol", "Sverdlovsk", "Tambov", "Tatarstan", "Tomsk", "Tula", "Tver",
        "Tyumen", "Udmurtia", "Ulyanovsk", "Vladimir", "Volgograd", "Vologda", "Voronezh", "Yamalo-Nenets", "Yaroslavl", "Zabaykalsky"
    ],
    "Egypt": [
        "Alexandria", "Aswan", "Asyut", "Beheira", "Beni Suef", "Cairo", "Dakahlia", "Damietta", "Faiyum", "Gharbia",
        "Giza", "Ismailia", "Kafr el-Sheikh", "Luxor", "Matruh", "Minya", "Monufia", "New Valley", "North Sinai", "Port Said",
        "Qalyubia", "Qena", "Red Sea", "Sharqia", "Sohag", "South Sinai", "Suez"
    ],"Japan": [
        "Aichi", "Akita", "Amami", "Aomori", "Chiba", "Ehime", "Fukuoka", "Fukui", "Fukushima", "Gifu", "Gunma", "Hiroshima",
        "Hokkaido", "Hyogo", "Ibaraki", "Ishikawa", "Ishigaki", "Iwami", "Kagawa", "Kagoshima", "Kanagawa", "Kochi", "Kumamoto",
        "Kyoto", "Mie", "Miyagi", "Miyazaki", "Nagano", "Nagasaki", "Nara", "Niigata", "Okinawa", "Osaka", "Port of Kobe",
        "Saga", "Saitama", "Shiga", "Shimane", "Shizuoka", "Tochigi", "Tokushima", "Tokyo", "Tottori", "Toyama", "Wakayama", "Yamagata",
        "Yamaguchi", "Yokohama"
    ],
    "South Korea": [
        "Chungcheongbuk", "Chungcheongnam", "Gyeonggi", "Gyeongsangbuk", "Gyeongsangnam", "Jeju", "Jeollabuk", "Jeollanam",
        "Sejong", "Seoul", "Incheon", "Busan", "Ulsan"
    ],
    "Italy": [
        "Abruzzo", "Aosta Valley", "Apulia", "Basilicata", "Calabria", "Campania", "Emilia-Romagna", "Friuli Venezia Giulia", "Lazio",
        "Liguria", "Lombardy", "Marche", "Molise", "Piedmont", "Sardinia", "Sicily", "Tuscany", "Trentino-Alto Adige/Südtirol",
        "Umbria", "Veneto"
    ],
    "Spain": [
        "Andalusia", "Aragon", "Asturias", "Balearic Islands", "Canary Islands", "Cantabria", "Castilla-La Mancha", "Castilla y León",
        "Catalonia", "Extremadura", "Galicia", "Madrid", "Murcia", "Navarre", "La Rioja", "Basque Country", "Valencia"
    ],
    "Argentina": [
        "Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja",
        "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero",
        "Tierra del Fuego", "Tucumán"
    ],
    "Italy": [
        "Abruzzo", "Aosta Valley", "Apulia", "Basilicata", "Calabria", "Campania", "Emilia-Romagna", "Friuli Venezia Giulia", "Lazio",
        "Liguria", "Lombardy", "Marche", "Molise", "Piedmont", "Sardinia", "Sicily", "Tuscany", "Trentino-Alto Adige/Südtirol",
        "Umbria", "Veneto"
    ],
    "Kenya": [
        "Baringo", "Bomet", "Bungoma", "Busia", "Elgeyo-Marakwet", "Embu", "Garissa", "Homa Bay", "Isiolo", "Kajiado", "Kakamega", "Kericho",
        "Kiambu", "Kilifi", "Kirinyaga", "Kisii", "Kisumu", "Kitui", "Kwale", "Laikipia", "Lamu", "Makueni", "Mandera", "Marsabit",
        "Mombasa", "Murang'a", "Nairobi", "Nakuru", "Nandi", "Narok", "Nyamira", "Nyandarua", "Nyanza", "Samburu", "Siaya", "Taita Taveta",
        "Tana River", "Tharaka Nithi", "Trans-Nzoia", "Uasin Gishu", "Vihiga", "Wajir", "West Pokot"
    ],
    "Indonesia": [
        "Aceh", "Bali", "Banten", "Bengkulu", "Gorontalo", "Jakarta", "Jambi", "West Java", "Central Java", "East Java", "Kalimantan",
        "Lampung", "Maluku", "North Maluku", "Nusa Tenggara Barat", "Nusa Tenggara Timur", "Papua", "Riau", "South Kalimantan",
        "South Sulawesi", "South Sumatra", "Southeast Sulawesi", "West Kalimantan", "West Papua", "Yogyakarta"
    ],
    "Turkey": [
        "Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydin",
        "Balikesir", "Bartin", "Batman", "Bayburt", "Bilecik", "Bingol", "Bitlis", "Bolu", "Burdur", "Bursa", "Canakkale", "Cankiri",
        "Corum", "Denizli", "Diyarbakir", "Edirne", "Elazig", "Erzincan", "Erzurum", "Eskisehir", "Gaziantep", "Giresun", "Gumushane",
        "Hakkari", "Hatay", "Igdir", "Isparta", "Istanbul", "Izmir", "Kahramanmaras", "Karabuk", "Karaman", "Kars", "Kastamonu",
        "Kayseri", "Kirikkale", "Kirklareli", "Kirsehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mugla",
        "Mus", "Nevsehir", "Nigde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Sanliurfa", "Siirt", "Sinop", "Sirnak", "Sivas",
        "Tekirdag", "Tokat", "Trabzon", "Tunceli", "Usak", "Van", "Yalova", "Yozgat", "Zonguldak"
    ],
    "Canada": [
        "Alberta", "British Columbia", "Manitoba", "New Brunswick",
        "Newfoundland and Labrador", "Nova Scotia", "Ontario",
        "Prince Edward Island", "Quebec", "Saskatchewan"
    ],
    "Australia": [
        "New South Wales", "Victoria", "Queensland", "Western Australia",
        "South Australia", "Tasmania", "Northern Territory", "Australian Capital Territory"
    ],
    "India": [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
        "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
        "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
        "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
        "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
        "Uttar Pradesh", "Uttarakhand", "West Bengal"
    ],
    "Nigeria": [
        "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa",
        "Benue", "Borno", "Cross River", "Delta", "Ebonyi", "Edo",
        "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano",
        "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa",
        "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau",
        "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara", "Federal Capital Territory"
    ],
    "Mexico": [
        "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua",
        "Coahuila", "Colima", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Mexico City", "Mexico State",
        "Michoacán", "Morelos", "Nayarit", "Nuevo Leon", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí",
        "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatan", "Zacatecas"
    ],
    "Brazil": [
        "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso",
        "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte",
        "Rio Grande do Sul", "Rondônia", "Roraima", "São Paulo", "Santa Catarina", "Sergipe", "Distrito Federal"
    ],
    "China": [
        "Anhui", "Beijing", "Chongqing", "Fujian", "Gansu", "Guangdong", "Guangxi", "Guizhou", "Hainan", "Hebei",
        "Heilongjiang", "Henan", "Hubei", "Hunan", "Jiangsu", "Jiangxi", "Jilin", "Liaoning", "Macau", "Ningxia",
        "Qinghai", "Shaanxi", "Shandong", "Shanghai", "Shanxi", "Sichuan", "Tianjin", "Tibet", "Xinjiang", "Yunnan", "Zhejiang"
    ],
    "Russia": [
        "Adygea", "Altai Republic", "Amur", "Arkhangelsk", "Astrakhan", "Bashkortostan", "Belgorod", "Bryansk", "Buryatia",
        "Chechen Republic", "Chelyabinsk", "Chita", "Chukotka", "Dagestan", "Ingushetia", "Irkutsk", "Ivanovo", "Jewish Autonomous",
        "Kabardino-Balkaria", "Kaliningrad", "Kaluga", "Kamchatka", "Kemerovo", "Khabarovsk", "Khakassia", "Kirov", "Komi", "Kostroma",
        "Krasnodar", "Krasnoyarsk", "Kurgan", "Kursk", "Leningrad", "Lipetsk", "Magadan", "Mari El", "Mordovia", "Moscow", "Murmansk",
        "Nenets", "Nizhny Novgorod", "North Ossetia", "Orel", "Orenburg", "Penza", "Perm", "Primorsky", "Pskov", "Rostov", "Ryazan",
        "Sakhalin", "Samara", "Saratov", "Smolensk", "Stavropol", "Sverdlovsk", "Tambov", "Tatarstan", "Tver", "Tomsk", "Tula", "Tver",
        "Udmurt", "Ulyanovsk", "Vladimir", "Volgograd", "Vologda", "Voronezh", "Yamalo-Nenets", "Yaroslavl"
    ],
    "United Kingdom": [
        "England", "Scotland", "Wales", "Northern Ireland"
    ],
    "France": [
        "Île-de-France", "Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Brittany", "Centre-Val de Loire", "Corsica",
        "Grand Est", "Hauts-de-France", "Normandy", "Nouvelle-Aquitaine", "Occitania", "Pays de la Loire", "Provence-Alpes-Côte d'Azur"
    ],
    "Germany": [
        "Baden-Württemberg", "Bavaria", "Berlin", "Brandenburg", "Bremen", "Hamburg", "Hesse", "Lower Saxony", "Mecklenburg-Vorpommern",
        "North Rhine-Westphalia", "Rhineland-Palatinate", "Saarland", "Saxony", "Saxony-Anhalt", "Schleswig-Holstein", "Thuringia"
    ],
    "South Africa": [
        "Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "North West", "Northern Cape", "Western Cape"
    ]
}


# Database model for user registration data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    state_of_origin = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(50), nullable=True)
    company = db.Column(db.String(100), nullable=True)
    area_of_expertise = db.Column(db.String(100), nullable=True)
    picture_path = db.Column(db.String(100), nullable=True)
    video_path = db.Column(db.String(100), nullable=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    countries = list(countries_and_states.keys())
    return render_template('register.html', countries=countries, states=countries_and_states)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        state_of_origin = request.form.get('state_of_origin')
        country = request.form.get('country')
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        title = request.form.get('title')
        company = request.form.get('company')
        area_of_expertise = request.form.get('area_of_expertise')

        picture = request.files.get('picture')
        video = request.files.get('video')

        picture_path = None
        video_path = None

        if picture:
            picture_filename = secure_filename(picture.filename)
            picture_path = picture_filename
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_filename))

        if video:
            video_filename = secure_filename(video.filename)
            video_path = video_filename
            video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))

        new_user = User(
            fullname=fullname,
            state_of_origin=state_of_origin,
            country=country,
            gender=gender,
            dob=dob,
            title=title,
            company=company,
            area_of_expertise=area_of_expertise,
            picture_path=picture_path,
            video_path=video_path
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!')
        return redirect(url_for('register'))

    countries = list(countries_and_states.keys())
    return render_template('register.html', countries=countries, states=countries_and_states)

@app.route('/admin_login', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials, please try again.')
            return redirect(url_for('admin'))

    return render_template('admin_login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        flash('Please log in to access the admin dashboard.')
        return redirect(url_for('admin'))

    users = User.query.all()
    return render_template('admin.html', users=users)

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully.')
    return redirect(url_for('admin'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)


# import pycountry
# import geonamescache
# from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
# from werkzeug.utils import secure_filename
# from flask_sqlalchemy import SQLAlchemy
# import os
#
# # Initialize Flask app
# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace with a strong secret key
# app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# # Create the upload folder if it doesn't exist
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
#
# # Admin credentials
# ADMIN_USERNAME = "Okechukwu"
# ADMIN_PASSWORD = "Ebube"
#
# # Initialize geonamescache
# gc = geonamescache.GeonamesCache()
#
# # Database model for user registration data
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fullname = db.Column(db.String(100), nullable=False)
#     state_of_origin = db.Column(db.String(50), nullable=False)
#     country = db.Column(db.String(50), nullable=False)
#     gender = db.Column(db.String(10), nullable=False)
#     dob = db.Column(db.String(20), nullable=False)
#     title = db.Column(db.String(50), nullable=True)
#     company = db.Column(db.String(100), nullable=True)
#     area_of_expertise = db.Column(db.String(100), nullable=True)
#     picture_path = db.Column(db.String(100), nullable=True)
#     video_path = db.Column(db.String(100), nullable=True)
#
# # Initialize the database
# with app.app_context():
#     db.create_all()
#
# def get_countries_and_states():
#     # Retrieve the countries from pycountry
#     countries = list(pycountry.countries)
#     country_states = {}
#
#     # Retrieve the states/provinces for each country using Geonamescache
#     for country in countries:
#         country_code = country.alpha_2.lower()
#         try:
#             states = gc.get_states_by_country(country_code)
#             country_states[country.name] = [state['name'] for state in states]
#         except KeyError:
#             country_states[country.name] = []
#     return country_states
#
# @app.route('/')
# def index():
#     countries_and_states = get_countries_and_states()
#     return render_template('register.html', countries_and_states=countries_and_states)
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         fullname = request.form.get('fullname')
#         state_of_origin = request.form.get('state_of_origin')
#         country = request.form.get('country')
#         gender = request.form.get('gender')
#         dob = request.form.get('dob')
#         title = request.form.get('title')
#         company = request.form.get('company')
#         area_of_expertise = request.form.get('area_of_expertise')
#
#         picture = request.files.get('picture')
#         video = request.files.get('video')
#
#         picture_path = None
#         video_path = None
#
#         if picture:
#             picture_filename = secure_filename(picture.filename)
#             picture_path = picture_filename
#             picture.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_filename))
#
#         if video:
#             video_filename = secure_filename(video.filename)
#             video_path = video_filename
#             video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))
#
#         new_user = User(
#             fullname=fullname,
#             state_of_origin=state_of_origin,
#             country=country,
#             gender=gender,
#             dob=dob,
#             title=title,
#             company=company,
#             area_of_expertise=area_of_expertise,
#             picture_path=picture_path,
#             video_path=video_path
#         )
#         db.session.add(new_user)
#         db.session.commit()
#
#         flash('Registration successful!')
#         return redirect(url_for('register'))
#
#     countries_and_states = get_countries_and_states()
#     return render_template('register.html', countries_and_states=countries_and_states)
#
# @app.route('/admin_login', methods=['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#
#         if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#             session['admin_logged_in'] = True
#             return redirect(url_for('admin_dashboard'))
#         else:
#             flash('Invalid credentials, please try again.')
#             return redirect(url_for('admin'))
#
#     return render_template('admin_login.html')
#
# @app.route('/admin_dashboard')
# def admin_dashboard():
#     if not session.get('admin_logged_in'):
#         flash('Please log in to access the admin dashboard.')
#         return redirect(url_for('admin'))
#
#     users = User.query.all()
#     return render_template('admin.html', users=users)
#
# @app.route('/logout')
# def logout():
#     session.pop('admin_logged_in', None)
#     flash('Logged out successfully.')
#     return redirect(url_for('admin'))
#
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
#
# if __name__ == '__main__':
#     app.run(debug=True)