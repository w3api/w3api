---
title: BasicGraphicsUtils.drawString()
permalink: Java/BasicGraphicsUtils/drawString
date: 2021-01-11
key: JavaJava.B.BasicGraphicsUtils
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicGraphicsUtils.metodos valor="drawString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void drawString(Graphics g, String text, int underlinedChar, int x, int y)
public static void drawString(JComponent c, Graphics2D g, String string, float x, float y)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}
* **Graphics2D g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics2D g" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **float y**,  {% include w3api/param_description.html metodo=_dato parametro="float y" %}
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **int underlinedChar**,  {% include w3api/param_description.html metodo=_dato parametro="int underlinedChar" %}
* **String string**,  {% include w3api/param_description.html metodo=_dato parametro="String string" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BasicGraphicsUtils](/Java/BasicGraphicsUtils/)

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
