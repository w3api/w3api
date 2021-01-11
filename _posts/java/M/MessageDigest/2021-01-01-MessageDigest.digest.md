---
title: MessageDigest.digest()
permalink: Java/MessageDigest/digest
date: 2021-01-11
key: JavaJava.M.MessageDigest
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageDigest.metodos valor="digest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public byte[] digest()
public byte[] digest(byte[] input)
public int digest(byte[] buf, int offset, int len) throws DigestException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] buf**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] buf" %}
* **byte[] input**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] input" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[DigestException](/Java/DigestException/)

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
