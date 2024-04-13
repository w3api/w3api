---
title: PKIXCertPathBuilderResult.PKIXCertPathBuilderResult()
permalink: /Java/PKIXCertPathBuilderResult/PKIXCertPathBuilderResult/
date: 2021-01-11
key: Java.P.PKIXCertPathBuilderResult
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKIXCertPathBuilderResult.constructores valor="PKIXCertPathBuilderResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PKIXCertPathBuilderResult(CertPath certPath, TrustAnchor trustAnchor, PolicyNode policyTree, PublicKey subjectPublicKey)
~~~

## Parámetros
* **PublicKey subjectPublicKey**,  {% include w3api/param_description.html metodo=_dato parametro="PublicKey subjectPublicKey" %}
* **CertPath certPath**,  {% include w3api/param_description.html metodo=_dato parametro="CertPath certPath" %}
* **TrustAnchor trustAnchor**,  {% include w3api/param_description.html metodo=_dato parametro="TrustAnchor trustAnchor" %}
* **PolicyNode policyTree**,  {% include w3api/param_description.html metodo=_dato parametro="PolicyNode policyTree" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PKIXCertPathBuilderResult](/Java/PKIXCertPathBuilderResult/)

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
