---
title: AlgorithmParametersSpi.engineGetEncoded()
permalink: Java/AlgorithmParametersSpi/engineGetEncoded
date: 2021-01-10
key: JavaJava.A.AlgorithmParametersSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmParametersSpi.metodos valor="engineGetEncoded" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract byte[] engineGetEncoded() throws IOException
protected abstract byte[] engineGetEncoded(String format) throws IOException
~~~

## Parámetros
* **String format**,  {% include w3api/param_description.html metodo=_dato parametro="String format" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[AlgorithmParametersSpi](/Java/AlgorithmParametersSpi/)

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
