---
title: KeyPairGenerator
permalink: Java/KeyPairGenerator
date: 2021-01-11
key: JavaJava.K.KeyPairGenerator
category: java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.K.KeyPairGenerator.description }}

## Sintaxis
~~~java
public abstract class KeyPairGenerator extends KeyPairGeneratorSpi
~~~

## Constructores
* [KeyPairGenerator()](/Java/KeyPairGenerator/KeyPairGenerator/)

## Métodos
* [generateKeyPair()](/Java/KeyPairGenerator/generateKeyPair)
* [genKeyPair()](/Java/KeyPairGenerator/genKeyPair)
* [getAlgorithm()](/Java/KeyPairGenerator/getAlgorithm)
* [getInstance()](/Java/KeyPairGenerator/getInstance)
* [getProvider()](/Java/KeyPairGenerator/getProvider)
* [initialize()](/Java/KeyPairGenerator/initialize)

## Ejemplo
~~~java
{{ site.data.Java.K.KeyPairGenerator.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyPairGenerator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
