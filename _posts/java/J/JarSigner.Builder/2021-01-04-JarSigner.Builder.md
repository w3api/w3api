---
title: JarSigner.Builder
permalink: Java/JarSigner/Builder
date: 2021-01-04
key: JavaJava.J.JarSigner.Builder
category: java
tags: ['java se', 'jdk.security.jarsigner', 'jdk.jartool', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JarSigner.Builder.description }}

## Sintaxis
~~~java
public static class JarSigner.Builder extends Object
~~~

## Constructores
* [JarSigner.Builder()](/Java/JarSigner/Builder/JarSigner/Builder/)

## Métodos
* [build()](/Java/JarSigner/Builder/build)
* [digestAlgorithm()](/Java/JarSigner/Builder/digestAlgorithm)
* [eventHandler()](/Java/JarSigner/Builder/eventHandler)
* [getDefaultDigestAlgorithm()](/Java/JarSigner/Builder/getDefaultDigestAlgorithm)
* [getDefaultSignatureAlgorithm()](/Java/JarSigner/Builder/getDefaultSignatureAlgorithm)
* [setProperty()](/Java/JarSigner/Builder/setProperty)
* [signatureAlgorithm()](/Java/JarSigner/Builder/signatureAlgorithm)
* [signerName()](/Java/JarSigner/Builder/signerName)
* [tsa()](/Java/JarSigner/Builder/tsa)

## Ejemplo
~~~java
{{ site.data.Java.J.JarSigner.Builder.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JarSigner.Builder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
