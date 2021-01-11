---
title: SignatureMethod
permalink: Java/SignatureMethod
date: 2021-01-11
key: JavaJava.S.SignatureMethod
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SignatureMethod.description }}

## Sintaxis
~~~java
public interface SignatureMethod extends XMLStructure, AlgorithmMethod
~~~

## Campos
* [DSA_SHA1](/Java/SignatureMethod/DSA_SHA1)
* [HMAC_SHA1](/Java/SignatureMethod/HMAC_SHA1)
* [RSA_SHA1](/Java/SignatureMethod/RSA_SHA1)

## Métodos
* [getParameterSpec()](/Java/SignatureMethod/getParameterSpec)

## Ejemplo
~~~java
{{ site.data.Java.S.SignatureMethod.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SignatureMethod.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
