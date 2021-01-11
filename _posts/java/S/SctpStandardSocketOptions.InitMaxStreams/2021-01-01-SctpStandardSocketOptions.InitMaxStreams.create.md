---
title: SctpStandardSocketOptions.InitMaxStreams.create()
permalink: Java/SctpStandardSocketOptions/InitMaxStreams/create
date: 2021-01-11
key: JavaJava.S.SctpStandardSocketOptions.InitMaxStreams
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpStandardSocketOptions.InitMaxStreams.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SctpStandardSocketOptions.InitMaxStreams create(int maxInStreams, int maxOutStreams)
~~~

## Parámetros
* **int maxInStreams**,  {% include w3api/param_description.html metodo=_dato parametro="int maxInStreams" %}
* **int maxOutStreams**,  {% include w3api/param_description.html metodo=_dato parametro="int maxOutStreams" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SctpStandardSocketOptions.InitMaxStreams](/Java/SctpStandardSocketOptions/InitMaxStreams/)

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
