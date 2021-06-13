---
title: InflaterInputStream.skip()
permalink: /Java/InflaterInputStream/skip/
date: 2021-01-11
key: Java.I.InflaterInputStream
category: Java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InflaterInputStream.metodos valor="skip" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long skip(long n) throws IOException
~~~

## Parámetros
* **long n**,  {% include w3api/param_description.html metodo=_dato parametro="long n" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[InflaterInputStream](/Java/InflaterInputStream/)

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
