---
title: CodecOperations.encode_value()
permalink: /Java/CodecOperations/encode_value/
date: 2021-01-11
key: Java.C.CodecOperations
category: Java
tags: ['java se', 'org.omg.IOP', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CodecOperations.metodos valor="encode_value" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
byte[] encode_value(Any data) throws InvalidTypeForEncoding
~~~

## Parámetros
* **Any data**,  {% include w3api/param_description.html metodo=_dato parametro="Any data" %}

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
