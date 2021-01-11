---
title: SwingUtilities.convertPoint()
permalink: Java/SwingUtilities/convertPoint
date: 2021-01-11
key: JavaJava.S.SwingUtilities
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwingUtilities.metodos valor="convertPoint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Point convertPoint(Component source, int x, int y, Component destination)
public static Point convertPoint(Component source, Point aPoint, Component destination)
~~~

## Parámetros
* **Component destination**,  {% include w3api/param_description.html metodo=_dato parametro="Component destination" %}
* **Point aPoint**,  {% include w3api/param_description.html metodo=_dato parametro="Point aPoint" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

## Clase Padre
[SwingUtilities](/Java/SwingUtilities/)

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
