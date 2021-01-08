---
title: PropertyResourceBundle.PropertyResourceBundle()
permalink: Java/PropertyResourceBundle/PropertyResourceBundle
date: 2021-01-04
key: JavaJava.P.PropertyResourceBundle
category: java
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
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_data parametro="Reader reader" %}

## Excepciones
[MalformedInputException](/Java/MalformedInputException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [UnmappableCharacterException](/Java/UnmappableCharacterException/), [IOException](/Java/IOException/)

## Clase Padre
[PropertyResourceBundle](/Java/PropertyResourceBundle/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyResourceBundle.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
