---
title: GlyphView.GlyphPainter.modelToView()
permalink: Java/GlyphView/GlyphPainter/modelToView
date: 2021-01-04
key: JavaJava.G.GlyphView.GlyphPainter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GlyphView.GlyphPainter.metodos valor="modelToView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Shape modelToView(GlyphView v, int pos, Position.Bias bias, Shape a) throws BadLocationException
~~~

## Parámetros
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **GlyphView v**,  {% include w3api/param_description.html metodo=_data parametro="GlyphView v" %}
* **Shape a**,  {% include w3api/param_description.html metodo=_data parametro="Shape a" %}
* **Position.Bias bias**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias bias" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

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
