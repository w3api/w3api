---
title: RSAMultiPrimePrivateCrtKeySpec.RSAMultiPrimePrivateCrtKeySpec()
permalink: Java/RSAMultiPrimePrivateCrtKeySpec/RSAMultiPrimePrivateCrtKeySpec
date: 2021-01-11
key: Java.R.RSAMultiPrimePrivateCrtKeySpec
category: java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RSAMultiPrimePrivateCrtKeySpec.constructores valor="RSAMultiPrimePrivateCrtKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RSAMultiPrimePrivateCrtKeySpec(BigInteger modulus, BigInteger publicExponent, BigInteger privateExponent, BigInteger primeP, BigInteger primeQ, BigInteger primeExponentP, BigInteger primeExponentQ, BigInteger crtCoefficient, RSAOtherPrimeInfo[] otherPrimeInfo)
~~~

## Parámetros
* **BigInteger primeQ**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger primeQ" %}
* **BigInteger crtCoefficient**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger crtCoefficient" %}
* **BigInteger modulus**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger modulus" %}
* **BigInteger publicExponent**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger publicExponent" %}
* **BigInteger primeExponentQ**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger primeExponentQ" %}
* **BigInteger primeP**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger primeP" %}
* **BigInteger primeExponentP**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger primeExponentP" %}
* **RSAOtherPrimeInfo[] otherPrimeInfo**,  {% include w3api/param_description.html metodo=_dato parametro="RSAOtherPrimeInfo[] otherPrimeInfo" %}
* **BigInteger privateExponent**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger privateExponent" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[RSAMultiPrimePrivateCrtKeySpec](/Java/RSAMultiPrimePrivateCrtKeySpec/)

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
