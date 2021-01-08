---
title: JScrollBar.JScrollBar()
permalink: Java/JScrollBar/JScrollBar
date: 2021-01-04
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
* **int orientation**,  {% include w3api/param_description.html metodo=_data parametro="int orientation" %}
* **int max**,  {% include w3api/param_description.html metodo=_data parametro="int max" %}
* **int value**,  {% include w3api/param_description.html metodo=_data parametro="int value" %}
* **int min**,  {% include w3api/param_description.html metodo=_data parametro="int min" %}
* **int extent**,  {% include w3api/param_description.html metodo=_data parametro="int extent" %}

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
{%- for _ldc in site.data.Java.J.JScrollBar.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
