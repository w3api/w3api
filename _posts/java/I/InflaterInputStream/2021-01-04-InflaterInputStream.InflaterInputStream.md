---
title: InflaterInputStream.InflaterInputStream()
permalink: Java/InflaterInputStream/InflaterInputStream
date: 2021-01-04
key: JavaJava.I.InflaterInputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InflaterInputStream.constructores valor="InflaterInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InflaterInputStream(InputStream in)
public InflaterInputStream(InputStream in, Inflater inf)
public InflaterInputStream(InputStream in, Inflater inf, int size)
~~~

## Parámetros
* **Inflater inf**,  {% include w3api/param_description.html metodo=_data parametro="Inflater inf" %}
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InflaterInputStream](/Java/InflaterInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InflaterInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
