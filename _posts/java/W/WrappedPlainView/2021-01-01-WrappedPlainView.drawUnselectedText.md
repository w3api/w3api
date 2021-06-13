---
title: WrappedPlainView.drawUnselectedText()
permalink: /Java/WrappedPlainView/drawUnselectedText/
date: 2021-01-11
key: Java.W.WrappedPlainView
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WrappedPlainView.metodos valor="drawUnselectedText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected float drawUnselectedText(Graphics2D g, float x, float y, int p0, int p1) throws BadLocationException
@Deprecated(since="9") protected int drawUnselectedText(Graphics g, int x, int y, int p0, int p1) throws BadLocationException
~~~

## Parámetros
* **int p1**,  {% include w3api/param_description.html metodo=_dato parametro="int p1" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **int p0**,  {% include w3api/param_description.html metodo=_dato parametro="int p0" %}
* **Graphics2D g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics2D g" %}
* **float y**,  {% include w3api/param_description.html metodo=_dato parametro="float y" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[WrappedPlainView](/Java/WrappedPlainView/)

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
