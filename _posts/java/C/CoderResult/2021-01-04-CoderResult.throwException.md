---
title: CoderResult.throwException()
permalink: Java/CoderResult/throwException
date: 2021-01-04
key: JavaJava.C.CoderResult
category: java
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
[BufferOverflowException](/Java/BufferOverflowException/), [MalformedInputException](/Java/MalformedInputException/), [CharacterCodingException](/Java/CharacterCodingException/), [BufferUnderflowException](/Java/BufferUnderflowException/), [UnmappableCharacterException](/Java/UnmappableCharacterException/)

## Clase Padre
[CoderResult](/Java/CoderResult/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CoderResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
