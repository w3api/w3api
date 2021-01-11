---
title: DefaultListCellRenderer.repaint()
permalink: Java/DefaultListCellRenderer/repaint
date: 2021-01-11
key: JavaJava.D.DefaultListCellRenderer
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultListCellRenderer.metodos valor="repaint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void repaint()
public void repaint(long tm, int x, int y, int width, int height)
public void repaint(Rectangle r)
~~~

## Parámetros
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **Rectangle r**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle r" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **long tm**,  {% include w3api/param_description.html metodo=_dato parametro="long tm" %}

## Clase Padre
[DefaultListCellRenderer](/Java/DefaultListCellRenderer/)

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
