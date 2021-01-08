---
title: SecureRandom.nextBytes()
permalink: Java/SecureRandom/nextBytes
date: 2021-01-04
key: JavaJava.S.SecureRandom
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandom.metodos valor="nextBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void nextBytes(byte[] bytes)
public void nextBytes(byte[] bytes, SecureRandomParameters params)
~~~

## Parámetros
* **byte[] bytes**,  {% include w3api/param_description.html metodo=_data parametro="byte[] bytes" %}
* **SecureRandomParameters params**,  {% include w3api/param_description.html metodo=_data parametro="SecureRandomParameters params" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SecureRandom](/Java/SecureRandom/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureRandom.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
