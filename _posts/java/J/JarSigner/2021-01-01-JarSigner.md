---
title: JarSigner
permalink: Java/JarSigner
date: 2021-01-11
key: JavaJava.J.JarSigner
category: java
tags: ['java se', 'jdk.security.jarsigner', 'jdk.jartool', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JarSigner.description }}

## Sintaxis
~~~java
public final class JarSigner extends Object
~~~

## Métodos
* [getDigestAlgorithm()](/Java/JarSigner/getDigestAlgorithm)
* [getProperty()](/Java/JarSigner/getProperty)
* [getSignatureAlgorithm()](/Java/JarSigner/getSignatureAlgorithm)
* [getSignerName()](/Java/JarSigner/getSignerName)
* [getTsa()](/Java/JarSigner/getTsa)
* [sign()](/Java/JarSigner/sign)

## Ejemplo
~~~java
{{ site.data.Java.J.JarSigner.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JarSigner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
