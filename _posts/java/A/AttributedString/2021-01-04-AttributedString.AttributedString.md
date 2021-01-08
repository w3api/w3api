---
title: AttributedString.AttributedString()
permalink: Java/AttributedString/AttributedString
date: 2021-01-04
key: JavaJava.A.AttributedString
category: java
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
* **?&gt; attributes**,  {% include w3api/param_description.html metodo=_data parametro="?> attributes" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_data parametro="int beginIndex" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **int endIndex**,  {% include w3api/param_description.html metodo=_data parametro="int endIndex" %}
* **AttributedCharacterIterator.Attribute[] attributes**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator.Attribute[] attributes" %}
* **Map&lt;? extends AttributedCharacterIterator.Attribute**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends AttributedCharacterIterator.Attribute" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator text" %}

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
