import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from matplotlib.gridspec import GridSpec
import matplotlib.patheffects as path_effects

from datetime import datetime
from . import PDFReport

fontManager.addfont('msjh.ttc')


class EnhancedSkillRadarPDFReport(PDFReport):
    def __init__(self, job_skill):
        super().__init__(job_skill)

        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#34495e',
            'success': '#66E6C7',
            'warning': '#f39c12',
            'danger': '#E5008E',
            'info': '#3498db',
            'light': '#ecf0f1',
            'accent1': '#9b59b6',
            'accent2': '#1abc9c'
        }

    def create_cover_page(self, pdf_pages, title, subtitle):
        fig, ax = plt.subplots(figsize=(8.27, 11.69))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14)
        ax.axis('off')
        fig.patch.set_facecolor('white')

        gradient = np.linspace(0, 1, 256).reshape(256, 1)
        ax.imshow(
            gradient,
            extent=(0, 10, 0, 14),
            aspect='auto',
            cmap='viridis',
            alpha=0.08
        )

        circle1 = Circle(
            (1.5, 11.5),
            1.2,
            facecolor=self.colors['info'],
            alpha=0.2
        )
        circle2 = Circle(
            (8.5, 2.5),
            0.8,
            facecolor=self.colors['accent1'],
            alpha=0.2
        )
        triangle = plt.Polygon(
            [(8, 11), (9, 11), (8.5, 12)],
            facecolor=self.colors['warning'],
            alpha=0.3
        )
        ax.add_patch(circle1)
        ax.add_patch(circle2)
        ax.add_patch(triangle)

        main_title = ax.text(
            5,
            10,
            title,
            fontsize=28,
            fontweight='bold',
            ha='center',
            va='center',
            color=self.colors['primary']
        )
        main_title.set_path_effects(
            [
                path_effects.withStroke(linewidth=2, foreground='white')
            ]
        )

        ax.text(
            5,
            9.2,
            subtitle,
            fontsize=16,
            ha='center',
            va='center',
            color=self.colors['secondary'],
            style='italic'
        )
        ax.plot(
            [2.5, 7.5],
            [8.6, 8.6],
            color=self.colors['info'],
            linewidth=3,
            alpha=0.8
        )
        ax.plot(
            [3, 7],
            [8.4, 8.4],
            color=self.colors['warning'],
            linewidth=2,
            alpha=0.6
        )

        info_panel = FancyBboxPatch(
            (1.5, 5.5),
            7,
            2.2,
            boxstyle='round,pad=0.15',
            facecolor=self.colors['light'],
            edgecolor=self.colors['info'],
            linewidth=2,
            alpha=0.9
        )
        ax.add_patch(info_panel)

        current_date = datetime.now().strftime('%Y/%m/%d')
        ax.text(
            5,
            7.2,
            f'報告日期：{current_date}',
            fontsize=13,
            ha='center',
            color=self.colors['primary'],
            fontweight='bold'
        )

        ax.text(
            5,
            6.2,
            '本報告提供個人化職涯發展建議',
            fontsize=11,
            ha='center',
            color=self.colors['secondary']
        )

        slogan_box = FancyBboxPatch(
            (1.5, 2),
            7,
            1,
            boxstyle='round,pad=0.2',
            facecolor=self.colors['accent2'],
            alpha=0.8
        )
        ax.add_patch(slogan_box)

        ax.text(
            5,
            2.5,
            '持續學習 · 不斷進步',
            fontsize=14,
            ha='center',
            color='white',
            fontweight='bold'
        )

        plt.tight_layout(pad=1.0)
        pdf_pages.savefig(
            fig,
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none'
        )
        plt.close(fig)

    def create_recommendation_section(self, ax, title, jobs, color):
        ax.axis('off')

        title_box = FancyBboxPatch(
            (0, 0.8),
            1,
            0.15,
            boxstyle='round,pad=0.02',
            facecolor=color,
            alpha=0.8,
            transform=ax.transAxes
        )
        ax.add_patch(title_box)

        ax.text(
            0.5,
            0.875,
            title,
            transform=ax.transAxes,
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold',
            color='white'
        )

        if not jobs:
            ax.text(
                0.5,
                0.4,
                '暫無符合條件的職業推薦',
                transform=ax.transAxes,
                ha='center',
                va='center',
                fontsize=10,
                color=self.colors['secondary'],
                style='italic'
            )
            return

        y_positions = [0.65, 0.45, 0.25]
        for i, job in enumerate(jobs[:3]):
            y = y_positions[i]

            job_text = f"{job['job_title']}（{job['match_rate']:.1f}%）"
            ax.text(
                0.05,
                y,
                job_text,
                transform=ax.transAxes,
                fontsize=10,
                fontweight='bold',
                color=self.colors['primary']
            )

            strengths_text = ''
            if job['strengths']:
                strengths_text = f"優勢：{'、'.join(job['strengths'][:3])}"

                if len(job['strengths']) > 3:
                    strengths_text += f"等 {len(job['strengths'])} 項"

            missing_text = ''
            if job['missing_skills']:
                missing_text = f"待提升：{'、'.join(job['missing_skills'][:2])}"

                if len(job['missing_skills']) > 2:
                    missing_text += f"等 {len(job['missing_skills'])} 項"

            combined_text = ' | '.join(filter(None, [strengths_text, missing_text]))
            ax.text(
                0.05,
                y - 0.08,
                combined_text,
                transform=ax.transAxes,
                fontsize=8,
                color='#0074CD'
            )

    def create_career_recommendation_page(self, pdf_pages, user_skills):
        recommendations = self.career_recommender.analyze_user_skills(user_skills)

        fig = plt.figure(figsize=(8.27, 11.69))
        fig.patch.set_facecolor('white')
        fig.suptitle(
            '職業發展推薦分析\n\n',
            fontsize=18,
            fontweight='bold',
            color=self.colors['primary'],
            y=0.94
        )

        gs = GridSpec(
            4,
            1,
            figure=fig,
            height_ratios=[1, 1, 1, 0.5],
            hspace=0.3,
            top=0.85,
            bottom=0.05,
            left=0.1,
            right=0.9
        )

        ax1 = fig.add_subplot(gs[0, 0])
        self.create_recommendation_section(
            ax1,
            '優秀匹配職業（高達 80%）',
            recommendations['excellent'],
            self.colors['success']
        )

        ax2 = fig.add_subplot(gs[1, 0])
        self.create_recommendation_section(
            ax2,
            '良好匹配職業（高達 65%）',
            recommendations['good'],
            self.colors['warning']
        )

        ax3 = fig.add_subplot(gs[2, 0])
        self.create_recommendation_section(
            ax3,
            '潛力發展職業（高達 50%）',
            recommendations['potential'],
            self.colors['info']
        )

        pdf_pages.savefig(
            fig,
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none'
        )
        plt.close(fig)

    def create_enhanced_radar(self, ax, categories, current_values, target_values):
        n = len(categories)
        angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
        angles += angles[:1]

        current = current_values + current_values[:1]
        target = target_values + target_values[:1]

        ax.set_ylim(0, 110)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=9, alpha=0.7)

        ax.grid(
            True,
            alpha=0.3,
            linewidth=1,
            color=self.colors['secondary']
        )

        ax.plot(
            angles,
            target,
            'o-',
            linewidth=3,
            markersize=6,
            label='目標技能',
            color=self.colors['danger'],
            alpha=0.9,
            zorder=3
        )
        ax.fill(
            angles,
            target,
            alpha=0.1,
            color=self.colors['danger']
        )

        ax.plot(
            angles,
            current,
            'o-',
            linewidth=3,
            markersize=6,
            label='目前技能',
            color=self.colors['info'],
            alpha=0.9,
            zorder=4
        )
        ax.fill(
            angles,
            current,
            alpha=0.2,
            color=self.colors['info']
        )

        ax.set_xticks(angles[:-1])

        short_categories = []
        for cat in categories:
            if len(cat) > 8:
                short_categories.append(cat[:6] + '..')
            else:
                short_categories.append(cat)

        for i, (angle, label) in enumerate(zip(angles[:-1], short_categories)):
            current_val = current_values[i]
            target_val = target_values[i]
            achievement = current_val / target_val if target_val > 0 else 0

            if achievement >= 1.0:
                bbox_color = self.colors['success']
                text_color = 'white'
            elif achievement >= 0.8:
                bbox_color = self.colors['warning']
                text_color = 'white'
            else:
                bbox_color = self.colors['danger']
                text_color = 'white'

            label_radius = 130 if i < n // 2 else 120
            ax.text(
                angle,
                label_radius,
                label,
                ha='center',
                va='center',
                fontsize=9,
                fontweight='bold',
                color=text_color,
                bbox=dict(
                    boxstyle='round,pad=0.3',
                    facecolor=bbox_color,
                    edgecolor='white',
                    linewidth=1,
                    alpha=0.9
                )
            )

            score_radius = max(20, current_val - 10)
            ax.text(
                angle,
                score_radius,
                f'{current_val}',
                ha='center',
                va='center',
                fontsize=8,
                fontweight='bold',
                color=self.colors['primary'],
                bbox=dict(
                    boxstyle='circle,pad=0.2',
                    facecolor='white',
                    edgecolor=bbox_color,
                    linewidth=1.5,
                    alpha=0.9
                )
            )

        ax.legend(
            loc='upper right',
            bbox_to_anchor=(1.2, 1.0),
            fontsize=10
        )

    def create_detailed_table(self, ax, categories, current_values, target_values):
        ax.axis('off')

        achievement_rates = [(c / t * 100 if t > 0 else 0) for c, t in zip(current_values, target_values)]
        gaps = [t - c for c, t in zip(current_values, target_values)]

        table_data = []
        for i, (cat, cur, tar, rate, gap) in enumerate(
                zip(categories, current_values, target_values, achievement_rates, gaps)
        ):
            short_cat = cat[:8] + '..' if len(cat) > 8 else cat

            if rate >= 100:
                status = '達標'
                priority = '保持'
            elif rate >= 50:
                status = '接近'
                priority = '優化'
            else:
                status = '待改進'
                priority = '重點'

            table_data.append(
                [
                    short_cat,
                    f'{cur}',
                    f'{tar}',
                    f'{rate:.0f}%',
                    f'+{gap}' if gap > 0 else '0',
                    status,
                    priority
                ]
            )

        table = ax.table(
            cellText=table_data,
            colLabels=['技能', '當前', '目標', '達成率', '差距', '狀態', '優先級'],
            cellLoc='center',
            loc='center',
            colWidths=[0.18, 0.1, 0.1, 0.12, 0.1, 0.14, 0.12]
        )
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.8)

        for (i, j), cell in table.get_celld().items():
            if i == 0:
                cell.set_text_props(weight='bold', color='white')
                cell.set_facecolor(self.colors['primary'])
                cell.set_height(0.1)
            else:
                rate = achievement_rates[i - 1] if i <= len(achievement_rates) else 0
                if j in [5, 6]:
                    if rate >= 100:
                        cell.set_facecolor('#d4edda')
                    elif rate >= 80:
                        cell.set_facecolor('#fff3cd')
                    else:
                        cell.set_facecolor('#f8d7da')
                else:
                    cell.set_facecolor('#f8f9fa' if i % 2 == 0 else 'white')

            cell.set_edgecolor('#dee2e6')
            cell.set_linewidth(0.5)

    def create_detailed_radar_page(self, pdf_pages, categories, current_values, target_values):
        fig = plt.figure(figsize=(8.27, 11.69))
        fig.patch.set_facecolor('white')
        fig.suptitle(
            '技能雷達圖分析\n\n',
            fontsize=18,
            fontweight='bold',
            color=self.colors['primary'],
            y=0.94
        )

        gs = GridSpec(
            3,
            1,
            figure=fig,
            height_ratios=[2.2, 1, 0.3],
            hspace=0.25,
            top=0.799,
            bottom=0.05,
            left=0.1,
            right=0.9
        )

        ax_radar = fig.add_subplot(gs[0, 0], projection='polar')
        self.create_enhanced_radar(ax_radar, categories, current_values, target_values)

        ax_table = fig.add_subplot(gs[1, 0])
        self.create_detailed_table(ax_table, categories, current_values, target_values)

        pdf_pages.savefig(
            fig,
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none',
            pad_inches=0.2
        )
        plt.close(fig)

    def generate_comprehensive_pdf_report(
            self,
            categories,
            current_values,
            target_values,
            user_skills,
            filename,
            title
    ):
        try:
            with PdfPages(filename) as pdf_pages:
                self.create_cover_page(pdf_pages, title, '個人職能發展評估')

                self.create_detailed_radar_page(pdf_pages, categories, current_values, target_values)

                if user_skills:
                    self.create_career_recommendation_page(pdf_pages, user_skills)

                metadata = pdf_pages.infodict()
                metadata['Title'] = title

            print(f'綜合 PDF 報告生成完成：{filename}')
            return filename

        except Exception as e:
            print(f'生成報告時發生錯誤：{e}')
            return None


class CareerSpecificReportGenerator(PDFReport):
    def __init__(self, job_skill, learning_paths, learning_resources):
        super().__init__(job_skill, learning_paths, learning_resources)

        self.colors = {'primary': '#2c3e50'}

    @staticmethod
    def calculate_job_match_score(job_skills, user_skills):
        if not job_skills:
            return 0

        total_score = 0
        for skill in job_skills:
            skill_score = user_skills.get(skill, 0)
            total_score += skill_score

        return total_score / len(job_skills)

    @staticmethod
    def get_user_skill_level(skill_name, user_skills):
        score = user_skills.get(skill_name, 0)

        if score >= 100:
            return 'Expert'
        elif score >= 70:
            return 'Advanced'
        elif score >= 50:
            return 'Intermediate'
        else:
            return 'Beginner'

    def create_cover_page(self, pdf_pages, job_title, job_skills, user_skills):
        fig, ax = plt.subplots(figsize=(8.27, 11.69))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14)
        ax.axis('off')
        fig.patch.set_facecolor('white')

        orange_block = plt.Polygon(
            [(0, 14), (0, 11), (2.5, 10.5), (3.5, 12), (2, 14)],
            facecolor='#FFA726',
            alpha=0.8,
            zorder=1
        )
        ax.add_patch(orange_block)

        blue_block = plt.Polygon(
            [(6.5, 14), (10, 14), (10, 10.5), (7.5, 11), (6, 13)],
            facecolor='#42A5F5',
            alpha=0.8,
            zorder=1
        )
        ax.add_patch(blue_block)

        light_blue_block = plt.Polygon(
            [(0, 3.5), (0, 0), (4, 0), (3.5, 2), (1.5, 4)],
            facecolor='#81D4FA',
            alpha=0.7,
            zorder=1
        )
        ax.add_patch(light_blue_block)

        right_orange_block = plt.Polygon(
            [(7, 2), (10, 0), (10, 4), (8.5, 3.5)],
            facecolor='#FFB74D',
            alpha=0.6,
            zorder=1
        )
        ax.add_patch(right_orange_block)

        main_area = FancyBboxPatch(
            (1.5, 3.5),
            7,
            7.5,
            boxstyle='round,pad=0.2',
            facecolor='white',
            edgecolor='none',
            alpha=0.95,
            zorder=2
        )
        ax.add_patch(main_area)

        ax.text(
            5,
            9.8,
            job_title,
            fontsize=24,
            fontweight='bold',
            ha='center',
            va='center',
            color='#2c3e50',
            zorder=4
        )
        ax.text(
            5,
            9.1,
            'SkillFlow 個人化學習地圖',
            fontsize=16,
            ha='center',
            va='center',
            color='#42A5F5',
            fontweight='normal',
            zorder=4
        )

        ax.plot(
            [2.5, 7.5],
            [8.6, 8.6],
            color='#42A5F5',
            linewidth=2,
            alpha=0.8,
            zorder=4
        )

        ax.text(
            5,
            8.2,
            '所需核心技能',
            fontsize=14,
            fontweight='bold',
            ha='center',
            va='center',
            color='#2c3e50',
            zorder=4
        )

        skills_per_column = 3
        left_skills = job_skills[:skills_per_column]
        right_skills = job_skills[skills_per_column:]

        y_start = 7.6
        for i, skill in enumerate(left_skills):
            score = user_skills.get(skill, 0)

            if score >= 75:
                status_color = '#27AE60'
                status = '精通'
            elif score >= 50:
                status_color = '#F39C12'
                status = '良好'
            elif score >= 25:
                status_color = '#E67E22'
                status = '基礎'
            else:
                status_color = '#E74C3C'
                status = '待加強'

            ax.text(
                2.2,
                y_start - i * 0.4,
                f'{skill}',
                fontsize=11,
                ha='left',
                va='center',
                color='#2c3e50',
                fontweight='bold',
                zorder=4
            )
            ax.text(
                2.2,
                y_start - i * 0.4 - 0.2,
                f'{score}分 {status}',
                fontsize=9,
                ha='left',
                va='center',
                color=status_color,
                zorder=4
            )

        for i, skill in enumerate(right_skills):
            score = user_skills.get(skill, 0)

            if score >= 75:
                status_color = '#27AE60'
                status = '精通'
            elif score >= 50:
                status_color = '#F39C12'
                status = '良好'
            elif score >= 25:
                status_color = '#E67E22'
                status = '基礎'
            else:
                status_color = '#E74C3C'
                status = '待加強'

            ax.text(
                6.8,
                y_start - i * 0.4,
                f'{skill}',
                fontsize=11,
                ha='left',
                va='center',
                color='#2c3e50',
                fontweight='bold',
                zorder=4
            )
            ax.text(
                6.8,
                y_start - i * 0.4 - 0.2,
                f'{score}分 {status}',
                fontsize=9,
                ha='left',
                va='center',
                color=status_color,
                zorder=4
            )

        job_match_score = self.calculate_job_match_score(job_skills, user_skills)
        match_y = y_start - max(len(left_skills), len(right_skills)) * 0.4 - 0.8

        match_bg = FancyBboxPatch(
            (2.5, match_y - 0.4),
            5,
            0.8,
            boxstyle='round,pad=0.1',
            facecolor='#E8F5E8',
            edgecolor='#27AE60',
            linewidth=2,
            alpha=0.9,
            zorder=3
        )
        ax.add_patch(match_bg)

        ax.text(
            5,
            match_y,
            f'職業匹配度：{job_match_score:.1f}%',
            fontsize=12,
            fontweight='bold',
            ha='center',
            va='center',
            color='#27AE60',
            zorder=4
        )

        current_date = datetime.now().strftime('%Y/%m/%d')
        ax.text(
            5,
            4.8,
            f'報告生成日期：{current_date}',
            fontsize=11,
            ha='center',
            color='#666666',
            fontweight='normal',
            zorder=4
        )

        plt.tight_layout(pad=0.5)
        pdf_pages.savefig(fig, bbox_inches='tight', facecolor='white', edgecolor='none')
        plt.close(fig)

    def create_career_overview_page(self, pdf_pages, job_title, job_skills, user_skills):
        fig, ax = plt.subplots(figsize=(9, 16))
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        fig.patch.set_facecolor('#FAFBFC')

        title_rect = FancyBboxPatch(
            (5, 92),
            90,
            6,
            boxstyle='round,pad=0.5',
            facecolor='#42498d',
            edgecolor='#313338',
            linewidth=2
        )
        ax.add_patch(title_rect)
        ax.text(
            50,
            95,
            f'{job_title} - 技能分析總覽',
            ha='center',
            va='center',
            fontsize=20,
            fontweight='bold',
            color='#f5f5f5'
        )

        job_match_score = self.calculate_job_match_score(job_skills, user_skills)
        match_rect = FancyBboxPatch(
            (5, 84),
            90,
            4,
            boxstyle='round,pad=0.3',
            facecolor='white',
            edgecolor='#42A5F5',
            linewidth=1.5,
            alpha=0.9
        )
        ax.add_patch(match_rect)

        ax.text(
            25,
            86.5,
            f'職業匹配度：{job_match_score:.1f}%',
            ha='center',
            va='center',
            fontsize=14,
            fontweight='bold',
            color='#2C3E50'
        )

        if job_match_score >= 80:
            match_status = '非常適合'
            match_color = '#27AE60'
        elif job_match_score >= 60:
            match_status = '適合'
            match_color = '#F39C12'
        elif job_match_score >= 40:
            match_status = '需要提升'
            match_color = '#E67E22'
        else:
            match_status = '需大幅提升'
            match_color = '#E74C3C'

        ax.text(
            75,
            86.5,
            f'評價：{match_status}',
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold',
            color=match_color
        )

        y_pos = 70
        ax.text(
            15,
            y_pos,
            '技能名稱',
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold',
            color='#2C3E50'
        )
        ax.text(
            30,
            y_pos,
            '當前分數',
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold',
            color='#2C3E50'
        )
        ax.text(
            45,
            y_pos,
            '等級',
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold',
            color='#2C3E50'
        )
        ax.text(
            60,
            y_pos,
            '狀態',
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold',
            color='#2C3E50'
        )
        ax.text(
            80,
            y_pos,
            '學習優先級',
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold',
            color='#2C3E50'
        )

        ax.plot([5, 95], [y_pos - 2, y_pos - 2], color='#42A5F5', linewidth=2)

        for i, skill in enumerate(job_skills):
            score = user_skills.get(skill, 0)
            level = self.get_user_skill_level(skill, user_skills)
            y = y_pos - 5 - i * 6

            bg_color = '#f8f9fa' if i % 2 == 0 else 'white'
            bg_rect = FancyBboxPatch(
                (5, y - 1.5),
                90,
                4,
                boxstyle='round,pad=0.1',
                facecolor=bg_color,
                alpha=0.8
            )
            ax.add_patch(bg_rect)

            ax.text(
                15,
                y,
                skill,
                ha='center',
                va='center',
                fontsize=11,
                fontweight='bold',
                color='#2C3E50'
            )

            if score < 25:
                score_color = '#E74C3C'
            elif score < 50:
                score_color = '#F39C12'
            elif score < 75:
                score_color = '#27AE60'
            else:
                score_color = '#8E44AD'
            ax.text(
                30,
                y,
                f'{score}',
                ha='center',
                va='center',
                fontsize=11,
                fontweight='bold',
                color=score_color
            )

            ax.text(
                45,
                y,
                level,
                ha='center',
                va='center',
                fontsize=10,
                color='#34495E'
            )

            if score >= 75:
                status = '精通'
            elif score >= 50:
                status = '良好'
            elif score >= 25:
                status = '基礎'
            else:
                status = '待加強'

            ax.text(
                60,
                y,
                status,
                ha='center',
                va='center',
                fontsize=9,
                fontweight='bold'
            )

            if score < 25:
                priority = '高'
            elif score < 50:
                priority = '中'
            else:
                priority = '低'
            priority_color = '#E74C3C' if priority == '高' else '#F39C12' if priority == '中' else '#27AE60'
            ax.text(
                80,
                y,
                priority,
                ha='center',
                va='center',
                fontsize=10,
                color=priority_color,
                fontweight='bold'
            )

        plt.tight_layout()
        pdf_pages.savefig(fig, bbox_inches='tight', facecolor='#FAFBFC', edgecolor='none')
        plt.close(fig)

    def generate_personalized_learning_path(self, skill_name, user_skills):
        current_level = self.get_user_skill_level(skill_name, user_skills)

        if skill_name in self.career_recommender.learning_paths:
            all_modules = self.career_recommender.learning_paths[skill_name]
        else:
            return [], current_level, f'暫無 {skill_name} 的詳細學習路徑'

        if current_level == 'Beginner':
            filtered_modules = all_modules
            recommendation = '從基礎課程開始，循序漸進學習'
        elif current_level == 'Intermediate':
            filtered_modules = [m for m in all_modules if m['level'] in ['Intermediate', 'Advanced', 'Expert']]
            recommendation = '從中級課程開始深入學習'
        elif current_level == 'Advanced':
            filtered_modules = [m for m in all_modules if m['level'] in ['Advanced', 'Expert']]
            recommendation = '專注於高級技術技能提升'
        else:
            filtered_modules = [m for m in all_modules if m['level'] in ['Advanced', 'Expert']]
            recommendation = '可選擇專家課程技能精進'

        return filtered_modules, current_level, recommendation

    def draw_personalized_module(self, ax, module, x, y, w=40, h=4):
        level_color = self.career_recommender.level_info[module['level']]['color']
        border_color = self.career_recommender.level_info[module['level']]['border']

        rect = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle='round,pad=0.3',
            facecolor=level_color,
            edgecolor=border_color,
            linewidth=2,
            alpha=0.9
        )
        ax.add_patch(rect)

        ax.text(
            x + w / 2,
            y + h / 2 + 0.3,
            module['name'],
            ha='center',
            va='center',
            fontsize=9,
            fontweight='bold',
            color='#2C3E50'
        )
        ax.text(
            x + w - 0.5,
            y + 0.3,
            module['duration'],
            ha='right',
            va='bottom',
            fontsize=9,
            color='#34495E',
            fontweight='bold'
        )
        return rect

    def draw_personalized_legend(self, ax, current_level, x=72, y=75):
        ax.text(
            x,
            y + 5,
            f'學習階段 (當前：{current_level})',
            ha='left',
            va='center',
            fontsize=12,
            fontweight='bold',
            color='#2C3E50'
        )

        box_w, box_h = 1.8, 1.0

        if current_level == "Beginner":
            shown_levels = ["Beginner", "Intermediate", "Advanced", "Expert"]
        elif current_level == "Intermediate":
            shown_levels = ["Intermediate", "Advanced", "Expert"]
        else:
            shown_levels = ["Advanced", "Expert"]

        for i, level in enumerate(shown_levels):
            info = self.career_recommender.level_info[level]
            y_pos = y - i * 5

            rect = FancyBboxPatch(
                (x, y_pos),
                box_w,
                box_h,
                boxstyle='round,pad=0.2',
                facecolor=info['color'],
                edgecolor=info['border'],
                linewidth=1.5
            )
            ax.add_patch(rect)

            level_name = info['name']
            if level == current_level:
                level_name += '（當前）'
                text_color = '#FF6B6B'
                font_weight = 'bold'
            else:
                text_color = '#2C3E50'
                font_weight = 'normal'

            ax.text(
                x + box_w + 1,
                y_pos + box_h / 2,
                level_name,
                ha='left',
                va='center',
                fontsize=9,
                fontweight=font_weight,
                color=text_color
            )
            ax.text(
                x + box_w + 1,
                y_pos - 0.9,
                info['desc'],
                ha='left',
                va='center',
                fontsize=7,
                color='#5D6D7E'
            )

    @staticmethod
    def compute_positions(n_modules, x=25, start_y=85, spacing=6):
        return [(x, start_y - i * spacing) for i in range(n_modules)]

    @staticmethod
    def draw_arrow(ax, start_rect, end_rect):
        start_point = (start_rect.get_x() + start_rect.get_width() / 2, start_rect.get_y())
        end_point = (end_rect.get_x() + end_rect.get_width() / 2, end_rect.get_y() + end_rect.get_height())
        arrow = FancyArrowPatch(
            start_point,
            end_point,
            arrowstyle='->',
            mutation_scale=15,
            color='#7F8C8D',
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(arrow)

    def create_personalized_learning_roadmap_page(self, pdf_pages, skill_name, user_skills):
        fig, ax = plt.subplots(figsize=(9, 16))
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        fig.patch.set_facecolor('#FAFBFC')

        filtered_modules, current_level, recommendation = self.generate_personalized_learning_path(
            skill_name,
            user_skills
        )
        current_score = user_skills.get(skill_name, 0)

        title_rect = FancyBboxPatch(
            (5, 92),
            90,
            6,
            boxstyle='round,pad=0.5',
            facecolor='#42498d',
            edgecolor='#313338',
            linewidth=2
        )
        ax.add_patch(title_rect)
        ax.text(
            50,
            95,
            f'{skill_name} 個人化學習路徑',
            ha='center',
            va='center',
            fontsize=20,
            fontweight='bold',
            color='#f5f5f5'
        )

        status_rect = FancyBboxPatch(
            (5, 84),
            90,
            4,
            boxstyle='round,pad=0.3',
            facecolor='white',
            edgecolor='#42A5F5',
            linewidth=1.5,
            alpha=0.9
        )
        ax.add_patch(status_rect)

        ax.text(
            15,
            86.5,
            f'當前技能等級：{current_level}',
            ha='left',
            va='center',
            fontsize=12,
            fontweight='bold',
            color='#2C3E50'
        )
        ax.text(
            15,
            85,
            f'技能分數：{current_score}/100',
            ha='left',
            va='center',
            fontsize=11,
            color='#34495E'
        )
        ax.text(
            65,
            85,
            recommendation,
            ha='left',
            va='center',
            fontsize=10,
            color='#42A5F5',
            style='italic'
        )

        positions = self.compute_positions(len(filtered_modules), start_y=77)
        rects = []
        for i, (module, pos) in enumerate(zip(filtered_modules, positions)):
            rect = self.draw_personalized_module(ax, module, *pos)
            rects.append(rect)

        for i in range(len(rects) - 1):
            self.draw_arrow(ax, rects[i], rects[i + 1])
        self.draw_personalized_legend(ax, current_level)

        plt.tight_layout()
        pdf_pages.savefig(fig, bbox_inches='tight', facecolor='#FAFBFC', edgecolor='none')
        plt.close(fig)

    def create_level_specific_learning_resources_page(self, pdf_pages, skill_name, user_skills):
        fig, ax = plt.subplots(figsize=(9, 16))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14)
        ax.axis('off')
        fig.patch.set_facecolor('white')

        current_level = self.get_user_skill_level(skill_name, user_skills)

        title_rect = FancyBboxPatch(
            (0.5, 12.5),
            9,
            1.2,
            boxstyle='round,pad=0.1',
            facecolor=self.colors['primary'],
            alpha=0.9
        )
        ax.add_patch(title_rect)
        ax.text(
            5,
            13.1,
            f'{skill_name} {self.career_recommender.level_info[current_level]["name"]}學習資源推薦',
            ha='center',
            va='center',
            fontsize=18,
            fontweight='bold',
            color='white'
        )

        if (skill_name in self.career_recommender.learning_resources and
                current_level in self.career_recommender.learning_resources[skill_name]):
            resources = self.career_recommender.learning_resources[skill_name][current_level]
        else:
            resources = []

        if not resources:
            ax.text(
                5,
                7,
                f'目前尚無 {skill_name} 的 {self.career_recommender.level_info[current_level]["name"]} 學習資源',
                ha='center',
                va='center',
                fontsize=16,
                color='#666666'
            )
            ax.text(
                5,
                6,
                '建議透過相關技術社群或論壇尋找最新資源',
                ha='center',
                va='center',
                fontsize=12,
                color='#666666'
            )
        else:
            table_data = [[resource['name'], resource['url']] for resource in resources]
            table = ax.table(
                cellText=table_data,
                colLabels=['資源名稱', '學習階段'],
                cellLoc='left',
                loc='center',
                colWidths=[1.5, 1.1],
                bbox=[0.05, 0.10, 0.9, 0.75]
            )

            table.auto_set_font_size(False)
            table.set_fontsize(11)
            table.scale(1, 9.5)

            for j in range(2):
                cell = table[(0, j)]
                cell.set_text_props(weight='bold', color='white')
                cell.set_facecolor(self.colors['primary'])
                cell.set_height(0.03)

            for i in range(1, len(table_data) + 1):
                name_cell = table[(i, 0)]
                name_cell.set_facecolor('#f8f9fa' if i % 2 == 0 else 'white')
                name_cell.set_text_props(weight='bold', color=self.colors['primary'])
                name_cell.set_edgecolor('#dee2e6')
                name_cell.set_linewidth(0.5)

                url_cell = table[(i, 1)]
                url_cell.set_facecolor('#f8f9fa' if i % 2 == 0 else 'white')
                url_cell.set_text_props(color='#007BFF', url=table_data[i - 1][1])
                url_cell.set_edgecolor('#dee2e6')
                url_cell.set_linewidth(0.5)

        plt.tight_layout()
        pdf_pages.savefig(fig, bbox_inches='tight', facecolor='white', edgecolor='none')
        plt.close(fig)

    def generate_comprehensive_pdf_report(self, job_title, user_skills, filename):
        job_skills = self.career_recommender.get_job_skills(job_title)

        if not job_skills:
            print(f'找不到{job_title}的技能要求')
            return None

        try:
            with PdfPages(filename) as pdf_pages:
                self.create_cover_page(pdf_pages, job_title, job_skills, user_skills)

                self.create_career_overview_page(pdf_pages, job_title, job_skills, user_skills)

                skills_with_paths = []
                for skill in job_skills:
                    if skill in self.career_recommender.learning_paths:
                        skills_with_paths.append(skill)
                        self.create_personalized_learning_roadmap_page(pdf_pages, skill, user_skills)
                        self.create_level_specific_learning_resources_page(pdf_pages, skill, user_skills)

                metadata = pdf_pages.infodict()
                metadata['Title'] = f'{job_title} 個人化技能學習路徑'
                metadata['Subject'] = f'{job_title} 個人化技能學習路徑與資源推薦'
                metadata['Author'] = '職業技能發展系統'
                metadata['Creator'] = 'Python Matplotlib'

            for skill in job_skills:
                score = user_skills.get(skill, 0)
                level = self.get_user_skill_level(skill, user_skills)
                has_guide = '✓' if skill in skills_with_paths else '○'
                print(f"   {has_guide} {skill}：{score}分 ({level})")

            return filename

        except Exception as e:
            print(f'生成報告時發生錯誤：{e}')
            return None




