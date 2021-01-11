---
title: CharsetDecoder.decode()
permalink: Java/CharsetDecoder/decode
date: 2021-01-11
key: JavaJava.C.CharsetDecoder
category: java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetDecoder.metodos valor="decode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CharBuffer decode(ByteBuffer in) throws CharacterCodingException
public final CoderResult decode(ByteBuffer in, CharBuffer out, boolean endOfInput)
~~~

## Parámetros
* **boolean endOfInput**,  {% include w3api/param_description.html metodo=_dato parametro="boolean endOfInput" %}
* **ByteBuffer in**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer in" %}
* **CharBuffer out**,  {% include w3api/param_description.html metodo=_dato parametro="CharBuffer out" %}

## Excepciones
[CharacterCodingException](/Java/CharacterCodingException/), [UnmappableCharacterException](/Java/UnmappableCharacterException/), [MalformedInputException](/Java/MalformedInputException/), [IllegalStateException](/Java/IllegalStateException/)

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
