---
title: CertPathChecker.check()
permalink: Java/CertPathChecker/check
date: 2021-01-04
key: JavaJava.C.CertPathChecker
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertPathChecker.metodos valor="check" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void check(Certificate cert) throws CertPathValidatorException
~~~

## Parámetros
* **Certificate cert**,  {% include w3api/param_description.html metodo=_data parametro="Certificate cert" %}

## Excepciones
[CertPathValidatorException](/Java/CertPathValidatorException/)

## Clase Padre
[CertPathChecker](/Java/CertPathChecker/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertPathChecker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
