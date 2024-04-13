---
title: CertPathValidatorSpi.engineValidate()
permalink: /Java/CertPathValidatorSpi/engineValidate/
date: 2021-01-11
key: Java.C.CertPathValidatorSpi
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertPathValidatorSpi.metodos valor="engineValidate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract CertPathValidatorResult engineValidate(CertPath certPath, CertPathParameters params) throws CertPathValidatorException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **CertPathParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="CertPathParameters params" %}
* **CertPath certPath**,  {% include w3api/param_description.html metodo=_dato parametro="CertPath certPath" %}

## Excepciones
[CertPathValidatorException](/Java/CertPathValidatorException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[CertPathValidatorSpi](/Java/CertPathValidatorSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
