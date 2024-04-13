---
title: PKIXCertPathChecker.check()
permalink: /Java/PKIXCertPathChecker/check/
date: 2021-01-11
key: Java.P.PKIXCertPathChecker
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKIXCertPathChecker.metodos valor="check" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void check(Certificate cert) throws CertPathValidatorException
public abstract void check(Certificate cert, Collection<String> unresolvedCritExts) throws CertPathValidatorException
~~~

## Parámetros
* **Certificate cert**,  {% include w3api/param_description.html metodo=_dato parametro="Certificate cert" %}
* **Collection&lt;String&gt; unresolvedCritExts**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<String> unresolvedCritExts" %}

## Excepciones
[CertPathValidatorException](/Java/CertPathValidatorException/)

## Clase Padre
[PKIXCertPathChecker](/Java/PKIXCertPathChecker/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
