---
title: CryptoPrimitive
permalink: /Java/CryptoPrimitive/
date: 2021-01-11
key: Java.C.CryptoPrimitive
category: Java
tags: ['java se', 'java.security', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CryptoPrimitive.description }}

## Sintaxis
~~~java
public enum CryptoPrimitive extends Enum<CryptoPrimitive>
~~~

## Enumerados
* [BLOCK_CIPHER](/Java/CryptoPrimitive/BLOCK_CIPHER)
* [KEY_AGREEMENT](/Java/CryptoPrimitive/KEY_AGREEMENT)
* [KEY_ENCAPSULATION](/Java/CryptoPrimitive/KEY_ENCAPSULATION)
* [KEY_WRAP](/Java/CryptoPrimitive/KEY_WRAP)
* [MAC](/Java/CryptoPrimitive/MAC)
* [MESSAGE_DIGEST](/Java/CryptoPrimitive/MESSAGE_DIGEST)
* [PUBLIC_KEY_ENCRYPTION](/Java/CryptoPrimitive/PUBLIC_KEY_ENCRYPTION)
* [SECURE_RANDOM](/Java/CryptoPrimitive/SECURE_RANDOM)
* [SIGNATURE](/Java/CryptoPrimitive/SIGNATURE)
* [STREAM_CIPHER](/Java/CryptoPrimitive/STREAM_CIPHER)

## Métodos
* [valueOf()](/Java/CryptoPrimitive/valueOf)
* [values()](/Java/CryptoPrimitive/values)

## Ejemplo
~~~java
{{ site.data.Java.C.CryptoPrimitive.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CryptoPrimitive.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
