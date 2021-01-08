---
title: CertPathValidatorSpi.engineValidate()
permalink: Java/CertPathValidatorSpi/engineValidate
date: 2021-01-04
key: JavaJava.C.CertPathValidatorSpi
category: java
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
* **CertPath certPath**,  {% include w3api/param_description.html metodo=_data parametro="CertPath certPath" %}
* **CertPathParameters params**,  {% include w3api/param_description.html metodo=_data parametro="CertPathParameters params" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [CertPathValidatorException](/Java/CertPathValidatorException/)

## Clase Padre
[CertPathValidatorSpi](/Java/CertPathValidatorSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertPathValidatorSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
