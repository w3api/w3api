---
title: CertificateFactorySpi.engineGenerateCRL()
permalink: Java/CertificateFactorySpi/engineGenerateCRL
date: 2021-01-04
key: JavaJava.C.CertificateFactorySpi
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertificateFactorySpi.metodos valor="engineGenerateCRL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract CRL engineGenerateCRL(InputStream inStream) throws CRLException
~~~

## Parámetros
* **InputStream inStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inStream" %}

## Excepciones
[CRLException](/Java/CRLException/)

## Clase Padre
[CertificateFactorySpi](/Java/CertificateFactorySpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertificateFactorySpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
