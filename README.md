# ML
<p>There are 2 files, that are used in our project. They are: <b>main.py</b> and <b>hum_rob.py</b>. The first file is designed to be played by two people, the second - by human and robot.</p>
<ul>Basic conditions:</ul>
<li>The player_1 is indicated by the symbol "X"</li>
<li>The player_2 is indicated by the symbol "O"</li>
<li>Human is always the "X" and robot is the "O"</li>
<li>The current state of the playing field is saved in the array <b>game_board</b></li>
<li>For convenience, abbreviations are used, where s is small, b is big. Thus, the code looks like this: b4s7 (move to the small cell 7 in the field with index 4)</li>
<h2>main.py</h2>
<p>The file consists of 2 functions: <b>game</b> and <b>victory</b>.</p> 
<ul>The <b>game</b> function accepts 4 parameters as input:</ul>
<li><b>player</b></li>
<li><b>board</b></li>
<li><b>counter</b></li>
<li><b>last_move</b></li>
<br>This function is designed to handle player's actions. It returns new <b>board</b>, <b>counter</b>, <b>last_move</b>, <b>previous_move</b>.
<p><ul>The <b>victory</b> function accepts 3 parameters as input:</ul></p>
<li><b>player</b></li>
<li><b>board</b></li>
<li><b>previous_move</b></li>
<br>This function is used to check the move for a victory condition. It returns <b>True</b>, if the last move was victorious, and returns <b>False</b>, if it wasn't.
<br><thead>Here is a table of variables with their descriptions</thead>
<table>
  <tr><td><b>param</b></td><td><b>descrription</b></td><td><b>type</b></td></tr>
  <tr><td>player</td><td>which player's move are we considering</td><td>str ('X', 'O')</td></tr>
  <tr><td>board</td><td>the current state of the playing field</td><td>array</td></tr>
  <tr><td>counter</td><td>counter for the number of moves</td><td>int</td></tr>
  <tr><td>last_move</td><td>the ordinal number of the cell that the opponent was in during the last move</td><td>int</td></tr>
  <tr><td>previous_move</td><td>the ordinal number of the cell that the player made a move to during the last move</td><td>int</td></tr>
</table>
<p>To run the code, just enter the number of the cell to which you want to make a move.</p>
<h3>hum_rob.py</h3>
<p>The file consists of 4 functions: <b>game</b>, <b>victory</b>, <b>minimax</b> and <b>optimal_move</b>.</p>
<p><ul>The <b>game</b> function accepts 4 parameters as input:</ul></p>
<li><b>player</b></li>
<li><b>board</b></li>
<li><b>counter</b></li>
<li><b>last_move</b></li>
<br>This function is designed to handle human actions. It returns <b>board</b>, <b>counter</b>, <b>last_move</b> and <b>previous_move</b>.
<p><ul>The <b>victory</b> function accepts 3 parameters as input:</ul></p>
<li><b>player</b></li>
<li><b>board</b></li>
<li><b>previous_move</b></li>
<br>This function is used to check the move for a victory condition. It returns <b>True</b>, if the last move was victorious, and returns <b>False</b>, if it wasn't.
<p><ul>The <b>minimax</b> function accepts 4 parameters as input:</ul></p>
<li><b>board</b></li>
<li><b>is_maximizing</b></li>
<li><b>depth</b></li>
<li><b>prev</b></li>
<br>This function is used to evaluate moves for a robot. It returns <b>best_score</b>.
<p><ul>The <b>optimal_move</b> function accepts 3 parameters as input:</ul></p>
<li><b>board</b></li>
<li><b>depth</b></li>
<li><b>prev</b></li>
<br>This function is used to select the best action for the robot. It returns <b>best_move</b>.
<p>To understand what each variable is responsible for, I made a table</p>
<table>
  <tr><td>param</td><td>descrription</td><td>type</td></tr>
  <tr><td>player</td><td>which player's move are we considering</td><td>str ('X','O')</td></tr>
  <tr><td>board</td><td>the current state of the playing field</td><td>array</td></tr>
  <tr><td>counter</td><td>counter for the number of moves</td><td>int</td></tr>
  <tr><td>last_move</td><td>the ordinal number of the cell that the opponent was in during the last move</td><td>int</td></tr>
  <tr><td>previous_move</td><td>the ordinal number of the cell that the player made a move to during the last move</td><td>int</td></tr>
  <tr><td>is_maximizing</td><td>provided that the move in question is made by a human, then among the following values it is necessary to look for the maximum and vice versa</td><td>bool</td></tr>
  <tr><td>depth</td><td>you can use this parameter to adjust the complexity of the model. The greater the depth, the more moves the robot calculates in advance, the more difficult it is to play against it</td><td>int</td></tr>
  <tr><td>prev</td><td>is the same as previous_move, but it used in functions minimax and optimal_move</td><td>int</td></tr>
</table>
<p>To run the code, just enter the number of the cell to which you want to make a move.</p>
