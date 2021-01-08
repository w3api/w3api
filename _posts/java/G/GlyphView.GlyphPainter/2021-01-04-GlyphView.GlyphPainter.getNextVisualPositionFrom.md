---
title: GlyphView.GlyphPainter.getNextVisualPositionFrom()
permalink: Java/GlyphView/GlyphPainter/getNextVisualPositionFrom
date: 2021-01-04
key: JavaJava.G.GlyphView.GlyphPainter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GlyphView.GlyphPainter.metodos valor="getNextVisualPositionFrom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getNextVisualPositionFrom(GlyphView v, int pos, Position.Bias b, Shape a, int direction, Position.Bias[] biasRet) throws BadLocationException
~~~

## Parámetros
* **Shape a**,  {% include w3api/param_description.html metodo=_data parametro="Shape a" %}
* **GlyphView v**,  {% include w3api/param_description.html metodo=_data parametro="GlyphView v" %}
* **Position.Bias b**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias b" %}
* **Position.Bias[] biasRet**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias[] biasRet" %}
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **int direction**,  {% include w3api/param_description.html metodo=_data parametro="int direction" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[GlyphView.GlyphPainter](/Java/GlyphView/GlyphPainter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GlyphView.GlyphPainter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
