---
title: PKIXCertPathChecker
permalink: Java/PKIXCertPathChecker
date: 2021-01-11
key: JavaJava.P.PKIXCertPathChecker
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PKIXCertPathChecker.description }}

## Sintaxis
~~~java
public abstract class PKIXCertPathChecker extends Object implements CertPathChecker, Cloneable
~~~

## Constructores
* [PKIXCertPathChecker()](/Java/PKIXCertPathChecker/PKIXCertPathChecker/)

## Métodos
* [check()](/Java/PKIXCertPathChecker/check)
* [clone()](/Java/PKIXCertPathChecker/clone)
* [getSupportedExtensions()](/Java/PKIXCertPathChecker/getSupportedExtensions)
* [init()](/Java/PKIXCertPathChecker/init)
* [isForwardCheckingSupported()](/Java/PKIXCertPathChecker/isForwardCheckingSupported)

## Ejemplo
~~~java
{{ site.data.Java.P.PKIXCertPathChecker.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PKIXCertPathChecker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
