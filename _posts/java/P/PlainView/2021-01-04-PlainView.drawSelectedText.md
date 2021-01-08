---
title: PlainView.drawSelectedText()
permalink: Java/PlainView/drawSelectedText
date: 2021-01-04
key: JavaJava.P.PlainView
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PlainView.metodos valor="drawSelectedText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected float drawSelectedText(Graphics2D g, float x, float y, int p0, int p1) throws BadLocationException
@Deprecated(since="9") protected int drawSelectedText(Graphics g, int x, int y, int p0, int p1) throws BadLocationException
~~~

## Parámetros
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **Graphics2D g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics2D g" %}
* **float y**,  {% include w3api/param_description.html metodo=_data parametro="float y" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **int p1**,  {% include w3api/param_description.html metodo=_data parametro="int p1" %}
* **int p0**,  {% include w3api/param_description.html metodo=_data parametro="int p0" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[PlainView](/Java/PlainView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PlainView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
