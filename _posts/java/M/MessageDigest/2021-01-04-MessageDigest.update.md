---
title: MessageDigest.update()
permalink: Java/MessageDigest/update
date: 2021-01-04
key: JavaJava.M.MessageDigest
category: java
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
* **ByteBuffer input**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer input" %}
* **byte[] input**,  {% include w3api/param_description.html metodo=_data parametro="byte[] input" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **byte input**,  {% include w3api/param_description.html metodo=_data parametro="byte input" %}

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
