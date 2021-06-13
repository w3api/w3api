---
title: CertPathValidator.CertPathValidator()
permalink: /Java/CertPathValidator/CertPathValidator/
date: 2021-01-11
key: Java.C.CertPathValidator
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertPathValidator.constructores valor="CertPathValidator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CertPathValidator(CertPathValidatorSpi validatorSpi, Provider provider, String algorithm)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **CertPathValidatorSpi validatorSpi**,  {% include w3api/param_description.html metodo=_dato parametro="CertPathValidatorSpi validatorSpi" %}

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
