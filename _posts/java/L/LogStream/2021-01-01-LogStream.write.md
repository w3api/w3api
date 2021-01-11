---
title: LogStream.write()
permalink: Java/LogStream/write
date: 2021-01-11
key: JavaJava.L.LogStream
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LogStream.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public void write(byte[] b, int off, int len)
@Deprecated public void write(int b)
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] b" %}

## Clase Padre
[LogStream](/Java/LogStream/)

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
