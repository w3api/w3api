---
title: CharsetDecoder.decode()
permalink: Java/CharsetDecoder/decode
date: 2021-01-04
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
* **ByteBuffer in**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer in" %}
* **boolean endOfInput**,  {% include w3api/param_description.html metodo=_data parametro="boolean endOfInput" %}
* **CharBuffer out**,  {% include w3api/param_description.html metodo=_data parametro="CharBuffer out" %}

## Excepciones
[MalformedInputException](/Java/MalformedInputException/), [IllegalStateException](/Java/IllegalStateException/), [UnmappableCharacterException](/Java/UnmappableCharacterException/), [CharacterCodingException](/Java/CharacterCodingException/)

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
