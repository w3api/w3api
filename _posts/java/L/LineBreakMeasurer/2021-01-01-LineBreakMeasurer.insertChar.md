---
title: LineBreakMeasurer.insertChar()
permalink: Java/LineBreakMeasurer/insertChar
date: 2021-01-11
key: JavaJava.L.LineBreakMeasurer
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LineBreakMeasurer.metodos valor="insertChar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insertChar(AttributedCharacterIterator newParagraph, int insertPos)
~~~

## Parámetros
* **AttributedCharacterIterator newParagraph**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator newParagraph" %}
* **int insertPos**,  {% include w3api/param_description.html metodo=_dato parametro="int insertPos" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

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
