---
title: CharsetDecoder.onUnmappableCharacter()
permalink: Java/CharsetDecoder/onUnmappableCharacter
date: 2021-01-11
key: JavaJava.C.CharsetDecoder
category: java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetDecoder.metodos valor="onUnmappableCharacter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CharsetDecoder onUnmappableCharacter(CodingErrorAction newAction)
~~~

## Parámetros
* **CodingErrorAction newAction**,  {% include w3api/param_description.html metodo=_dato parametro="CodingErrorAction newAction" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
