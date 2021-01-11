---
title: JScrollBar.JScrollBar()
permalink: Java/JScrollBar/JScrollBar
date: 2021-01-11
key: JavaJava.J.JScrollBar
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JScrollBar.constructores valor="JScrollBar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JScrollBar()
public JScrollBar(int orientation)
public JScrollBar(int orientation, int value, int extent, int min, int max)
~~~

## Parámetros
* **int value**,  {% include w3api/param_description.html metodo=_dato parametro="int value" %}
* **int extent**,  {% include w3api/param_description.html metodo=_dato parametro="int extent" %}
* **int orientation**,  {% include w3api/param_description.html metodo=_dato parametro="int orientation" %}
* **int max**,  {% include w3api/param_description.html metodo=_dato parametro="int max" %}
* **int min**,  {% include w3api/param_description.html metodo=_dato parametro="int min" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JScrollBar](/Java/JScrollBar/)

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
