---
title: MessageDigestSpi.engineUpdate()
permalink: Java/MessageDigestSpi/engineUpdate
date: 2021-01-04
key: JavaJava.M.MessageDigestSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageDigestSpi.metodos valor="engineUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineUpdate(byte input)
protected abstract void engineUpdate(byte[] input, int offset, int len)
protected void engineUpdate(ByteBuffer input)
~~~

## Parámetros
* **ByteBuffer input**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer input" %}
* **byte[] input**,  {% include w3api/param_description.html metodo=_data parametro="byte[] input" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **byte input**,  {% include w3api/param_description.html metodo=_data parametro="byte input" %}

## Clase Padre
[MessageDigestSpi](/Java/MessageDigestSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MessageDigestSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
