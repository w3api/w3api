---
title: PropertyResourceBundle.PropertyResourceBundle()
permalink: /Java/PropertyResourceBundle/PropertyResourceBundle/
date: 2021-01-11
key: Java.P.PropertyResourceBundle
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyResourceBundle.constructores valor="PropertyResourceBundle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PropertyResourceBundle(InputStream stream) throws IOException
public PropertyResourceBundle(Reader reader) throws IOException
~~~

## Parámetros
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [UnmappableCharacterException](/Java/UnmappableCharacterException/), [MalformedInputException](/Java/MalformedInputException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PropertyResourceBundle](/Java/PropertyResourceBundle/)

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
