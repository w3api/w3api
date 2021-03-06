---
title: LineBreakMeasurer.deleteChar()
permalink: /Java/LineBreakMeasurer/deleteChar/
date: 2021-01-11
key: Java.L.LineBreakMeasurer
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LineBreakMeasurer.metodos valor="deleteChar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void deleteChar(AttributedCharacterIterator newParagraph, int deletePos)
~~~

## Parámetros
* **int deletePos**,  {% include w3api/param_description.html metodo=_dato parametro="int deletePos" %}
* **AttributedCharacterIterator newParagraph**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator newParagraph" %}

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
