---
title: DigestMethod
permalink: /Java/DigestMethod/
date: 2021-01-11
key: Java.D.DigestMethod
category: Java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DigestMethod.description }}

## Sintaxis
~~~java
public interface DigestMethod extends XMLStructure, AlgorithmMethod
~~~

## Campos
* [RIPEMD160](/Java/DigestMethod/RIPEMD160/)
* [SHA1](/Java/DigestMethod/SHA1/)
* [SHA256](/Java/DigestMethod/SHA256/)
* [SHA512](/Java/DigestMethod/SHA512/)

## Métodos
* [getParameterSpec()](/Java/DigestMethod/getParameterSpec/)

## Ejemplo
~~~java
{{ site.data.Java.D.DigestMethod.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DigestMethod.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
