---
title: CertificateFactorySpi.engineGenerateCRLs()
permalink: /Java/CertificateFactorySpi/engineGenerateCRLs/
date: 2021-01-11
key: Java.C.CertificateFactorySpi
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertificateFactorySpi.metodos valor="engineGenerateCRLs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Collection<? extends CRL> engineGenerateCRLs(InputStream inStream) throws CRLException
~~~

## Parámetros
* **InputStream inStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream inStream" %}

## Excepciones
[CRLException](/Java/CRLException/)

## Clase Padre
[CertificateFactorySpi](/Java/CertificateFactorySpi/)

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
