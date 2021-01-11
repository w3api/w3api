---
title: BasicGraphicsUtils.drawBezel()
permalink: Java/BasicGraphicsUtils/drawBezel
date: 2021-01-11
key: JavaJava.B.BasicGraphicsUtils
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicGraphicsUtils.metodos valor="drawBezel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void drawBezel(Graphics g, int x, int y, int w, int h, boolean isPressed, boolean isDefault, Color shadow, Color darkShadow, Color highlight, Color lightHighlight)
~~~

## Parámetros
* **Color shadow**,  {% include w3api/param_description.html metodo=_dato parametro="Color shadow" %}
* **Color darkShadow**,  {% include w3api/param_description.html metodo=_dato parametro="Color darkShadow" %}
* **boolean isDefault**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isDefault" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **Color highlight**,  {% include w3api/param_description.html metodo=_dato parametro="Color highlight" %}
* **Color lightHighlight**,  {% include w3api/param_description.html metodo=_dato parametro="Color lightHighlight" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **boolean isPressed**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isPressed" %}

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
