---
title: ByteArrayInputStream.ByteArrayInputStream()
permalink: Java/ByteArrayInputStream/ByteArrayInputStream
date: 2021-01-04
key: JavaJava.B.ByteArrayInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteArrayInputStream.constructores valor="ByteArrayInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ByteArrayInputStream(byte[] buf)
public ByteArrayInputStream(byte[] buf, int offset, int length)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **byte[] buf**,  {% include w3api/param_description.html metodo=_data parametro="byte[] buf" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Clase Padre
[ByteArrayInputStream](/Java/ByteArrayInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.ByteArrayInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
