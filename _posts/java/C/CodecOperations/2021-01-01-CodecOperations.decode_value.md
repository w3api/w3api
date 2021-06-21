---
title: CodecOperations.decode_value()
permalink: /Java/CodecOperations/decode_value/
date: 2021-01-11
key: Java.C.CodecOperations
category: Java
tags: ['java se', 'org.omg.IOP', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CodecOperations.metodos valor="decode_value" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Any decode_value(byte[] data, TypeCode tc) throws FormatMismatch, TypeMismatch
~~~

## Parámetros
* **TypeCode tc**,  {% include w3api/param_description.html metodo=_dato parametro="TypeCode tc" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}

## Clase Padre
[CodecOperations](/Java/CodecOperations/)

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
