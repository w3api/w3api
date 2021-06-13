---
title: CertPathValidatorException.BasicReason
permalink: /Java/CertPathValidatorException/BasicReason/
date: 2021-01-11
key: Java.C.CertPathValidatorException.BasicReason
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CertPathValidatorException.BasicReason.description }}

## Sintaxis
~~~java
public static enum CertPathValidatorException.BasicReason extends Enum<CertPathValidatorException.BasicReason> implements CertPathValidatorException.Reason
~~~

## Enumerados
* [ALGORITHM_CONSTRAINED](/Java/CertPathValidatorException/BasicReason/ALGORITHM_CONSTRAINED)
* [EXPIRED](/Java/CertPathValidatorException/BasicReason/EXPIRED)
* [INVALID_SIGNATURE](/Java/CertPathValidatorException/BasicReason/INVALID_SIGNATURE)
* [NOT_YET_VALID](/Java/CertPathValidatorException/BasicReason/NOT_YET_VALID)
* [REVOKED](/Java/CertPathValidatorException/BasicReason/REVOKED)
* [UNDETERMINED_REVOCATION_STATUS](/Java/CertPathValidatorException/BasicReason/UNDETERMINED_REVOCATION_STATUS)
* [UNSPECIFIED](/Java/CertPathValidatorException/BasicReason/UNSPECIFIED)

## Métodos
* [valueOf()](/Java/CertPathValidatorException/BasicReason/valueOf)
* [values()](/Java/CertPathValidatorException/BasicReason/values)

## Ejemplo
~~~java
{{ site.data.Java.C.CertPathValidatorException.BasicReason.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertPathValidatorException.BasicReason.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
