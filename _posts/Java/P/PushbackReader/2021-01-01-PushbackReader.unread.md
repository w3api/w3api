---
title: PushbackReader.unread()
permalink: /Java/PushbackReader/unread/
date: 2021-01-11
key: Java.P.PushbackReader
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PushbackReader.metodos valor="unread" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void unread(char[] cbuf) throws IOException
public void unread(char[] cbuf, int off, int len) throws IOException
public void unread(int c) throws IOException
~~~

## Parámetros
* **int c**,  {% include w3api/param_description.html metodo=_dato parametro="int c" %}
* **char[] cbuf**,  {% include w3api/param_description.html metodo=_dato parametro="char[] cbuf" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[PushbackReader](/Java/PushbackReader/)

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
