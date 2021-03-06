---
title: PlainView.drawLine()
permalink: /Java/PlainView/drawLine/
date: 2021-01-11
key: Java.P.PlainView
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PlainView.metodos valor="drawLine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void drawLine(int lineIndex, Graphics2D g, float x, float y)
@Deprecated(since="9") protected void drawLine(int lineIndex, Graphics g, int x, int y)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **int lineIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int lineIndex" %}
* **Graphics2D g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics2D g" %}
* **float y**,  {% include w3api/param_description.html metodo=_dato parametro="float y" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}

## Clase Padre
[PlainView](/Java/PlainView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
