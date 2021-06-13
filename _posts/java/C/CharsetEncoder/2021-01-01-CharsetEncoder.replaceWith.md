---
title: CharsetEncoder.replaceWith()
permalink: /Java/CharsetEncoder/replaceWith/
date: 2021-01-11
key: Java.C.CharsetEncoder
category: Java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetEncoder.metodos valor="replaceWith" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CharsetEncoder replaceWith(byte[] newReplacement)
~~~

## Parámetros
* **byte[] newReplacement**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] newReplacement" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CharsetEncoder](/Java/CharsetEncoder/)

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
