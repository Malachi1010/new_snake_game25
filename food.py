<html>
<head>
<title>food.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #6aab73;}
.s4 { color: #2aacb8;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
food.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">turtle </span><span class="s0">import </span><span class="s1">Turtle</span>
<span class="s0">import </span><span class="s1">random</span>

<span class="s0">class </span><span class="s1">Food</span><span class="s2">(</span><span class="s1">Turtle</span><span class="s2">):</span>

    <span class="s0">def </span><span class="s1">__init__</span><span class="s2">(</span><span class="s1">self</span><span class="s2">):</span>
        <span class="s1">super</span><span class="s2">().</span><span class="s1">__init__</span><span class="s2">()</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">shape</span><span class="s2">(</span><span class="s3">&quot;circle&quot;</span><span class="s2">)</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">penup</span><span class="s2">()</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">shapesize</span><span class="s2">(</span><span class="s4">0.5</span><span class="s2">, </span><span class="s4">0.5</span><span class="s2">)</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">color</span><span class="s2">(</span><span class="s3">&quot;red&quot;</span><span class="s2">)</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">speed</span><span class="s2">(</span><span class="s4">10</span><span class="s2">)</span>



    <span class="s0">def </span><span class="s1">refresh</span><span class="s2">(</span><span class="s1">self</span><span class="s2">):</span>
        <span class="s1">random_x </span><span class="s2">= </span><span class="s1">random</span><span class="s2">.</span><span class="s1">randint</span><span class="s2">(-</span><span class="s4">280</span><span class="s2">, </span><span class="s4">280</span><span class="s2">)</span>
        <span class="s1">random_y </span><span class="s2">= </span><span class="s1">random</span><span class="s2">.</span><span class="s1">randint</span><span class="s2">(-</span><span class="s4">280</span><span class="s2">, </span><span class="s4">280</span><span class="s2">)</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">goto</span><span class="s2">(</span><span class="s1">random_x</span><span class="s2">, </span><span class="s1">random_y</span><span class="s2">)</span></pre>
</body>
</html>