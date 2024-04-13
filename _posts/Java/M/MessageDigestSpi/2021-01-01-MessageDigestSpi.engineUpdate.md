---
title: MessageDigestSpi.engineUpdate()
permalink: /Java/MessageDigestSpi/engineUpdate/
date: 2021-01-11
key: Java.M.MessageDigestSpi
category: Java
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
* **ByteBuffer input**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer input" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] input**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] input" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **byte input**,  {% include w3api/param_description.html metodo=_dato parametro="byte input" %}

## Clase Padre
[MessageDigestSpi](/Java/MessageDigestSpi/)

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
