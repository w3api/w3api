---
title: SecureRandom.next()
permalink: Java/SecureRandom/next
date: 2021-01-11
key: JavaJava.S.SecureRandom
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandom.metodos valor="next" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected int next(int numBits)
~~~

## Parámetros
* **int numBits**,  {% include w3api/param_description.html metodo=_dato parametro="int numBits" %}

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
