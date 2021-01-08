---
title: AttributedString.addAttribute()
permalink: Java/AttributedString/addAttribute
date: 2021-01-04
key: JavaJava.A.AttributedString
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributedString.metodos valor="addAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addAttribute(AttributedCharacterIterator.Attribute attribute, Object value)
public void addAttribute(AttributedCharacterIterator.Attribute attribute, Object value, int beginIndex, int endIndex)
~~~

## Parámetros
* **int endIndex**,  {% include w3api/param_description.html metodo=_data parametro="int endIndex" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_data parametro="int beginIndex" %}
* **AttributedCharacterIterator.Attribute attribute**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator.Attribute attribute" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AttributedString](/Java/AttributedString/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttributedString.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
