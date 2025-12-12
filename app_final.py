import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS file
load_css('style.css')

# Load data
@st.cache_data
def load_data():
    students_df = pd.read_csv('students.csv')
    academic_df = pd.read_csv('academic_performance.csv')
    faculty_df = pd.read_csv('faculty.csv')
    return students_df, academic_df, faculty_df

students_df, academic_df, faculty_df = load_data()

# Set page config
st.set_page_config(
    page_title="Dashboard Universitas",
    page_icon="🎓",
    layout="wide"
)

# Header
st.title("🎓 Dashboard Analitik Universitas")
st.markdown("---")

# Sidebar for filters
st.sidebar.header("🔍 Filter Data")

# Filter by year
year_range = st.sidebar.slider(
    'Pilih Rentang Tahun',
    int(students_df['year_enrolled'].min()),
    int(students_df['year_enrolled'].max()),
    (int(students_df['year_enrolled'].min()), int(students_df['year_enrolled'].max()))
)

# Filter by faculty
faculties = sorted(students_df['faculty'].unique())
selected_faculties = st.sidebar.multiselect(
    'Pilih Fakultas',
    faculties,
    default=faculties
)

# Filter by gender
genders = sorted(students_df['gender'].unique())
selected_gender = st.sidebar.selectbox(
    'Pilih Jenis Kelamin',
    ['Semua Jenis Kelamin'] + genders,
    index=0
)

# Apply filters
if selected_faculties:
    faculty_filter = students_df['faculty'].isin(selected_faculties)
else:
    faculty_filter = students_df['faculty'].isin(faculties)

if selected_gender == 'Semua Jenis Kelamin':
    gender_filter = students_df['gender'].isin(genders)
else:
    gender_filter = students_df['gender'] == selected_gender

filtered_students = students_df[
    (students_df['year_enrolled'] >= year_range[0]) &
    (students_df['year_enrolled'] <= year_range[1]) &
    faculty_filter &
    gender_filter
]

# KPI Metrics
st.subheader("📊 Ringkasan Data")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Mahasiswa", 
        value=len(filtered_students),
        delta=len(filtered_students)-len(students_df)+len(filtered_students)
    )

with col2:
    avg_gpa = filtered_students['gpa'].mean()
    st.metric(
        label="IPK Rata-rata", 
        value=f"{avg_gpa:.2f}",
        delta=round(avg_gpa - students_df['gpa'].mean(), 2)
    )

with col3:
    unique_faculties = len(filtered_students['faculty'].unique())
    st.metric(
        label="Jumlah Fakultas", 
        value=unique_faculties,
        delta=0
    )

with col4:
    active_students = len(filtered_students[filtered_students['status'] == 'Active'])
    st.metric(
        label="Mahasiswa Aktif", 
        value=active_students,
        delta=round(active_students * 0.05)
    )

# Charts using Streamlit's built-in chart functions
st.markdown("---")
st.subheader("📈 Visualisasi Data (Distribusi dan Tren Mahasiswa)")

col1, col2 = st.columns(2)

with col1:
    st.write("**Distribusi Mahasiswa per Fakultas**")
    faculty_counts = filtered_students['faculty'].value_counts()
    
    import plotly.graph_objects as go
    
    # Buat bar chart dengan Plotly (warna biru & background hitam)
    fig = go.Figure(data=[
        go.Bar(
            x=faculty_counts.index,
            y=faculty_counts.values,
            text=faculty_counts.values,  # Nilai di dalam bar
            textposition='inside',  # Posisi text di dalam bar
            textfont=dict(size=12, color='white', family='Arial'),
            marker=dict(
                color='#60a5fa',  
            ),
            hovertemplate='<b>%{x}</b><br>Jumlah Mahasiswa: %{y}<extra></extra>',  # Tooltip saat hover
            hoverlabel=dict(
                bgcolor='#1e3a8a',
                font_size=13,
                font_family='Arial',
                font_color='white',
                bordercolor='#60a5fa'
            )
        )
    ])
    fig.update_layout(
        margin=dict(l=40, r=20, t=20, b=80),  
        height=350  
    )
    st.plotly_chart(fig, use_container_width=True)


with col2:
    st.write("**Tren Jumlah Mahasiswa per Tahun**")
    yearly_counts = filtered_students.groupby('year_enrolled').size().reset_index(name='count')
    
    # Konversi tahun ke string agar tidak pakai koma
    yearly_counts['year_enrolled'] = yearly_counts['year_enrolled'].astype(str)
    
    yearly_chart = pd.DataFrame(yearly_counts.set_index('year_enrolled')['count'])
    st.line_chart(yearly_chart)

# Additional visualizations
st.markdown("---")
st.subheader("📈  Visualisasi Data (Status, IPK, dan Distribusi Gender Mahasiswa)")

# Create tabs for different analysis views
tab1, tab2, tab3 = st.tabs(["📊 Status Mahasiswa", "🎓 IPK per Fakultas", "👥 Distribusi Gender"])

# Palette warna soft & modern
colors_palette = ['#60a5fa', '#34d399', '#fbbf24', '#f87171', '#a78bfa', '#f472b6']

with tab1:
    st.write("**Distribusi Status Mahasiswa**")
    status_counts = filtered_students['status'].value_counts()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        fig, ax = plt.subplots(figsize=(6, 6))
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        
        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct*total/100.0))
                return f'{pct:.1f}%\n({val})'
            return my_autopct
        
        wedges, texts, autotexts = ax.pie(
            status_counts.values, 
            labels=status_counts.index, 
            autopct=make_autopct(status_counts.values), 
            startangle=90, 
            colors=colors_palette[:len(status_counts)],
            textprops={'fontsize': 10, 'weight': 'bold'},
            explode=[0.05] * len(status_counts)
        )
        
        # Styling untuk label
        for text in texts:
            text.set_color('#1e3a8a')
            text.set_fontsize(11)
            text.set_weight('bold')
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_weight('bold')
        
        ax.axis('equal')
        st.pyplot(fig)


with tab2:
    st.write("**Perbandingan IPK Rata-rata per Fakultas**")
    
    # Hitung IPK rata-rata dan jumlah mahasiswa per fakultas
    faculty_gpa = filtered_students.groupby('faculty')['gpa'].mean().sort_values(ascending=False)
    faculty_count = filtered_students.groupby('faculty').size()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        
        # Buat horizontal bar chart untuk IPK
        bars = ax.barh(
            faculty_gpa.index, 
            faculty_gpa.values,
            color=colors_palette[:len(faculty_gpa)],
            edgecolor='#1e3a8a',
            linewidth=1.5,
            height=0.6
        )
        
        # Tambahkan label IPK dan jumlah mahasiswa di ujung bar
        for i, (faculty, gpa) in enumerate(faculty_gpa.items()):
            count = faculty_count[faculty]
            ax.text(
                gpa + 0.05, i, 
                f'{gpa:.2f} ({count} mhs)', 
                va='center', 
                fontweight='bold', 
                color='#1e3a8a',
                fontsize=10
            )
        
        ax.set_xlabel('IPK Rata-rata', fontsize=12, color='#1e3a8a', fontweight='bold')
        ax.set_ylabel('Fakultas', fontsize=12, color='#1e3a8a', fontweight='bold')
        ax.set_xlim(0, 4.2)  # IPK maksimal 4.0 + space untuk label
        ax.tick_params(axis='both', colors='#334155')
        ax.grid(axis='x', alpha=0.3, linestyle='--', color='#bfdbfe')
        ax.set_axisbelow(True)
        
        plt.tight_layout()
        st.pyplot(fig)



with tab3:
    st.write("**Distribusi Gender Mahasiswa**")
    gender_counts = filtered_students['gender'].value_counts()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        fig, ax = plt.subplots(figsize=(6, 6))
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        
        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct*total/100.0))
                return f'{pct:.1f}%\n({val})'
            return my_autopct
        
        wedges, texts, autotexts = ax.pie(
            gender_counts.values, 
            labels=gender_counts.index, 
            autopct=make_autopct(gender_counts.values), 
            startangle=90, 
            colors=colors_palette[:len(gender_counts)],
            textprops={'fontsize': 10, 'weight': 'bold'},
            explode=[0.05] * len(gender_counts)
        )
        
        # Styling untuk label
        for text in texts:
            text.set_color('#1e3a8a')
            text.set_fontsize(11)
            text.set_weight('bold')
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_weight('bold')
        
        ax.axis('equal')
        st.pyplot(fig)

# Detailed Data Section
st.markdown("---")
st.subheader("📋 Data Mahasiswa")

# Apply search filter
filtered_data = filtered_students.copy()

# Tampilkan data dengan scrolling
if len(filtered_data) > 0:
    st.dataframe(
        filtered_data, 
        use_container_width=True,
        hide_index=True,
        height=500  # Tinggi fixed dengan scrolling otomatis
    )
    
    # Download button
    col1, col2, col3 = st.columns([2, 2, 2])
    with col2:
        csv = filtered_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Data (CSV)",
            data=csv,
            file_name=f'data_mahasiswa_{pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")}.csv',
            mime='text/csv',
            use_container_width=True
        )

# Summary statistics
st.markdown("---")
st.subheader("📈 Statistik dan TOP Program Studi")

summary_stats = pd.DataFrame({
    'Statistik': ['Jumlah Total', 'IPK Rata-rata', 'IPK Tertinggi', 'IPK Terendah', 'Rata-rata Umur'],
    'Nilai': [
        f"{len(filtered_students):,}",
        f"{filtered_students['gpa'].mean():.2f}",
        f"{filtered_students['gpa'].max():.2f}",
        f"{filtered_students['gpa'].min():.2f}",
        f"{filtered_students['age'].mean():.1f}"
    ]
})

col1, col2 = st.columns(2)
with col1:
    st.write("**Statistik Umum**")
    # Konversi ke HTML tanpa index
    st.markdown(summary_stats.to_html(index=False), unsafe_allow_html=True)



with col2:
    st.write("**Distribusi Program Studi (Top 5)**")
    top_majors = filtered_students['major'].value_counts().head(5)
    
    import plotly.graph_objects as go
    
    # Buat bar chart dengan Plotly
    fig = go.Figure(data=[
        go.Bar(
            x=top_majors.index,
            y=top_majors.values,
            text=top_majors.values,  # Nilai di dalam bar
            textposition='inside',
            textfont=dict(
                size=12,
                color='white',
                family='Arial'
            ),
            marker=dict(
                color='#60a5fa',  # Biru terang
            ),
            hovertemplate='<b>%{x}</b><br>Jumlah: %{y} mahasiswa<extra></extra>',
            hoverlabel=dict(
                bgcolor='#1e3a8a',
                font_size=14,
                font_family='Arial',
                font_color='white',
                bordercolor='#60a5fa'
            )
        )
    ])
    fig.update_layout(
        margin=dict(l=40, r=20, t=20, b=80),  
        height=350  
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<p class='caption'>Dashboard Analitik Universitas | Dibuat dengan menggunakan Streamlit</p>", unsafe_allow_html=True)
