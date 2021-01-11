---
title: CharsetEncoder.encode()
permalink: Java/CharsetEncoder/encode
date: 2021-01-11
key: JavaJava.C.CharsetEncoder
category: java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetEncoder.metodos valor="encode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final ByteBuffer encode(CharBuffer in) throws CharacterCodingException
public final CoderResult encode(CharBuffer in, ByteBuffer out, boolean endOfInput)
~~~

## Parámetros
* **boolean endOfInput**,  {% include w3api/param_description.html metodo=_dato parametro="boolean endOfInput" %}
* **ByteBuffer out**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer out" %}
* **CharBuffer in**,  {% include w3api/param_description.html metodo=_dato parametro="CharBuffer in" %}

## Excepciones
[CharacterCodingException](/Java/CharacterCodingException/), [UnmappableCharacterException](/Java/UnmappableCharacterException/), [MalformedInputException](/Java/MalformedInputException/), [IllegalStateException](/Java/IllegalStateException/)

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
