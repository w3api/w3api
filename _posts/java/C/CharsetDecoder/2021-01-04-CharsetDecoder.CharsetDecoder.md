---
title: CharsetDecoder.CharsetDecoder()
permalink: Java/CharsetDecoder/CharsetDecoder
date: 2021-01-04
key: JavaJava.C.CharsetDecoder
category: java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetDecoder.constructores valor="CharsetDecoder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CharsetDecoder(Charset cs, float averageCharsPerByte, float maxCharsPerByte)
~~~

## Parámetros
* **float averageCharsPerByte**,  {% include w3api/param_description.html metodo=_data parametro="float averageCharsPerByte" %}
* **float maxCharsPerByte**,  {% include w3api/param_description.html metodo=_data parametro="float maxCharsPerByte" %}
* **Charset cs**,  {% include w3api/param_description.html metodo=_data parametro="Charset cs" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CharsetDecoder](/Java/CharsetDecoder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CharsetDecoder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
