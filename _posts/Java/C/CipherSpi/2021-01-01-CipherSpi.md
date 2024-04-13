---
title: CipherSpi
permalink: /Java/CipherSpi/
date: 2021-01-11
key: Java.C.CipherSpi
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CipherSpi.description }}

## Sintaxis
~~~java
public abstract class CipherSpi extends Object
~~~

## Constructores
* [CipherSpi()](/Java/CipherSpi/CipherSpi/)

## Métodos
* [engineDoFinal()](/Java/CipherSpi/engineDoFinal/)
* [engineGetBlockSize()](/Java/CipherSpi/engineGetBlockSize/)
* [engineGetIV()](/Java/CipherSpi/engineGetIV/)
* [engineGetKeySize()](/Java/CipherSpi/engineGetKeySize/)
* [engineGetOutputSize()](/Java/CipherSpi/engineGetOutputSize/)
* [engineGetParameters()](/Java/CipherSpi/engineGetParameters/)
* [engineInit()](/Java/CipherSpi/engineInit/)
* [engineSetMode()](/Java/CipherSpi/engineSetMode/)
* [engineSetPadding()](/Java/CipherSpi/engineSetPadding/)
* [engineUnwrap()](/Java/CipherSpi/engineUnwrap/)
* [engineUpdate()](/Java/CipherSpi/engineUpdate/)
* [engineUpdateAAD()](/Java/CipherSpi/engineUpdateAAD/)
* [engineWrap()](/Java/CipherSpi/engineWrap/)

## Ejemplo
~~~java
{{ site.data.Java.C.CipherSpi.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CipherSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
