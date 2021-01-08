---
title: PKIXCertPathValidatorResult.PKIXCertPathValidatorResult()
permalink: Java/PKIXCertPathValidatorResult/PKIXCertPathValidatorResult
date: 2021-01-04
key: JavaJava.P.PKIXCertPathValidatorResult
category: java
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
* **PolicyNode policyTree**,  {% include w3api/param_description.html metodo=_data parametro="PolicyNode policyTree" %}
* **TrustAnchor trustAnchor**,  {% include w3api/param_description.html metodo=_data parametro="TrustAnchor trustAnchor" %}
* **PublicKey subjectPublicKey**,  {% include w3api/param_description.html metodo=_data parametro="PublicKey subjectPublicKey" %}

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
{%- for _ldc in site.data.Java.P.PKIXCertPathValidatorResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
