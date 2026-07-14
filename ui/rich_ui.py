from ui.base_ui import BaseUI
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.rule import Rule

class RichUI(BaseUI):
    def __init__(self):
        self.console = Console()

    def clear(self):
        self.console.clear()

    def show_menu1(self, title, options):
        self.clear()
        self.console.print(title)
        for i, opt in enumerate(options, 0):
            self.console.print(i, opt)
        return int(self.console.input(">"))
    
    def show_menu(self,title,options):
        """
        Отображает красивое меню и возвращает выбранный пункт.
        """
        self.clear()

        table = Table(
            show_header=True,
            header_style="bold cyan",
            border_style="green"
        )

        table.add_column("№", justify="center", width=5)
        table.add_column("Действие")

        for i, option in enumerate(options, 0):
            table.add_row(str(i), option)

        panel = Panel(
            Align.center(table),
            title=f"[bold yellow]{title}[/bold yellow]",
            border_style="blue",
            padding=(1, 2)
        )

        self.console.print(panel)

        while True:
            try:
                choice = int(
                    self.console.input(
                        "\n[bold green]Выберите пункт:[/bold green] "
                    )
                )

                if 0 <= choice <= len(options):
                    return choice

                self.console.print(
                    "[red]Неверный номер пункта![/red]"
                )

            except ValueError:
                self.console.print(
                    "[red]Введите число![/red]"
                )

    def show_message(self, text):
        self.console.print(text)

    def ask_input(self, text):
        self.console.clear()
        return self.console.input(text)

    #def show_question(self, question):
    #    self.console.print(question)

    def show_question(self, question_num, total_questions, question_id, question_text, answers):    
    #    self.console.print(f"Вопрос {question_id}({question_num + 1}/{total_questions})")
    #    self.console.print(question_text)
    #    self.console.print(answers)
        self.clear

        self.console.print(
            Rule(
                f"[bold cyan]Вопрос{question_id}({question_num}/{total_questions})[/bold cyan]"
            )
           
        )
        self.console.print(
            Panel(
                question_text,
                title="❓ Вопрос",
                border_style="cyan"
            )
        )

        for i, answer in enumerate(answers, start=1):
            self.console.print(
                Panel(
                    answer["text"],
                    title=f"[yellow]{i}[/yellow]",
                    border_style="green",
                    padding=(0, 1)
                )
            )
        self.console.print()
        return int(self.console.input("[bold cyan]Ваш ответ: [/bold cyan]"))
    


    def success(self, text):
        self.console.print(f"[green]✓ {text}[/green]")
    
    def error(self, text):
        self.console.print(f"[bold red]✗ {text}[/bold red]")
    
    def pause(self):
        self.console.input("\n[dim]Нажмите Enter для продолжения...[/dim]")