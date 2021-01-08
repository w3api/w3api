---
title: MessageDigest.isEqual()
permalink: Java/MessageDigest/isEqual
date: 2021-01-04
key: JavaJava.M.MessageDigest
category: java
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
* **byte[] digesta**,  {% include w3api/param_description.html metodo=_data parametro="byte[] digesta" %}
* **byte[] digestb**,  {% include w3api/param_description.html metodo=_data parametro="byte[] digestb" %}

## Clase Padre
[MessageDigest](/Java/MessageDigest/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MessageDigest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
