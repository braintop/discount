import os
import sqlite3
from typing import List, Tuple

from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtWidgets import (
    QApplication,
    QCompleter,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app1 import JsonPlaceholderPostsCRUD


DB_PATH = os.path.join(os.path.dirname(__file__), "db.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            age INTEGER
        )
        """
    )
    conn.commit()
    conn.close()


def get_all_persons() -> List[Tuple[int, str, int]]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, first_name, age FROM persons ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows


def insert_person(first_name: str, age: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO persons (first_name, age) VALUES (?, ?)", (first_name, age)
    )
    conn.commit()
    conn.close()


def update_person(person_id: int, first_name: str, age: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE persons SET first_name = ?, age = ? WHERE id = ?",
        (first_name, age, person_id),
    )
    conn.commit()
    conn.close()


def delete_person(person_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM persons WHERE id = ?", (person_id,))
    conn.commit()
    conn.close()


class PersonsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persons CRUD - SQLite + PyQt")
        self.resize(700, 500)

        init_db()
        self._setup_ui()
        self.load_data()

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        # Search with autocomplete
        search_layout = QHBoxLayout()
        search_label = QLabel("Search by name:")
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Type a name...")
        self.search_completer = QCompleter()
        self.search_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.search_edit.setCompleter(self.search_completer)
        self.search_completer.activated.connect(self.on_search_selected)
        self.search_edit.textChanged.connect(self.on_search_text_changed)

        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_edit)
        main_layout.addLayout(search_layout)

        # Table of persons
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "First Name", "Age"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.cellClicked.connect(self.on_table_row_clicked)
        main_layout.addWidget(self.table)

        # Form for first_name and age
        form_layout = QHBoxLayout()

        self.first_name_edit = QLineEdit()
        self.first_name_edit.setPlaceholderText("First name")
        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText("Age (number)")

        form_layout.addWidget(QLabel("First name:"))
        form_layout.addWidget(self.first_name_edit)
        form_layout.addWidget(QLabel("Age:"))
        form_layout.addWidget(self.age_edit)

        main_layout.addLayout(form_layout)

        # Buttons
        buttons_layout = QHBoxLayout()

        self.add_btn = QPushButton("Add")
        self.update_btn = QPushButton("Update")
        self.delete_btn = QPushButton("Delete")
        self.refresh_btn = QPushButton("Refresh")
        self.load_json_btn = QPushButton("Load from JSONPlaceholder")

        self.add_btn.clicked.connect(self.on_add_clicked)
        self.update_btn.clicked.connect(self.on_update_clicked)
        self.delete_btn.clicked.connect(self.on_delete_clicked)
        self.refresh_btn.clicked.connect(self.load_data)
        self.load_json_btn.clicked.connect(self.on_load_json_clicked)

        buttons_layout.addWidget(self.add_btn)
        buttons_layout.addWidget(self.update_btn)
        buttons_layout.addWidget(self.delete_btn)
        buttons_layout.addWidget(self.refresh_btn)
        buttons_layout.addWidget(self.load_json_btn)

        main_layout.addLayout(buttons_layout)

    # ---------- Data handling ----------
    def load_data(self):
        persons = get_all_persons()
        self.table.setRowCount(len(persons))

        names_for_autocomplete = []

        for row_idx, (pid, name, age) in enumerate(persons):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(pid)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(name))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(age)))
            names_for_autocomplete.append(name)

        # Update completer model
        model = QStringListModel(sorted(set(names_for_autocomplete)))
        self.search_completer.setModel(model)

        self.table.resizeColumnsToContents()

    def get_selected_person_id(self) -> int:
        selected_items = self.table.selectedItems()
        if not selected_items:
            return -1
        row = selected_items[0].row()
        id_item = self.table.item(row, 0)
        return int(id_item.text())

    # ---------- Slots ----------
    def on_table_row_clicked(self, row: int, column: int):
        id_item = self.table.item(row, 0)
        name_item = self.table.item(row, 1)
        age_item = self.table.item(row, 2)
        if not id_item:
            return
        self.first_name_edit.setText(name_item.text())
        self.age_edit.setText(age_item.text())

    def on_add_clicked(self):
        name = self.first_name_edit.text().strip()
        age_text = self.age_edit.text().strip()

        if not name or not age_text:
            QMessageBox.warning(self, "Validation", "Please fill name and age.")
            return

        try:
            age = int(age_text)
        except ValueError:
            QMessageBox.warning(self, "Validation", "Age must be a number.")
            return

        insert_person(name, age)
        self.first_name_edit.clear()
        self.age_edit.clear()
        self.load_data()

    def on_update_clicked(self):
        person_id = self.get_selected_person_id()
        if person_id == -1:
            QMessageBox.information(self, "Selection", "Please select a row to update.")
            return

        name = self.first_name_edit.text().strip()
        age_text = self.age_edit.text().strip()

        if not name or not age_text:
            QMessageBox.warning(self, "Validation", "Please fill name and age.")
            return

        try:
            age = int(age_text)
        except ValueError:
            QMessageBox.warning(self, "Validation", "Age must be a number.")
            return

        update_person(person_id, name, age)
        self.load_data()

    def on_delete_clicked(self):
        person_id = self.get_selected_person_id()
        if person_id == -1:
            QMessageBox.information(self, "Selection", "Please select a row to delete.")
            return

        reply = QMessageBox.question(
            self,
            "Confirm delete",
            f"Delete person id {person_id}?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            delete_person(person_id)
            self.first_name_edit.clear()
            self.age_edit.clear()
            self.load_data()

    def on_load_json_clicked(self):
        """
        Load all posts from JSONPlaceholder into the local SQLite table,
        mapping:
        - title -> first_name
        - userId -> age
        """
        try:
            crud = JsonPlaceholderPostsCRUD()
            posts = crud.list_posts()
            if not posts:
                QMessageBox.information(
                    self,
                    "JSONPlaceholder",
                    "No posts received from JSONPlaceholder.",
                )
                return

            for p in posts:
                title = str(p.get("title", "")).strip()
                if not title:
                    continue
                name = title[:50]
                try:
                    age = int(p.get("userId", 0) or 0)
                except (TypeError, ValueError):
                    age = 0
                insert_person(name, age)

            self.load_data()
            QMessageBox.information(
                self,
                "JSONPlaceholder",
                f"Imported {len(posts)} posts into the persons table.",
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to load from JSONPlaceholder:\n{e}",
            )

    def on_search_selected(self, text: str):
        # When user picks from autocomplete, select the first matching row
        self.select_row_by_name(text)

    def on_search_text_changed(self, text: str):
        # Optional: live filter – here just try to select exact name when user presses Enter
        # (QCompleter itself already shows suggestions)
        # You can expand this to real-time filtering if תרצה.
        pass

    def select_row_by_name(self, name: str):
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 1)
            if item and item.text().lower() == name.lower():
                self.table.selectRow(row)
                self.table.scrollToItem(item)
                self.on_table_row_clicked(row, 1)
                break


def main():
    import sys

    app = QApplication(sys.argv)
    window = PersonsWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


