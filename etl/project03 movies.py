import pandas as pd

# Đọc dữ liệu
try:
    data = pd.read_csv('/home/long/PycharmProject/Project03/Database/tmdb-movies.csv')
except Exception as e:
    print(f"Lỗi khi đọc dữ : {e}")

# Chuyển đổi và chỉnh sửa cột 'release_date'
try:
    data['release_date'] = pd.to_datetime(data['release_date'], format='%m/%d/%y')
    data['release_date'] = data['release_date'].apply(lambda date: date.replace(year=date.year - 100) if date.year > 2024 else date)
except Exception as e:
    print(f"Phát hiện lỗi 'release_date': {e}")

# Task 1: Sắp xếp theo ngày phát hành
try:
    sorted_data = data.sort_values(by='release_date', ascending=False)
    sorted_data.to_csv('/home/long/PycharmProject/Project03/export/Project03-Task 1.csv')
    print("Task 1: Đã xuất thành công.")
except Exception as e:
    print(f"Lỗi Task 1: {e}")

# Task 2: Lọc phim có đánh giá trên 7.5
try:
    rating_movie = data[data['vote_average'] >= 7.5]
    rating_movie.to_csv('/home/long/PycharmProject/Project03/export/Project03-Task 2.csv')
    print("Task 2: Đã xuất thành công.")
except Exception as e:
    print(f"Lỗi Task 2: {e}")

# Task 3: Tìm phim có revenue cao nhất và thấp nhất khác 0
try:
    data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce')
    max_revenue_movie = data.loc[data['revenue'].idxmax()]
    filterdata = data[data['revenue'] > 0]
    min_revenue_movie = filterdata.loc[filterdata['revenue'].idxmin()]
    print("Task 3: Phim có doanh thu cao nhất:", max_revenue_movie['original_title'], max_revenue_movie['revenue'])
    print("Task 3: Phim có doanh thu thấp nhất khác 0:", min_revenue_movie['original_title'], min_revenue_movie['revenue'])
except Exception as e:
    print(f"Lỗi Task 3: {e}")

# Task 4: Tính tổng doanh thu tất cả phim
try:
    total_revenue = data['revenue'].sum()
    print(f"Task 4: Tổng doanh thu các phim = {total_revenue}")
except Exception as e:
    print(f"Lỗi Task 4: {e}")

# Task 5: Top 10 bộ phim lợi nhuận cao nhất
try:
    data['profit'] = data['revenue'] - data['budget']
    top_10_profitable = data.sort_values(by='profit', ascending=False).head(10)
    print("Task 5: Top 10 bộ phim có lợi nhuận cao nhất:")
    print(top_10_profitable[['original_title', 'profit']])
except Exception as e:
    print(f"Lỗi Task 5: {e}")

# Task 6: Đạo diễn và diễn viên có nhiều phim nhất
try:
    director_counts = data['director'].astype(str).value_counts()
    actor_counts = data['cast'].astype(str).str.split('|').explode().value_counts()
    mvp_director  = director_counts.idxmax()
    mvp_cast  = actor_counts.idxmax()
    print(f"Task 6:")
    print(f"Đạo diễn có nhiều bộ phim nhất: {mvp_director} ({director_counts.max()})")
    print(f"Diễn viên có nhiều phim nhất: {mvp_cast} ({actor_counts.max()})")
except Exception as e:
    print(f"Lỗi Task 6: {e}")

# Task 7: Thôngs kê số lượng phim theo từng thể
try:
    list_theloai = data['genres'].str.split('|').explode()
    dem_theloai = list_theloai.value_counts()
    print("Task 7: Thống kê số lượng phim theo từng thể lọai:")
    print(dem_theloai)
except Exception as e:
    print(f"Lỗi Task 7: {e}")s
