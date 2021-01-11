---
title: TextMeasurer.deleteChar()
permalink: Java/TextMeasurer/deleteChar
date: 2021-01-11
key: JavaJava.T.TextMeasurer
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextMeasurer.metodos valor="deleteChar" %}

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
[TextMeasurer](/Java/TextMeasurer/)

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
