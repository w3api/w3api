---
title: ClassLoader.defineClass()
permalink: Java/ClassLoader/defineClass
date: 2021-01-04
key: JavaJava.C.ClassLoader
category: java
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
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **ProtectionDomain protectionDomain**,  {% include w3api/param_description.html metodo=_data parametro="ProtectionDomain protectionDomain" %}
* **ByteBuffer b**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer b" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[ClassLoader](/Java/ClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
