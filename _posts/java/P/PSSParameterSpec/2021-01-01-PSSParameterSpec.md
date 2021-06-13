---
title: PSSParameterSpec
permalink: /Java/PSSParameterSpec/
date: 2021-01-11
key: Java.P.PSSParameterSpec
category: java
tags: ['java se', 'java.security.spec', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PSSParameterSpec.description }}

## Sintaxis
~~~java
public class PSSParameterSpec extends Object implements AlgorithmParameterSpec
~~~

## Constructores
* [PSSParameterSpec()](/Java/PSSParameterSpec/PSSParameterSpec/)

## Campos
* [DEFAULT](/Java/PSSParameterSpec/DEFAULT)

## Métodos
* [getDigestAlgorithm()](/Java/PSSParameterSpec/getDigestAlgorithm)
* [getMGFAlgorithm()](/Java/PSSParameterSpec/getMGFAlgorithm)
* [getMGFParameters()](/Java/PSSParameterSpec/getMGFParameters)
* [getSaltLength()](/Java/PSSParameterSpec/getSaltLength)
* [getTrailerField()](/Java/PSSParameterSpec/getTrailerField)

## Ejemplo
~~~java
{{ site.data.Java.P.PSSParameterSpec.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PSSParameterSpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
