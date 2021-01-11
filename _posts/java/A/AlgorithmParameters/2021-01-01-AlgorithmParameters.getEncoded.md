---
title: AlgorithmParameters.getEncoded()
permalink: Java/AlgorithmParameters/getEncoded
date: 2021-01-11
key: JavaJava.A.AlgorithmParameters
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmParameters.metodos valor="getEncoded" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final byte[] getEncoded() throws IOException
public final byte[] getEncoded(String format) throws IOException
~~~

## Parámetros
* **String format**,  {% include w3api/param_description.html metodo=_dato parametro="String format" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[AlgorithmParameters](/Java/AlgorithmParameters/)

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
