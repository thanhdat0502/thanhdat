bài 1:
- Khái niệm ngôn ngữ thông dịch: là loại ngôn ngữ lập trình mà mã nguồn được thực thi trực tiếp từng dòng một bởi một chương trình gọi là trình thông dịch — không cần biên dịch toàn bộ mã nguồn thành mã máy trước khi chạy.
- Khái niệm ngôn biên dịch: là ngôn ngữ lập trình mà mã nguồn phải được chuyển đổi toàn bộ sang mã máy (thường là file .exe, .out,...) trước khi chương trình được thực thi, thông qua một chương trình gọi là trình biên dịch (compiler).
- Trong Python, khi bạn viết một chương trình và chạy nó (ví dụ: python tenfile.py), trình thông dịch Python sẽ thực hiện các bước sau:
    Chuyển mã nguồn .py sang bytecode (định dạng trung gian, file .pyc).

    Thực thi bytecode đó bằng Python Virtual Machine (PVM) – một phần của trình thông dịch.

Mặc dù có một bước biên dịch sang bytecode, nhưng bước này là ẩn, không phải biên dịch như các ngôn ngữ như C/C++ (tạo ra file máy .exe).
=> Do đó, Python vẫn được xem là ngôn ngữ thông dịch.