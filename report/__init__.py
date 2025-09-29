from abc import ABC, abstractmethod


class CareerRecommendation:
    def __init__(self, job_skill, learning_paths=None, learning_resources=None):
        self.job_skill = job_skill
        self.learning_paths = learning_paths
        self.learning_resources = learning_resources

        self.skill_levels = {
            'Beginner': 25,
            'Intermediate': 50,
            'Advanced': 75,
            'Expert': 100
        }

        self.recommendation_thresholds = {
            'excellent': 75,
            'good': 50,
            'potential': 20
        }

        self.level_info = {
            "Beginner": {
                "color": "#E3F2FD",
                "name": "初學者",
                "desc": "基礎語法",
                "border": "#90CAF9"
            },
            "Intermediate": {
                "color": "#FFF3E0",
                "name": "中級",
                "desc": "核心技術",
                "border": "#FFB74D"
            },
            "Advanced": {
                "color": "#FFEBEE",
                "name": "高級",
                "desc": "進階開發",
                "border": "#F48FB1"
            },
            "Expert": {
                "color": "#F3E5F5",
                "name": "專家",
                "desc": "架構設計",
                "border": "#CE93D8"
            }
        }

    def get_job_skills(self, job_title):
        return self.job_skill.get(job_title, [])

    def analyze_user_skills(self, user_skills):
        recommendations = {
            'excellent': [],
            'good': [],
            'potential': []
        }

        for job_title, required_skills in self.job_skill.items():
            skill_scores = []
            missing_skills = []

            for skill in required_skills:
                if skill in user_skills:
                    skill_scores.append(user_skills[skill])
                else:
                    skill_scores.append(0)
                    missing_skills.append(skill)

            if skill_scores:
                avg_score = sum(skill_scores) / len(skill_scores)
                match_rate = avg_score / 100 * 100

                job_info = {
                    'job_title': job_title,
                    'match_rate': match_rate,
                    'avg_score': avg_score,
                    'skill_scores': dict(zip(required_skills, skill_scores)),
                    'missing_skills': missing_skills,
                    'strengths': [skill for skill, score in zip(required_skills, skill_scores) if score >= 75]
                }

                if match_rate >= self.recommendation_thresholds['excellent']:
                    recommendations['excellent'].append(job_info)
                elif match_rate >= self.recommendation_thresholds['good']:
                    recommendations['good'].append(job_info)
                elif match_rate >= self.recommendation_thresholds['potential']:
                    recommendations['potential'].append(job_info)

        for category in recommendations:
            recommendations[category].sort(key=lambda x: x['match_rate'], reverse=True)

        return recommendations

    def get_skill_improvement_suggestions(self, user_skills, target_job):
        if target_job not in self.job_skill:
            return None

        required_skills = self.job_skill[target_job]
        suggestions = []

        for skill in required_skills:
            current_score = user_skills.get(skill, 0)

            if current_score < 75:
                improvement_needed = 75 - current_score
                priority = '高' if current_score < 25 else '中' if current_score < 50 else '低'

                suggestions.append(
                    {
                        'skill': skill,
                        'current': current_score,
                        'target': 75,
                        'improvement': improvement_needed,
                        'priority': priority
                    }
                )

        return sorted(suggestions, key=lambda x: x['improvement'], reverse=True)


class PDFReport(ABC):
    def __init__(self, job_skill, learning_paths=None, learning_resources=None):
        self.career_recommender = CareerRecommendation(job_skill, learning_paths, learning_resources)

    @abstractmethod
    def create_cover_page(self, *args, **kwargs):
        pass

    @abstractmethod
    def generate_comprehensive_pdf_report(self, *args, **kwargs):
        pass
