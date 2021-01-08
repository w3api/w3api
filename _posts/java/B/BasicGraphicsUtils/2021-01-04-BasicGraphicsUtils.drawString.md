---
title: BasicGraphicsUtils.drawString()
permalink: Java/BasicGraphicsUtils/drawString
date: 2021-01-04
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
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **Graphics2D g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics2D g" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **float y**,  {% include w3api/param_description.html metodo=_data parametro="float y" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **int underlinedChar**,  {% include w3api/param_description.html metodo=_data parametro="int underlinedChar" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_data parametro="JComponent c" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **String string**,  {% include w3api/param_description.html metodo=_data parametro="String string" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

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
{%- for _ldc in site.data.Java.B.BasicGraphicsUtils.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
