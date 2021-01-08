---
title: PlainView.drawLine()
permalink: Java/PlainView/drawLine
date: 2021-01-04
key: JavaJava.P.PlainView
category: java
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
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **Graphics2D g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics2D g" %}
* **float y**,  {% include w3api/param_description.html metodo=_data parametro="float y" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int lineIndex**,  {% include w3api/param_description.html metodo=_data parametro="int lineIndex" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

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
