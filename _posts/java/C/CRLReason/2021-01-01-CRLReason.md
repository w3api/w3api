---
title: CRLReason
permalink: /Java/CRLReason/
date: 2021-01-11
key: Java.C.CRLReason
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CRLReason.description }}

## Sintaxis
~~~java
public enum CRLReason extends Enum<CRLReason>
~~~

## Enumerados
* [AA_COMPROMISE](/Java/CRLReason/AA_COMPROMISE)
* [AFFILIATION_CHANGED](/Java/CRLReason/AFFILIATION_CHANGED)
* [CA_COMPROMISE](/Java/CRLReason/CA_COMPROMISE)
* [CERTIFICATE_HOLD](/Java/CRLReason/CERTIFICATE_HOLD)
* [CESSATION_OF_OPERATION](/Java/CRLReason/CESSATION_OF_OPERATION)
* [KEY_COMPROMISE](/Java/CRLReason/KEY_COMPROMISE)
* [PRIVILEGE_WITHDRAWN](/Java/CRLReason/PRIVILEGE_WITHDRAWN)
* [REMOVE_FROM_CRL](/Java/CRLReason/REMOVE_FROM_CRL)
* [SUPERSEDED](/Java/CRLReason/SUPERSEDED)
* [UNSPECIFIED](/Java/CRLReason/UNSPECIFIED)
* [UNUSED](/Java/CRLReason/UNUSED)

## Métodos
* [valueOf()](/Java/CRLReason/valueOf)
* [values()](/Java/CRLReason/values)

## Ejemplo
~~~java
{{ site.data.Java.C.CRLReason.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CRLReason.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
