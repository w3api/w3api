---
title: LineBreakMeasurer.LineBreakMeasurer()
permalink: Java/LineBreakMeasurer/LineBreakMeasurer
date: 2021-01-11
key: JavaJava.L.LineBreakMeasurer
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LineBreakMeasurer.constructores valor="LineBreakMeasurer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LineBreakMeasurer(AttributedCharacterIterator text, FontRenderContext frc)
public LineBreakMeasurer(AttributedCharacterIterator text, BreakIterator breakIter, FontRenderContext frc)
~~~

## Parámetros
* **BreakIterator breakIter**,  {% include w3api/param_description.html metodo=_dato parametro="BreakIterator breakIter" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator text" %}
* **FontRenderContext frc**,  {% include w3api/param_description.html metodo=_dato parametro="FontRenderContext frc" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LineBreakMeasurer](/Java/LineBreakMeasurer/)

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
