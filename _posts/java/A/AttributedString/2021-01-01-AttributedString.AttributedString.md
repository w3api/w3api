---
title: AttributedString.AttributedString()
permalink: /Java/AttributedString/AttributedString/
date: 2021-01-11
key: Java.A.AttributedString
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributedString.constructores valor="AttributedString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AttributedString(String text)
public AttributedString(String text, Map<? extends AttributedCharacterIterator.Attribute,?> attributes)
public AttributedString(AttributedCharacterIterator text)
public AttributedString(AttributedCharacterIterator text, int beginIndex, int endIndex)
public AttributedString(AttributedCharacterIterator text, int beginIndex, int endIndex, AttributedCharacterIterator.Attribute[] attributes)
~~~

## Parámetros
* **Map&lt;? extends AttributedCharacterIterator.Attribute**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends AttributedCharacterIterator.Attribute" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator text" %}
* **?&gt; attributes**,  {% include w3api/param_description.html metodo=_dato parametro="?> attributes" %}
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int beginIndex" %}
* **AttributedCharacterIterator.Attribute[] attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator.Attribute[] attributes" %}
* **int endIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int endIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AttributedString](/Java/AttributedString/)

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
