---
title: StringReader.skip()
permalink: Java/StringReader/skip
date: 2021-01-04
key: JavaJava.S.StringReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringReader.metodos valor="skip" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long skip(long ns) throws IOException
~~~

## Parámetros
* **long ns**,  {% include w3api/param_description.html metodo=_data parametro="long ns" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[StringReader](/Java/StringReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
