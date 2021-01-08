---
title: SecureRandomSpi.engineNextBytes()
permalink: Java/SecureRandomSpi/engineNextBytes
date: 2021-01-04
key: JavaJava.S.SecureRandomSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandomSpi.metodos valor="engineNextBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineNextBytes(byte[] bytes)
protected void engineNextBytes(byte[] bytes, SecureRandomParameters params)
~~~

## Parámetros
* **byte[] bytes**,  {% include w3api/param_description.html metodo=_data parametro="byte[] bytes" %}
* **SecureRandomParameters params**,  {% include w3api/param_description.html metodo=_data parametro="SecureRandomParameters params" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SecureRandomSpi](/Java/SecureRandomSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureRandomSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
