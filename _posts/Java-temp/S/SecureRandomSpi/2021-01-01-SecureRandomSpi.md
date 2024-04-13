---
title: SecureRandomSpi
permalink: /Java/SecureRandomSpi/
date: 2021-01-11
key: Java.S.SecureRandomSpi
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SecureRandomSpi.description }}

## Sintaxis
~~~java
public abstract class SecureRandomSpi extends Object implements Serializable
~~~

## Constructores
* [SecureRandomSpi()](/Java/SecureRandomSpi/SecureRandomSpi/)

## Métodos
* [engineGenerateSeed()](/Java/SecureRandomSpi/engineGenerateSeed)
* [engineGetParameters()](/Java/SecureRandomSpi/engineGetParameters)
* [engineNextBytes()](/Java/SecureRandomSpi/engineNextBytes)
* [engineReseed()](/Java/SecureRandomSpi/engineReseed)
* [engineSetSeed()](/Java/SecureRandomSpi/engineSetSeed)
* [toString()](/Java/SecureRandomSpi/toString)

## Ejemplo
~~~java
{{ site.data.Java.S.SecureRandomSpi.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureRandomSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
