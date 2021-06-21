---
title: ClassLoader.defineClass()
permalink: /Java/ClassLoader/defineClass/
date: 2021-01-11
key: Java.C.ClassLoader
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="defineClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Class<?> defineClass(byte[] b, int off, int len)
protected Class<?> defineClass(String name, byte[] b, int off, int len)
protected Class<?> defineClass(String name, byte[] b, int off, int len, ProtectionDomain protectionDomain)
protected Class<?> defineClass(String name, ByteBuffer b, ProtectionDomain protectionDomain)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **ProtectionDomain protectionDomain**,  {% include w3api/param_description.html metodo=_dato parametro="ProtectionDomain protectionDomain" %}
* **ByteBuffer b**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer b" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] b" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Clase Padre
[ClassLoader](/Java/ClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
