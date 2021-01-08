---
title: CodecOperations.decode_value()
permalink: Java/CodecOperations/decode_value
date: 2021-01-04
key: JavaJava.C.CodecOperations
category: java
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
* **byte[] data**,  {% include w3api/param_description.html metodo=_data parametro="byte[] data" %}
* **TypeCode tc**,  {% include w3api/param_description.html metodo=_data parametro="TypeCode tc" %}

## Clase Padre
[CodecOperations](/Java/CodecOperations/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CodecOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
