---
title: InputStream.skip()
permalink: /Java/InputStream-java-io/skip/
date: 2021-01-11
key: Java.I.InputStream-java-io
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputStream-java-io.metodos valor="skip" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long skip(long n) throws IOException
~~~

## Parámetros
* **long n**,  {% include w3api/param_description.html metodo=_dato parametro="long n" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[InputStream](/Java/InputStream-java-io/)

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
