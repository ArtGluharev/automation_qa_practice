import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite("Тестирование страницы Interactions")
class TestInteractionsPage:
    @allure.feature("Тестирование Sortable")
    class TestSortablePage:
        @allure.title("Тестирование сортировки")
        def test_sortable_page(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the grid has not been changed"

    @allure.feature("Тестирование Selectable")
    class TestSelectablePage:
        @allure.title("Тестирование выборочных")
        def test_selectable_page(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "No elements were selected"
            assert len(item_grid) > 0, "No elements were selected"

    @allure.feature("Тестирование Resizable")
    class TestResizablePage:
        @allure.title("Тестирование изменяемых в размере окон")
        def test_resizable_page(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box
            assert ('150px', '150px') == min_box
            assert min_resize != max_resize

    @allure.feature("Тестирование Droppable")
    class TestDroppablePage:
        @allure.title("Тестирование Simple droppable")
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            print(text)
            assert text == "Dropped!", "The element has not been dropped"

        @allure.title("Тестирование Accept droppable")
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            accept_text, not_accept_text = droppable_page.drop_accept()
            assert not_accept_text == "Drop here", "the dropped element has not been accepted"
            assert accept_text == "Dropped!", "the dropped element has been accepted"

        @allure.title("Тестирование prevent propogation droppable")
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == "Dropped!", "The elements texts has not been changed"
            assert not_greedy_inner == "Dropped!", "The elements texts has not been changed"
            assert greedy == "Outer droppable", "The elements texts has been changed"
            assert greedy_inner == "Dropped!", "The elements texts has not been changed"

        @allure.title("Тестирование Revert draggable")
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, "The elements has not reverted"
            assert not_will_after_move == not_will_after_revert, "The elements has reverted"

    @allure.feature("Тестирование страницы Draggable")
    class TestDraggablePage:
        @allure.title("Тестирование простого Draggable")
        def test_draggable_page(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "The position of the box has not been changed"

        @allure.title("Тестирование только по ося X или Y")
        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            draggable_page.axis_restricted_x()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0
