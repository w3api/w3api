---
title: CharsetEncoder.encode()
permalink: Java/CharsetEncoder/encode
date: 2021-01-04
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
* **ByteBuffer out**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer out" %}
* **boolean endOfInput**,  {% include w3api/param_description.html metodo=_data parametro="boolean endOfInput" %}
* **CharBuffer in**,  {% include w3api/param_description.html metodo=_data parametro="CharBuffer in" %}

## Excepciones
[MalformedInputException](/Java/MalformedInputException/), [IllegalStateException](/Java/IllegalStateException/), [UnmappableCharacterException](/Java/UnmappableCharacterException/), [CharacterCodingException](/Java/CharacterCodingException/)

## Clase Padre
[CharsetEncoder](/Java/CharsetEncoder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CharsetEncoder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
