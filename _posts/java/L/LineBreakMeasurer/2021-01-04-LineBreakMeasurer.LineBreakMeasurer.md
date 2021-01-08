---
title: LineBreakMeasurer.LineBreakMeasurer()
permalink: Java/LineBreakMeasurer/LineBreakMeasurer
date: 2021-01-04
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
* **FontRenderContext frc**,  {% include w3api/param_description.html metodo=_data parametro="FontRenderContext frc" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator text" %}
* **BreakIterator breakIter**,  {% include w3api/param_description.html metodo=_data parametro="BreakIterator breakIter" %}

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
{%- for _ldc in site.data.Java.L.LineBreakMeasurer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
