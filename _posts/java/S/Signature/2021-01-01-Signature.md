---
title: Signature
permalink: /Java/Signature/
date: 2021-01-11
key: Java.S.Signature
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.Signature.description }}

## Sintaxis
~~~java
public abstract class Signature extends SignatureSpi
~~~

## Constructores
* [Signature()](/Java/Signature/Signature/)

## Campos
* [SIGN](/Java/Signature/SIGN)
* [state](/Java/Signature/state)
* [UNINITIALIZED](/Java/Signature/UNINITIALIZED)
* [VERIFY](/Java/Signature/VERIFY)

## Métodos
* [clone()](/Java/Signature/clone)
* [getAlgorithm()](/Java/Signature/getAlgorithm)
* [getInstance()](/Java/Signature/getInstance)
* [getParameter()](/Java/Signature/getParameter)
* [getParameters()](/Java/Signature/getParameters)
* [getProvider()](/Java/Signature/getProvider)
* [initSign()](/Java/Signature/initSign)
* [initVerify()](/Java/Signature/initVerify)
* [setParameter()](/Java/Signature/setParameter)
* [sign()](/Java/Signature/sign)
* [toString()](/Java/Signature/toString)
* [update()](/Java/Signature/update)
* [verify()](/Java/Signature/verify)

## Ejemplo
~~~java
{{ site.data.Java.S.Signature.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Signature.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
