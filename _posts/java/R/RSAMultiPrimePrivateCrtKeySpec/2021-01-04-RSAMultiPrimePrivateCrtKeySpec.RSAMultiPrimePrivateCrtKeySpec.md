---
title: RSAMultiPrimePrivateCrtKeySpec.RSAMultiPrimePrivateCrtKeySpec()
permalink: Java/RSAMultiPrimePrivateCrtKeySpec/RSAMultiPrimePrivateCrtKeySpec
date: 2021-01-04
key: JavaJava.R.RSAMultiPrimePrivateCrtKeySpec
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
* **BigInteger crtCoefficient**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger crtCoefficient" %}
* **BigInteger primeExponentQ**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger primeExponentQ" %}
* **BigInteger publicExponent**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger publicExponent" %}
* **BigInteger primeExponentP**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger primeExponentP" %}
* **BigInteger primeP**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger primeP" %}
* **BigInteger modulus**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger modulus" %}
* **BigInteger privateExponent**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger privateExponent" %}
* **BigInteger primeQ**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger primeQ" %}
* **RSAOtherPrimeInfo[] otherPrimeInfo**,  {% include w3api/param_description.html metodo=_data parametro="RSAOtherPrimeInfo[] otherPrimeInfo" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RSAMultiPrimePrivateCrtKeySpec](/Java/RSAMultiPrimePrivateCrtKeySpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RSAMultiPrimePrivateCrtKeySpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
