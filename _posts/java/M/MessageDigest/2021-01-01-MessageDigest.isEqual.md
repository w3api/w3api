---
title: MessageDigest.isEqual()
permalink: Java/MessageDigest/isEqual
date: 2021-01-11
key: JavaJava.M.MessageDigest
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageDigest.metodos valor="isEqual" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean isEqual(byte[] digesta, byte[] digestb)
~~~

## Parámetros
* **byte[] digestb**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] digestb" %}
* **byte[] digesta**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] digesta" %}

## Clase Padre
[MessageDigest](/Java/MessageDigest/)

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
