---
title: SecureClassLoader.defineClass()
permalink: Java/SecureClassLoader/defineClass
date: 2021-01-04
key: JavaJava.S.SecureClassLoader
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureClassLoader.metodos valor="defineClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Class<?> defineClass(String name, byte[] b, int off, int len, CodeSource cs)
protected Class<?> defineClass(String name, ByteBuffer b, CodeSource cs)
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **ByteBuffer b**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer b" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **CodeSource cs**,  {% include w3api/param_description.html metodo=_data parametro="CodeSource cs" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[SecureClassLoader](/Java/SecureClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
