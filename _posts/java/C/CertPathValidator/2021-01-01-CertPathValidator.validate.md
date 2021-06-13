---
title: CertPathValidator.validate()
permalink: /Java/CertPathValidator/validate/
date: 2021-01-11
key: Java.C.CertPathValidator
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertPathValidator.metodos valor="validate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CertPathValidatorResult validate(CertPath certPath, CertPathParameters params) throws CertPathValidatorException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **CertPathParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="CertPathParameters params" %}
* **CertPath certPath**,  {% include w3api/param_description.html metodo=_dato parametro="CertPath certPath" %}

## Excepciones
[CertPathValidatorException](/Java/CertPathValidatorException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[CertPathValidator](/Java/CertPathValidator/)

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
