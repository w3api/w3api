---
title: RSAPrivateKeySpec.RSAPrivateKeySpec()
permalink: Java/RSAPrivateKeySpec/RSAPrivateKeySpec
date: 2021-01-11
key: Java.R.RSAPrivateKeySpec
category: java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RSAPrivateKeySpec.constructores valor="RSAPrivateKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RSAPrivateKeySpec(BigInteger modulus, BigInteger privateExponent)
~~~

## Parámetros
* **BigInteger privateExponent**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger privateExponent" %}
* **BigInteger modulus**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger modulus" %}

## Clase Padre
[RSAPrivateKeySpec](/Java/RSAPrivateKeySpec/)

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
