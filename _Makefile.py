import os

# HTML khởi tạo cơ bản
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson {}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    {}
    {}
</head>
<body class="bg-gray-50 p-8">
    <header class="text-center mb-8">
        <h1 class="text-3xl font-bold text-blue-700">Chào mừng đến với Lesson {}</h1>
        <p class="text-gray-600">Đây là trang khởi tạo cho bài học</p>
    </header>
    <main class="max-w-3xl mx-auto">
        <p>Bắt đầu chỉnh sửa nội dung tại đây!</p>
    </main>
</body>
</html>
"""

# CSS mẫu
CSS_TEMPLATE = """body {
    font-family: Arial, sans-serif;
}
"""

# JS mẫu
JS_TEMPLATE = """console.log("Chào mừng đến với Lesson {}!");
"""

# Nhập số bắt đầu và kết thúc từ người dùng
start = int(input("Nhập số bắt đầu của Lession (ví dụ: 1): "))
end = int(input("Nhập số kết thúc của Lession (ví dụ: 13): "))
create_css = input("Tạo thư mục và tệp CSS? (y/n): ").lower() == 'y'
create_js = input("Tạo thư mục và tệp JS? (y/n): ").lower() == 'y'

# Tạo các thư mục và tệp
for i in range(start, end + 1):
    lesson_dir = f"Lession {i}"
    
    # Tạo thư mục Lesson_X nếu chưa tồn tại
    if not os.path.exists(lesson_dir):
        os.makedirs(lesson_dir)
    
    # Tạo link đến CSS và JS nếu người dùng yêu cầu
    css_link = '<link rel="stylesheet" href="css/style.css">' if create_css else ''
    js_link = '<script src="js/script.js"></script>' if create_js else ''
    
    # Tạo tệp index.html
    with open(os.path.join(lesson_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(i, css_link, js_link, i))
    
    # Tạo thư mục css và tệp style.css nếu được chọn
    if create_css:
        css_dir = os.path.join(lesson_dir, "css")
        if not os.path.exists(css_dir):
            os.makedirs(css_dir)
        with open(os.path.join(css_dir, "style.css"), "w", encoding="utf-8") as f:
            f.write(CSS_TEMPLATE)
    
    # Tạo thư mục js và tệp script.js nếu được chọn
    if create_js:
        js_dir = os.path.join(lesson_dir, "js")
        if not os.path.exists(js_dir):
            os.makedirs(js_dir)
        with open(os.path.join(js_dir, "script.js"), "w", encoding="utf-8") as f:
            f.write(JS_TEMPLATE.format(i))

print(f"Đã tạo các thư mục và tệp từ Lesson {start} đến Lesson {end}.")
if create_css:
    print("Đã tạo thư mục css và tệp style.css trong mỗi Lesson.")
if create_js:
    print("Đã tạo thư mục js và tệp script.js trong mỗi Lesson.")