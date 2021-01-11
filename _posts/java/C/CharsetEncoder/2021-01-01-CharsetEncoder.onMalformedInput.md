---
title: CharsetEncoder.onMalformedInput()
permalink: Java/CharsetEncoder/onMalformedInput
date: 2021-01-11
key: JavaJava.C.CharsetEncoder
category: java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetEncoder.metodos valor="onMalformedInput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CharsetEncoder onMalformedInput(CodingErrorAction newAction)
~~~

## Parámetros
* **CodingErrorAction newAction**,  {% include w3api/param_description.html metodo=_dato parametro="CodingErrorAction newAction" %}

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