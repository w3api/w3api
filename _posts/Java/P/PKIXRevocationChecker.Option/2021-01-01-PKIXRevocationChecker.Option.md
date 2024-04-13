---
title: PKIXRevocationChecker.Option
permalink: /Java/PKIXRevocationChecker/Option/
date: 2021-01-11
key: Java.P.PKIXRevocationChecker.Option
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'enumerado java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PKIXRevocationChecker.Option.description }}

## Sintaxis
~~~java
public static enum PKIXRevocationChecker.Option extends Enum<PKIXRevocationChecker.Option>
~~~

## Enumerados
* [NO_FALLBACK](/Java/PKIXRevocationChecker/Option/NO_FALLBACK/)
* [ONLY_END_ENTITY](/Java/PKIXRevocationChecker/Option/ONLY_END_ENTITY/)
* [PREFER_CRLS](/Java/PKIXRevocationChecker/Option/PREFER_CRLS/)
* [SOFT_FAIL](/Java/PKIXRevocationChecker/Option/SOFT_FAIL/)

## Métodos
* [valueOf()](/Java/PKIXRevocationChecker/Option/valueOf/)
* [values()](/Java/PKIXRevocationChecker/Option/values/)

## Ejemplo
~~~java
{{ site.data.Java.P.PKIXRevocationChecker.Option.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PKIXRevocationChecker.Option.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
