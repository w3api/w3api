---
title: GlyphView.GlyphPainter.getNextVisualPositionFrom()
permalink: /Java/GlyphView/GlyphPainter/getNextVisualPositionFrom/
date: 2021-01-11
key: Java.G.GlyphView.GlyphPainter
category: Java
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
* **Shape a**,  {% include w3api/param_description.html metodo=_dato parametro="Shape a" %}
* **Position.Bias[] biasRet**,  {% include w3api/param_description.html metodo=_dato parametro="Position.Bias[] biasRet" %}
* **int direction**,  {% include w3api/param_description.html metodo=_dato parametro="int direction" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}
* **Position.Bias b**,  {% include w3api/param_description.html metodo=_dato parametro="Position.Bias b" %}
* **GlyphView v**,  {% include w3api/param_description.html metodo=_dato parametro="GlyphView v" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
