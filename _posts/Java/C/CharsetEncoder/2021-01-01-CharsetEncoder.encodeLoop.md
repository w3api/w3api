---
title: CharsetEncoder.encodeLoop()
permalink: /Java/CharsetEncoder/encodeLoop/
date: 2021-01-11
key: Java.C.CharsetEncoder
category: Java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetEncoder.metodos valor="encodeLoop" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract CoderResult encodeLoop(CharBuffer in, ByteBuffer out)
~~~

## Parámetros
* **ByteBuffer out**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer out" %}
* **CharBuffer in**,  {% include w3api/param_description.html metodo=_dato parametro="CharBuffer in" %}

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
