---
title: ByteArrayOutputStream.write()
permalink: Java/ByteArrayOutputStream/write
date: 2021-01-04
key: JavaJava.B.ByteArrayOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteArrayOutputStream.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(byte[] b, int off, int len)
public void write(int b)
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}

## Clase Padre
[ByteArrayOutputStream](/Java/ByteArrayOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.ByteArrayOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
