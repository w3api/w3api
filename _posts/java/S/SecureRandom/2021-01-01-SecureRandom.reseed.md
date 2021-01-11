---
title: SecureRandom.reseed()
permalink: Java/SecureRandom/reseed
date: 2021-01-11
key: JavaJava.S.SecureRandom
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandom.metodos valor="reseed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void reseed()
public void reseed(SecureRandomParameters params)
~~~

## Parámetros
* **SecureRandomParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandomParameters params" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[SecureRandom](/Java/SecureRandom/)

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
