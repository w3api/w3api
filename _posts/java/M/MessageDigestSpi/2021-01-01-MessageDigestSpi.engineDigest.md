---
title: MessageDigestSpi.engineDigest()
permalink: /Java/MessageDigestSpi/engineDigest/
date: 2021-01-11
key: Java.M.MessageDigestSpi
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageDigestSpi.metodos valor="engineDigest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract byte[] engineDigest()
protected int engineDigest(byte[] buf, int offset, int len) throws DigestException
~~~

## Parámetros
* **byte[] buf**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] buf" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[DigestException](/Java/DigestException/)

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
