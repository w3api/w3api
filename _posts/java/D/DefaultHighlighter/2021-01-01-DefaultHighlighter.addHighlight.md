---
title: DefaultHighlighter.addHighlight()
permalink: Java/DefaultHighlighter/addHighlight
date: 2021-01-11
key: JavaJava.D.DefaultHighlighter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultHighlighter.metodos valor="addHighlight" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object addHighlight(int p0, int p1, Highlighter.HighlightPainter p) throws BadLocationException
~~~

## Parámetros
* **Highlighter.HighlightPainter p**,  {% include w3api/param_description.html metodo=_dato parametro="Highlighter.HighlightPainter p" %}
* **int p1**,  {% include w3api/param_description.html metodo=_dato parametro="int p1" %}
* **int p0**,  {% include w3api/param_description.html metodo=_dato parametro="int p0" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[DefaultHighlighter](/Java/DefaultHighlighter/)

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