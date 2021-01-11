---
title: PKIXReason
permalink: Java/PKIXReason
date: 2021-01-11
key: JavaJava.P.PKIXReason
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PKIXReason.description }}

## Sintaxis
~~~java
public enum PKIXReason extends Enum<PKIXReason> implements CertPathValidatorException.Reason
~~~

## Enumerados
* [INVALID_KEY_USAGE](/Java/PKIXReason/INVALID_KEY_USAGE)
* [INVALID_NAME](/Java/PKIXReason/INVALID_NAME)
* [INVALID_POLICY](/Java/PKIXReason/INVALID_POLICY)
* [NAME_CHAINING](/Java/PKIXReason/NAME_CHAINING)
* [NO_TRUST_ANCHOR](/Java/PKIXReason/NO_TRUST_ANCHOR)
* [NOT_CA_CERT](/Java/PKIXReason/NOT_CA_CERT)
* [PATH_TOO_LONG](/Java/PKIXReason/PATH_TOO_LONG)
* [UNRECOGNIZED_CRIT_EXT](/Java/PKIXReason/UNRECOGNIZED_CRIT_EXT)

## Métodos
* [valueOf()](/Java/PKIXReason/valueOf)
* [values()](/Java/PKIXReason/values)

## Ejemplo
~~~java
{{ site.data.Java.P.PKIXReason.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PKIXReason.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
