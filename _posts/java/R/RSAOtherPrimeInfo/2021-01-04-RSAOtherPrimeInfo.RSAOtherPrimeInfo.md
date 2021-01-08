---
title: RSAOtherPrimeInfo.RSAOtherPrimeInfo()
permalink: Java/RSAOtherPrimeInfo/RSAOtherPrimeInfo
date: 2021-01-04
key: JavaJava.R.RSAOtherPrimeInfo
category: java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RSAOtherPrimeInfo.constructores valor="RSAOtherPrimeInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RSAOtherPrimeInfo(BigInteger prime, BigInteger primeExponent, BigInteger crtCoefficient)
~~~

## Parámetros
* **BigInteger crtCoefficient**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger crtCoefficient" %}
* **BigInteger primeExponent**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger primeExponent" %}
* **BigInteger prime**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger prime" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[RSAOtherPrimeInfo](/Java/RSAOtherPrimeInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RSAOtherPrimeInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
