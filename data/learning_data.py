from urllib.parse import quote

learning_paths = {
    "Python": [
        {
            "name": "基礎語法\nBasic Syntax、Variables、Conditionals、\nLoops、Type Casting",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "基礎語法\nExceptions、Function、Lists、\nTuples、Sets、Dict",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "模組與套件\nLibrary、Modules、PyPI、Pip、\nConda、Packages",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "物件導向程式設計\nClasses、Methods、Inheritance",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "資料結構與演算法\nArrays、Linked Lists、Hash Tables、\nHeaps、Stacks、Queues、\nSorting Algorithms",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "函式與進階概念\nLambda、Decorators、Iterators、\nRegular Expressions",
            'level': "Intermediate",
            "duration": "3個月"
        },
        {
            "name": "進階套件管理\nPoetry、Configuration、pyproject.toml、\nList Comprehensions、\nParadigms、Context Manager、uv",
            'level': "Intermediate",
            "duration": "3個月"},
        {
            "name": "框架\nSynchronous、Asynchronous、\nPlotly Dash、Pyramid、gevent、\naiohttp、FastAPI、Django、Flask",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "Concurrency\nThreading、Multiprocessing、Asynchrony、GIL",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "Environments\nPipenv、virtualenv、pyenv",
            "level": "Advanced",
            "duration": "3個月"
        },
        {
            "name": "Static Typing\ntyping、mypy、pyright、\npyre、Static Typing",
            "level": "Advanced",
            "duration": "3個月"
        },
        {
            "name": "Code Formatting\nyapf、black、ruff",
            "level": "Expert",
            "duration": "3個月+"
        },
        {
            "name": "Documentation Generation and Testing Tools\nSphinx、tox、nose、pyUnit、doctest、pytest",
            "level": "Expert",
            "duration": "3個月+"
        }
    ],
    "JavaScript": [
        {
            "name": "JavaScript基礎\n語法、變數、資料型別",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "流程控制與迴圈\n條件判斷、迴圈語法",
            "level": "Beginner",
            "duration": "1.5個月"
        },
        {
            "name": "函數與閉包\n參數、箭頭函數、閉包",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "物件與原型\n物件導向、類別、原型繼承",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "非同步程式設計\nEvent Loop、Promise、Async/Await",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "模組化與API整合\nESM、CommonJS、Fetch API",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "記憶體管理\n垃圾回收、效能優化",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "除錯與最佳化\nDevTools、記憶體/效能問題",
            "level": "Expert",
            "duration": "2個月"
        }
    ],
    "C++": [
        {
            "name": "語言基礎\n安裝、編譯環境、基本運算與資料型別",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "流程控制與函式\n控制敘述、函式、多載與運算子重載",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "指標與記憶體管理\n指標、引用、智能指標、物件生命週期",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "程式碼組織\n前置宣告、命名空間、程式碼結構化",
            "level": "Beginner",
            "duration": "1.5個月"
        },
        {
            "name": "物件導向程式設計\n類別、繼承、多型、迭代器",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "語言進階概念\n型別轉換、自動推導、未定義行為",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "標準函式庫與STL\n容器、演算法、迭代器、多執行緒",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "樣板與特化\n模板、SFINAE、可變參數模板",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "例外處理與編譯器\n例外機制、退出碼、主流編譯器",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "C++標準與慣用法\nC++11/14/17/20、常見設計慣用法",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "語言工具與建置系統\n除錯工具、CMake、Makefile、Ninja",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "套件與函式庫\n套件管理工具、Boost、OpenCV 等",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "框架與應用\nOrbit Profiler、PyTorch C++",
            "level": "Expert",
            "duration": "2個月"
        }
    ],
    "Linux": [
        {
            "name": "導覽與檔案操作\n基本指令、檔案/目錄操作、Vim/Nano 編輯",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "Shell 與基礎操作\n指令路徑、環境變數、重新導向、超級使用者",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "檔案管理與壓縮\n檔案權限、壓縮歸檔、連結檔",
            "level": "Beginner",
            "duration": "1.5個月"
        },
        {
            "name": "文字處理工具\n管線、grep、awk、sort、head/tail 等",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "程序管理\n前景/背景、訊號、優先級、分叉",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "使用者與群組管理\n建立/刪除/更新、權限設定",
            "level": "Intermediate",
            "duration": "1.5個月"
        },
        {
            "name": "伺服器監控\n系統負載、日誌、服務與資源檢查",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "服務管理 (systemd)\n建立/啟動/停止/檢查服務",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "磁碟與檔案系統\ninode、掛載、LVM、Swap",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "Linux 開機流程\n日誌、Boot Loader",
            "level": "Intermediate",
            "duration": "1.5個月"
        },
        {
            "name": "套件管理\n套件庫、安裝/移除/升級、Snap",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "網路管理\nTCP/IP、路由、DNS、SSH、檔案傳輸",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "Shell 程式設計\n變數、迴圈、條件判斷、除錯",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "系統疑難排解\nping、traceroute、cgroups、\nnetstat、封包分析",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "容器化技術\nDocker、容器執行環境",
            "level": "Advanced",
            "duration": "2個月"
        }
    ],
    "Java": [
        {
            "name": "語言基礎\n基本語法、程式生命週期、資料型態、變數與作用域、型態轉換",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "字串、數學運算與方法\n字串操作、數學運算、方法設計",
            "level": "Beginner",
            "duration": "1.5個月"
        },
        {
            "name": "陣列、條件與迴圈\n陣列、條件判斷、迴圈控制",
            "level": "Beginner",
            "duration": "2個月"
        },
        {
            "name": "物件導向程式設計基礎\nOOP 基本觀念",
            "level": "Beginner",
            "duration": "1.5個月"
        },
        {
            "name": "物件導向程式設計進階\n物件生命週期、繼承、抽象、介面、封裝、模組與套件",
            "level": "Intermediate",
            "duration": "2.5個月"
        },
        {
            "name": "例外處理\n例外機制與應用",
            "level": "Intermediate",
            "duration": "1個月"
        },
        {
            "name": "集合框架\nList、Set、Map、Queue、Stack、迭代器、泛型集合",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "多執行緒與並行\nThreads、虛擬執行緒、volatile",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "I/O 與檔案操作\n輸入輸出、檔案存取",
            "level": "Intermediate",
            "duration": "1.5個月"
        },
        {
            "name": "其他應用\n正規表示式、日期時間、密碼學、網路、Java 記憶體模型",
            "level": "Intermediate",
            "duration": "2個月"
        },
        {
            "name": "函式式程式設計\n高階函式、函式介面、函式組合、Stream API",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "建置工具\nMaven、Gradle、Bazel",
            "level": "Advanced",
            "duration": "1.5個月"
        },
        {
            "name": "Web 框架\nSpring、Spring Boot、Quarkus、Javalin、Play",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "資料庫存取\nJDBC、ORM、Hibernate、Spring Data JPA",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "軟體測試\n單元測試、整合測試、行為測試、模擬",
            "level": "Advanced",
            "duration": "2個月"
        },
        {
            "name": "日誌框架\nLogback、Log4j2、SLF4J",
            "level": "Advanced",
            "duration": "1個月"
        }
    ]
}

learning_resources = {
    "Python": {
        "Beginner": [
            {
                "name": "Python Tutorials",
                "url": "第一階段"
            },
            {
                "name": "Python Tutorial for Beginners \n(For Absolute Beginners)",
                "url": "第一階段"
            },
            {
                "name": "Data Structures & Algorithms in Python\n - TheComplete Pathway",
                "url": "第二階段"
            },
            {
                "name": "Python 全民瘋AI系列 [經典機器學習]",
                "url": "第二階段"
            },
            {
                "name": "Python AI Projects",
                "url": "第三階段"
            },
            {
                "name": "Deep Learning Projects with Python and Keras",
                "url": "第三階段"
            },
            {
                "name": "Advanced Python Tutorial by DURGA Sir",
                "url": "第四階段"
            },
        ],
        "Intermediate": [
            {
                "name": "Python Tutorials",
                "url": "第一階段"
            },
            {
                "name": "Python Tutorial for Beginners \n(For Absolute Beginners)",
                "url": "第二階段"
            },
            {
                "name": "Data Structures & Algorithms in Python \n- The Complete Pathway",
                "url": "第三階段"
            },
            {
                "name": "Python 全民瘋AI系列 [經典機器學習]",
                "url": "第四階段"
            },
        ],
        "Advanced": [
            {
                "name": "Python Tutorials",
                "url": "第一階段"
            },
            {
                "name": "Python Tutorial for Beginners\n (For Absolute Beginners)",
                "url": "第二階段"
            },
            {
                "name": "Python 全民瘋AI系列 [經典機器學習]",
                "url": "第三階段"
            },
            {
                "name": "Deep Learning Projects with Python and Keras",
                "url": "第三階段"
            },
            {
                "name": "Machine Learning",
                "url": "第四階段"
            },
        ],
        "Expert": [
            {
                "name": "Python Tutorials",
                "url": "第一階段"
            },
            {
                "name": "Deep Learning Projects with Python and Keras",
                "url": "第二階段"
            },
            {
                "name": "Machine Learning",
                "url": "第三階段"
            },
            {
                "name": "Appium With Python",
                "url": "第四階段"
            },
        ]
    },
    "JavaScript": {
        "Beginner": [
            {
                "name": "The Complete JavaScript Course\n _ Zero to Advanced in 65 Hours",
                "url": "第一階段"
            },
            {
                "name": "【千锋】JavaScript从入门到精通\n（小白必看！）（139集）",
                "url": "第一階段"
            },
            {
                "name": "JavaScript 完整教學 \n#fullcourse #beginners #tutorial",
                "url": "第二階段"
            },
            {
                "name": "JavaScript 網頁前端工程進階教學",
                "url": "第二階段"
            },
            {
                "name": "Myanmar JavaScript Beginner",
                "url": "第三階段"
            },
            {
                "name": "【前端】JavaScript零基础轻松入门教程\n(JavaScript Tutorials For Beginners)",
                "url": "第三階段"
            },
            {
                "name": "Namaste JavaScript",
                "url": "第四階段"
            },
        ],
        "Intermediate": [
            {
                "name": "The Complete JavaScript Course\n _ Zero to Advanced in 65 Hours",
                "url": "第一階段"
            },
            {
                "name": "JavaScript 網頁前端工程進階教學",
                "url": "第二階段"
            },
            {
                "name": "javascript advanced The Complete JavaScript Course\n _ Zero to Advanced in 65 Hours",
                "url": "第三階段"
            },
            {
                "name": "Namaste JavaScript",
                "url": "第四階段"
            },
        ],
        "Advanced": [
            {
                "name": "The Complete JavaScript Course\n _ Zero to Advanced in 65 Hours",
                "url": "第一階段"
            },
            {
                "name": "JNamaste JavaScript",
                "url": "第二階段"
            },
        ],
        "Expert": [
            {
                "name": "Chai aur Javascript Backend _ Hindi",
                "url": "第一階段"
            }
        ]
    },
    "C++": {
        "Beginner": [
            {
                "name": "【尚硅谷】2023版C++零基础教程，c++项目实战，清华学神带你一套通关",
                "url": "第一階段"
            },
            {
                "name": "C++ - Projects",
                "url": "第一階段"
            },
            {
                "name": "C++ GUI applications \n(beginner to advanced)",
                "url": "第二階段"
            },
            {
                "name": "C語言線上課程教學 - 近代程式語言的基礎",
                "url": "第二階段"
            },
            {
                "name": "QT C++ GUI Tutorial For Beginners",
                "url": "第三階段"
            },
        ],
        "Intermediate": [
            {
                "name": "程式設計（C++）— 完整課程",
                "url": "第一階段"
            },
            {
                "name": "C++ - Projects",
                "url": "第二階段"
            },
            {
                "name": "QT C++ GUI Tutorial For Beginners",
                "url": "第三階段"
            },
        ],
        "Advanced": [
            {
                "name": "C++ - Projects",
                "url": "第一階段"
            },
            {
                "name": "QT C++ GUI Tutorial For Beginners",
                "url": "第二階段"
            },
        ],
        "Expert": [
            {
                "name": "C++ - Projects",
                "url": "第一階段"
            },
        ]
    },
    "Linux": {
        "Beginner": [
            {
                "name": "【尚硅谷】Linux+Shell教程 3天搞定Linux，1天搞定Shell",
                "url": "第一階段"
            },
            {
                "name": "Docker and Kubernetes Tutorial for Beginners",
                "url": "第一階段"
            },
            {
                "name": "Linux for Beginners",
                "url": "第二階段"
            },
            {
                "name": "Linux 核心設計",
                "url": "第二階段"
            },
            {
                "name": "Linux Essentials For Hackers",
                "url": "第三階段"
            },
            {
                "name": "Free Docker Fundamentals Course - just enough docker to do stuff",
                "url": "第三階段"
            },
            {
                "name": "Linux 教學計畫 - Unix Linux 作業系統實務",
                "url": "第四階段"
            },
        ],
        "Intermediate": [
            {
                "name": "Linux 核心設計",
                "url": "第一階段"
            },
            {
                "name": "Docker and Kubernetes Tutorial for Beginners",
                "url": "第一階段"
            },
            {
                "name": "Free Docker Fundamentals Course - just enough docker to do stuff",
                "url": "第三階段"
            },
            {
                "name": "Linux 教學計畫 - Unix Linux 作業系統實務",
                "url": "第二階段"
            },
            {
                "name": "【尚硅谷】Linux+Shell教程 3天搞定Linux，1天搞定Shell",
                "url": "第三階段"
            },
        ],
        "Advanced": [
            {
                "name": "Linux 核心設計",
                "url": "第一階段"
            },
        ],
        "Expert": [
            {
                "name": "Docker and Kubernetes Tutorial for Beginners",
                "url": "第一階段"
            },
        ]
    }
}

course_links = {
    'Python': {
        'Beginner': [
            f'Python 課程學習路徑 :\nPython Tutorials：\nhttps://skillflow-python-beginner.vercel.app/playlist.html?playlist={quote("Python Tutorials")}',
            f'2. Python Tutorial for Beginners (For Absolute Beginners)：\nhttps://skillflow-python-intermediate1.vercel.app/playlist.html?playlist={quote("Python Tutorial for Beginners (For Absolute Beginners)")}',
            f'3. Data Structures & Algorithms in Python - The Complete Pathway：\nhttps://skillflow-python-beginner.vercel.app/playlist.html?playlist={quote("Python Tutorial for Beginners (For Absolute Beginners)")}',
            f'4. Python 全民瘋AI系列 [經典機器學習]：\nhttps://skillflow-python-beginner.vercel.app/playlist.html?playlist={quote("Python 全民瘋AI系列 [經典機器學習]")}',
            f'5. Python AI Projects：\nhttps://skillflow-python-beginner.vercel.app/playlist.html?playlist={quote("Python AI Projects")}',
            f'6. Deep Learning Projects with Python and Keras：\nhttps://skillflow-python-beginner.vercel.app/playlist.html?playlist={quote("Deep Learning Projects with Python and Keras")}',
            f'7. Advanced Python Tutorial by DURGA Sir：\nhttps://skillflow-python-beginner.vercel.app/playlist.html?playlist={quote("Advanced Python Tutorial by DURGA Sir")}'
        ],
        'Intermediate': [
            f'Python 課程學習路徑 :\nPython Tutorials：\nhttps://skillflow-python-intermediate1.vercel.app/playlist.html?playlist={quote("Python Tutorials")}',
            f'2. Python Tutorial for Beginners (For Absolute Beginners)：\nhttps://skillflow-python-intermediate1.vercel.app/playlist.html?playlist={quote("Python Tutorial for Beginners (For Absolute Beginners)")}',
            f'3. Data Structures & Algorithms in Python - The Complete Pathway：\nhttps://skillflow-python-intermediate1.vercel.app/playlist.html?playlist={quote("Data Structures %26 Algorithms in Python - The Complete Pathway")}',
            f'4. Python 全民瘋AI系列 [經典機器學習]：\nhttps://skillflow-python-intermediate1.vercel.app/playlist.html?playlist={quote("Python 全民瘋AI系列 [經典機器學習]")}'
        ],
        'Advanced': [
            f'Python 課程學習路徑 :\n\n1. Python Tutorials：\nhttps://python3-nine.vercel.app/playlist.html?playlist={quote("Python Tutorials")}',
            f'2. Python Tutorial for Beginners (For Absolute Beginners)：\nhttps://python3-nine.vercel.app/playlist.html?playlist={quote("Python Tutorial for Beginners (For Absolute Beginners)")}',
            f'3. Python 全民瘋AI系列 [經典機器學習]：\nhttps://python3-nine.vercel.app/playlist.html?playlist={quote("Python 全民瘋AI系列 [經典機器學習]")}',
            f'4. Deep Learning Projects with Python and Keras：\nhttps://python3-nine.vercel.app/playlist.html?playlist={quote("Deep Learning Projects with Python and Keras")}',
            f'5. Machine Learning：\nhttps://python3-nine.vercel.app/playlist.html?playlist={quote("Machine Learning")}'
        ],
        'Expert': [
            f'Python 課程學習路徑 :\n\n1. Python Tutorials：\nhttps://skillflow-python-expert.vercel.app/playlist.html?playlist={quote("Python Tutorials")}',
            f'2. Deep Learning Projects with Python and Keras：\nhttps://skillflow-python-expert.vercel.app/playlist.html?playlist={quote("Deep Learning Projects with Python and Keras")}',
            f'3. Machine Learning：\n\nhttps://skillflow-python-expert.vercel.app/playlist.html?playlist={quote("Machine Learning")}',
            f'4. Appium With Python：\n\nhttps://skillflow-python-expert.vercel.app/playlist.html?playlist={quote("Appium With Python")}'
        ]
    },
    'JavaScript': {
        'Beginner': [
            f'JavaScript 課程學習路徑 :\n\n1. The Complete JavaScript Course _ Zero to Advanced in 65 Hours：\nhttps://skillflow-javascript-beginner.vercel.app/playlist.html?playlist={quote("The Complete JavaScript Course _ Zero to Advanced in 65 Hours")}',
            f'2. 【千锋】JavaScript从入门到精通（小白必看！）（139集）：\nhttps://skillflow-javascript-beginner.vercel.app/playlist.html?playlist={quote("【千锋】JavaScript从入门到精通（小白必看！）（139集）")}',
            f'3. JavaScript 完整教學 #fullcourse #beginners #tutorial：\nhttps://skillflow-javascript-beginner.vercel.app/playlist.html?playlist={quote("JavaScript 完整教學 %23fullcourse %23beginners %23tutorial")}',
            f'4. JavaScript 網頁前端工程進階教學：\nhttps://skillflow-javascript-beginner.vercel.app/playlist.html?playlist={quote("JavaScript 網頁前端工程進階教學")}',
            f'5. Myanmar JavaScript Beginner：\nhttps://skillflow-javascript-beginner.vercel.app/playlist.html?playlist={quote("Myanmar JavaScript Beginner")}',
            f'6. 【前端】JavaScript零基础轻松入门教程 (JavaScript Tutorials For Beginners)：\nhttps://skillflow-javascript-beginner.vercel.app/playlist.html?playlist={quote("【前端】JavaScript零基础轻松入门教程 (JavaScript Tutorials For Beginners)")}',
            f'7. Namaste 🙏 JavaScript：\nhttps://skillflow-javascript-beginner.vercel.app/playlist.html?playlist={quote("Namaste 🙏 JavaScript")}'
        ],
        'Intermediate': [
            f'JavaScript 課程學習路徑 :\n\n1. The Complete JavaScript Course _ Zero to Advanced in 65 Hours：\nhttps://javascript-intermediate-phi.vercel.app/playlist.html?playlist={quote("The Complete JavaScript Course _ Zero to Advanced in 65 Hours")}',
            f'2. JavaScript 網頁前端工程進階教學：\nhttps://javascript-intermediate-phi.vercel.app/playlist.html?playlist={quote("JavaScript 網頁前端工程進階教學")}',
            f'3. Namaste 🙏 JavaScript：\nhttps://javascript-intermediate-phi.vercel.app/playlist.html?playlist={quote("Namaste 🙏 JavaScript")}',
            f'4. The Complete JavaScript Course _ Zero to Advanced in 65 Hours：\nhttps://javascript-advanced-ten.vercel.app/playlist.html?playlist={quote("The Complete JavaScript Course _ Zero to Advanced in 65 Hours")}',
            f'5. Namaste 🙏 JavaScript：\nhttps://javascript-advanced-ten.vercel.app/playlist.html?playlist={quote("Namaste 🙏 JavaScript")}'
        ],
        'Advanced': [
            f'JavaScript 課程學習路徑 :\n\n1. The Complete JavaScript Course _ Zero to Advanced in 65 Hours：\nhttps://javascript-advanced-ten.vercel.app/playlist.html?playlist={quote("The Complete JavaScript Course _ Zero to Advanced in 65 Hours")}',
            f'2. Namaste 🙏 JavaScript：\nhttps://javascript-advanced-ten.vercel.app/playlist.html?playlist={quote("Namaste 🙏 JavaScript")}'
        ],
        'Expert': [
            f'JavaScript 課程學習路徑 :\n\n1. Chai aur Javascript Backend _ Hindi：\nhttps://javascript-expert.vercel.app/playlist.html?playlist={quote("Chai aur Javascript Backend _ Hin")}'
        ]
    },
    'C++': {
        'Beginner': [
            f'C++ 課程學習路徑 :\n\n1. 【尚硅谷】2023版C++零基础教程，c++项目实战，清华学神带你一套通关：\nhttps://skillflow-c-plusplus-beginner.vercel.app/playlist.html?playlist={quote("【尚硅谷】2023版C%2B%2B零基础教程，c%2B%2B项目实战，清华学神带你一套通关")}',
            f'2. C++ - Projects：\nhttps://skillflow-c-plusplus-beginner.vercel.app/playlist.html?playlist={quote("C%2B%2B - Projects")}',
            f'3. 程式設計（C++）— 完整課程：\nhttps://skillflow-c-plusplus-beginner.vercel.app/playlist.html?playlist={quote("程式設計（C%2B%2B）— 完整課程")}',
            f'4. C++ GUI applications (beginner to advanced)：\nhttps://skillflow-c-plusplus-beginner.vercel.app/playlist.html?playlist={quote("C%2B%2B GUI applications (beginner to advanced)")}',
            f'5. C語言線上課程教學 - 近代程式語言的基礎：\nhttps://skillflow-c-plusplus-beginner.vercel.app/playlist.html?playlist={quote("C語言線上課程教學 - 近代程式語言的基礎")}',
            f'6. QT C++ GUI Tutorial For Beginners：\nhttps://skillflow-c-plusplus-beginner.vercel.app/playlist.html?playlist={quote("QT C%2B%2B GUI Tutorial For Beginners")}'
        ],
        'Intermediate': [
            f'C++ 課程學習路徑 :\n\n1. 程式設計（C++）— 完整課程：\nhttps://skillflow-c-plusplus-intermediate.vercel.app/playlist.html?playlist={quote("程式設計（C%2B%2B）— 完整課程")}',
            f'2. C++ - Projects：\nhttps://skillflow-c-plusplus-intermediate.vercel.app/playlist.html?playlist={quote("C%2B%2B - Projects")}',
            f'3. QT C++ GUI Tutorial For Beginners：\nhttps://skillflow-c-plusplus-intermediate.vercel.app/playlist.html?playlist={quote("QT C%2B%2B GUI Tutorial For Beginners")}'
        ],
        'Advanced': [
            f'C++ 課程學習路徑 :\n\n1. C++ - Projects：\nhttps://c-plusplus-advanced.vercel.app/playlist.html?playlist={quote("C%2B%2B - Projects")}',
            f'2. QT C++ GUI Tutorial For Beginners：\nhttps://c-plusplus-advanced.vercel.app/playlist.html?playlist={quote("QT C%2B%2B GUI Tutorial For Beginners")}'
        ],
        'Expert': [
            f'C++ 課程學習路徑 :\n\n1. C++ - Projects：\nhttps://c-plusplus-expert.vercel.app/playlist.html?playlist={quote("C%2B%2B - Projects")}'
        ]
    },
    'Linux': {
        'Beginner': [
            f'Linux 課程學習路徑 :\n\n1. 【尚硅谷】Linux+Shell教程 3天搞定Linux，1天搞定Shell：\nhttps://skillflow-linux-beginner.vercel.app/playlist.html?playlist={quote("【尚硅谷】Linux%2BShell教程 3天搞定Linux，1天搞定Shell")}',
            f'2. Docker and Kubernetes Tutorial for Beginners：\nhttps://skillflow-linux-beginner.vercel.app/playlist.html?playlist={quote("Docker and Kubernetes Tutorial for Beginners")}',
            f'3.Linux for Beginners：\nhttps://skillflow-linux-beginner.vercel.app/playlist.html?playlist={quote("Linux for Beginners")}',
            f'4. Linux 核心設計：\nhttps://skillflow-linux-beginner.vercel.app/playlist.html?playlist={quote("Linux 核心設計")}',
            f'5. Linux Essentials For Hackers：\nhttps://skillflow-linux-beginner.vercel.app/playlist.html?playlist={quote("Linux Essentials For Hackers")}',
            f'6. Free Docker Fundamentals Course - just enough docker to do stuff：\nhttps://skillflow-linux-beginner.vercel.app/playlist.html?playlist={quote("Free Docker Fundamentals Course - just enough docker to do stuff")}',
            f'7. Linux Zero to Hero _ Free Linux Course：\nhttps://skillflow-linux-beginner.vercel.app/playlist.html?playlist={quote("Linux Zero to Hero _ Free Linux Course")}',
            f'8. Linux 教學計畫 - Unix Linux 作業系統實務：\nhttps://skillflow-linux-beginner.vercel.app/playlist.html?playlist={quote("Linux 教學計畫 - Unix Linux 作業系統實務")}'
        ],
        'Intermediate': [
            f'Linux 課程學習路徑 :\n\n1. Linux 核心設計：\nhttps://skillflow-linux-intermediate-1n64.vercel.app/playlist.html?playlist={quote("Linux 核心設計")}',
            f'2. Docker and Kubernetes Tutorial for Beginners：\nhttps://skillflow-linux-intermediate-1n64.vercel.app/playlist.html?playlist={quote("Docker and Kubernetes Tutorial for Beginners")}',
            f'3. Free Docker Fundamentals Course - just enough docker to do stuff：\nhttps://skillflow-linux-intermediate-1n64.vercel.app/playlist.html?playlist={quote("Free Docker Fundamentals Course - just enough docker to do stuff")}',
            f'4. Linux 教學計畫 - Unix Linux 作業系統實務：\nhttps://skillflow-linux-intermediate-1n64.vercel.app/playlist.html?playlist={quote("Linux 教學計畫 - Unix Linux 作業系統實務")}',
            f'5. 【尚硅谷】Linux+Shell教程 3天搞定Linux，1天搞定Shell：\nhttps://skillflow-linux-intermediate-1n64.vercel.app/playlist.html?playlist={quote("【尚硅谷】Linux%2BShell教程 3天搞定Linux，1天搞定Shell")}'
        ],
        'Advanced': [
            f'Linux 課程學習路徑 :\n\n1. Linux 核心設計：\nhttps://skillflow-linux-advanced.vercel.app/playlist.html?playlist={quote("Linux 核心設計")}'
        ],
        'Expert': [
            f'Linux 課程學習路徑 :\n\n1. Docker and Kubernetes Tutorial for Beginners：\nhttps://skillflow-linux-expert.vercel.app/playlist.html?playlist={quote("Docker and Kubernetes Tutorial for Beginners")}'
        ]
    }
}
