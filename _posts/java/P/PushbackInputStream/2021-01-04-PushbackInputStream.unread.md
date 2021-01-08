---
title: PushbackInputStream.unread()
permalink: Java/PushbackInputStream/unread
date: 2021-01-04
key: JavaJava.P.PushbackInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PushbackInputStream.metodos valor="unread" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void unread(byte[] b) throws IOException
public void unread(byte[] b, int off, int len) throws IOException
public void unread(int b) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[PushbackInputStream](/Java/PushbackInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PushbackInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
