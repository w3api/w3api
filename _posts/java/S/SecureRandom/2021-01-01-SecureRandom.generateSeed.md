---
title: SecureRandom.generateSeed()
permalink: /Java/SecureRandom/generateSeed/
date: 2021-01-11
key: Java.S.SecureRandom
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandom.metodos valor="generateSeed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public byte[] generateSeed(int numBytes)
~~~

## Parámetros
* **int numBytes**,  {% include w3api/param_description.html metodo=_dato parametro="int numBytes" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
