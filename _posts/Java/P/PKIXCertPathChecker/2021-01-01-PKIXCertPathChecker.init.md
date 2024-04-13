---
title: PKIXCertPathChecker.init()
permalink: /Java/PKIXCertPathChecker/init/
date: 2021-01-11
key: Java.P.PKIXCertPathChecker
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKIXCertPathChecker.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void init(boolean forward) throws CertPathValidatorException
~~~

## Parámetros
* **boolean forward**,  {% include w3api/param_description.html metodo=_dato parametro="boolean forward" %}

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
