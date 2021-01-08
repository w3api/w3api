---
title: CryptoPrimitive.valueOf()
permalink: Java/CryptoPrimitive/valueOf
date: 2021-01-04
key: JavaJava.C.CryptoPrimitive
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CryptoPrimitive.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CryptoPrimitive valueOf(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CryptoPrimitive](/Java/CryptoPrimitive/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CryptoPrimitive.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
