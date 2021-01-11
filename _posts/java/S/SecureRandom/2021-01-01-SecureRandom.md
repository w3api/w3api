---
title: SecureRandom
permalink: Java/SecureRandom
date: 2021-01-11
key: JavaJava.S.SecureRandom
category: java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SecureRandom.description }}

## Sintaxis
~~~java
public class SecureRandom extends Random
~~~

## Constructores
* [SecureRandom()](/Java/SecureRandom/SecureRandom/)

## Métodos
* [generateSeed()](/Java/SecureRandom/generateSeed)
* [getAlgorithm()](/Java/SecureRandom/getAlgorithm)
* [getInstance()](/Java/SecureRandom/getInstance)
* [getInstanceStrong()](/Java/SecureRandom/getInstanceStrong)
* [getParameters()](/Java/SecureRandom/getParameters)
* [getProvider()](/Java/SecureRandom/getProvider)
* [getSeed()](/Java/SecureRandom/getSeed)
* [next()](/Java/SecureRandom/next)
* [nextBytes()](/Java/SecureRandom/nextBytes)
* [reseed()](/Java/SecureRandom/reseed)
* [setSeed()](/Java/SecureRandom/setSeed)
* [toString()](/Java/SecureRandom/toString)

## Ejemplo
~~~java
{{ site.data.Java.S.SecureRandom.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureRandom.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
