---
title: InflaterInputStream.InflaterInputStream()
permalink: /Java/InflaterInputStream/InflaterInputStream/
date: 2021-01-11
key: Java.I.InflaterInputStream
category: Java
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
* **InputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream in" %}
* **Inflater inf**,  {% include w3api/param_description.html metodo=_dato parametro="Inflater inf" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
