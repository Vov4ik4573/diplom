#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *

html = """<html>
<body>
  <table border=1 width="80%" align="center">
    <tr>
      <th>Статика</th>
      <th>Кинематика</th>
      <th>Динамика</th>
    </tr>
    
    <tr>
      <td>
        <a href="http://localhost/diplom/intersection_forces.py">Задача на тему "Силы, линии действия которых пересекаются в одной точке"</a><br>
        <a href="http://localhost/diplom/parallel_forces.py">Задача на тему "Параллельные силы"</a><br>
        <a href="http://localhost/diplom/friction_forces.py">Задача на тему "Силы трения"</a><br>
        <a href="http://localhost/diplom/balance_forces.py">Задача на тему "Равновесие произвольной системы сил"</a><br>
      </td>      
      <td>
				<a href="http://localhost/diplom/pointspeed.py">Задача на тему "Скорость точки"</a><br>
        <a href="http://localhost/diplom/pointacceleration.py">Задача на тему "Ускорение точки"</a><br>
        <a href="http://localhost/diplom/addingspeeds.py">Задача на тему "Сложение скоростей"</a><br>
        <a href="http://localhost/diplom/addition_of_accelerations.py">Задача на тему "Сложение ускорений"</a><br>
        <a href="http://localhost/diplom/kinematic.py">Задача на тему "Общая задача"</a><br>
			</td>
      <td>
        <a href="http://localhost/diplom/dinamic1.py">Задача на тему "Определение сил по заданному движению"</a><br>
        <a href="http://localhost/diplom/oscillatory_motion.py">Задача на тему "Колебательное движение"</a><br>
        <a href="http://localhost/diplom/relative_motion.py">Задача на тему "Относительное движение"</a><br>
        <a href="http://localhost/diplom/geometry_of_masses.py">Задача на тему "Геометрия масс: центр масс материальной системы, моменты инерции твердых тел"</a><br>
        <a href="http://localhost/diplom/point_dynamics.py">Задача на тему "Динамика точки и системы переменной массы (переменного состава)"</a><br>
      </td>
    </tr>
  </table>
</body>
</html>"""

print(html)
