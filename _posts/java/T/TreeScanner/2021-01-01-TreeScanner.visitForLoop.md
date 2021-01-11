---
title: TreeScanner.visitForLoop()
permalink: Java/TreeScanner/visitForLoop
date: 2021-01-11
key: JavaJava.T.TreeScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeScanner.metodos valor="visitForLoop" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitForLoop(ForLoopTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **ForLoopTree node**,  {% include w3api/param_description.html metodo=_dato parametro="ForLoopTree node" %}

## Clase Padre
[TreeScanner](/Java/TreeScanner/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
