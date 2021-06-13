---
title: PKIXCertPathValidatorResult.PKIXCertPathValidatorResult()
permalink: /Java/PKIXCertPathValidatorResult/PKIXCertPathValidatorResult/
date: 2021-01-11
key: Java.P.PKIXCertPathValidatorResult
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKIXCertPathValidatorResult.constructores valor="PKIXCertPathValidatorResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PKIXCertPathValidatorResult(TrustAnchor trustAnchor, PolicyNode policyTree, PublicKey subjectPublicKey)
~~~

## Parámetros
* **PublicKey subjectPublicKey**,  {% include w3api/param_description.html metodo=_dato parametro="PublicKey subjectPublicKey" %}
* **TrustAnchor trustAnchor**,  {% include w3api/param_description.html metodo=_dato parametro="TrustAnchor trustAnchor" %}
* **PolicyNode policyTree**,  {% include w3api/param_description.html metodo=_dato parametro="PolicyNode policyTree" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PKIXCertPathValidatorResult](/Java/PKIXCertPathValidatorResult/)

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
