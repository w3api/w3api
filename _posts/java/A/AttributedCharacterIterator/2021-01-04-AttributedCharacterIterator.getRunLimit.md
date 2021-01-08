---
title: AttributedCharacterIterator.getRunLimit()
permalink: Java/AttributedCharacterIterator/getRunLimit
date: 2021-01-04
key: JavaJava.A.AttributedCharacterIterator
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributedCharacterIterator.metodos valor="getRunLimit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int getRunLimit()
int getRunLimit(AttributedCharacterIterator.Attribute attribute)
int getRunLimit(Set<? extends AttributedCharacterIterator.Attribute> attributes)
~~~

## Parámetros
* **AttributedCharacterIterator.Attribute attribute**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator.Attribute attribute" %}
* **Set&lt;? extends AttributedCharacterIterator.Attribute&gt; attributes**,  {% include w3api/param_description.html metodo=_data parametro="Set<? extends AttributedCharacterIterator.Attribute> attributes" %}

## Clase Padre
[AttributedCharacterIterator](/Java/AttributedCharacterIterator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttributedCharacterIterator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
