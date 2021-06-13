---
title: Certificate
permalink: /Java/Certificate-java-security/
date: 2021-01-11
key: Java.C.Certificate-java-security
category: Java
tags: ['java se', 'java.security', 'java.base', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Certificate-java-security.description }}

## Sintaxis
~~~java
@Deprecated(since="1.2", forRemoval=true) public interface Certificate
~~~

## Métodos
* [decode()](/Java/Certificate-java-security/decode)
* [encode()](/Java/Certificate-java-security/encode)
* [getFormat()](/Java/Certificate-java-security/getFormat)
* [getGuarantor()](/Java/Certificate-java-security/getGuarantor)
* [getPrincipal()](/Java/Certificate-java-security/getPrincipal)
* [getPublicKey()](/Java/Certificate-java-security/getPublicKey)
* [toString()](/Java/Certificate-java-security/toString)

## Ejemplo
~~~java
{{ site.data.Java.C.Certificate-java-security.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Certificate-java-security.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
