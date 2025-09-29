software_development = {
    '前端工程師': ['JavaScript', 'CSS', 'HTML', 'Git', 'Vue'],
    '全端工程師': ['JavaScript', 'Git', 'C#', 'CSS', 'HTML'],
    '韌體工程師': ['C 語言', 'C++', 'Linux', 'Python', 'MCU'],
    '演算法工程師': ['Python', 'C++', 'C 語言', 'Linux', 'C#'],
    'MES 工程師': ['C#', 'MS SQL', 'MES', 'Oracle Database', 'C 語言'],
    'AI 工程師': ['Python', 'C++', 'C 語言', 'PyTorch', 'Linux']
}

system = {
    '系統工程師': ['Linux', 'Excel', 'VMware', 'Python', 'C 語言'],
    'MIS 工程師': ['C#', 'MS SQL', 'JavaScript', 'ASP.NET', 'Java'],
    '資安工程師': ['Linux', 'Firewall', 'ISO', "VMware", 'TCP/IP'],
    '資料庫管理師': ['MS SQL', 'Linux', 'Oracle Database', 'SQL', 'MySQL'],
    'MIS／網管主管': ['Linux', 'Firewall', 'VMware', 'DNS', 'TCP/IP']
}

analysis = {
    '數據分析師': ['Python', 'Excel', 'Tableau', 'SQL', 'MS SQL'],
    '資料工程師': ['Python', 'MS SQL', 'SQL', 'Linux', 'MySQL'],
    '系統分析師': ['MS SQL', 'Java', 'C#', 'Python', 'JavaScript']
}

management = {
    '軟體專案主管': ['Java', 'C#', 'Python', 'C 語言', 'Linux']
}

job_skill = software_development | system | analysis | management
