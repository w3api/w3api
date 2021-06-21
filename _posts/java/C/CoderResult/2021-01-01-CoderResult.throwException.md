---
title: CoderResult.throwException()
permalink: /Java/CoderResult/throwException/
date: 2021-01-11
key: Java.C.CoderResult
category: Java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CoderResult.metodos valor="throwException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void throwException() throws CharacterCodingException
~~~

## Excepciones
[BufferOverflowException](/Java/BufferOverflowException/), [CharacterCodingException](/Java/CharacterCodingException/), [UnmappableCharacterException](/Java/UnmappableCharacterException/), [BufferUnderflowException](/Java/BufferUnderflowException/), [MalformedInputException](/Java/MalformedInputException/)

## Clase Padre
[CoderResult](/Java/CoderResult/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
