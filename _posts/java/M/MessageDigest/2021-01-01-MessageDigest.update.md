---
title: MessageDigest.update()
permalink: Java/MessageDigest/update
date: 2021-01-11
key: JavaJava.M.MessageDigest
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageDigest.metodos valor="update" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void update(byte input)
public void update(byte[] input)
public void update(byte[] input, int offset, int len)
public final void update(ByteBuffer input)
~~~

## Parámetros
* **ByteBuffer input**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer input" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] input**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] input" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **byte input**,  {% include w3api/param_description.html metodo=_dato parametro="byte input" %}

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
