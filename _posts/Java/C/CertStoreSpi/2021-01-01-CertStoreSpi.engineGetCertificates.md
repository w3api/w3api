---
title: CertStoreSpi.engineGetCertificates()
permalink: /Java/CertStoreSpi/engineGetCertificates/
date: 2021-01-11
key: Java.C.CertStoreSpi
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertStoreSpi.metodos valor="engineGetCertificates" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Collection<? extends Certificate> engineGetCertificates(CertSelector selector) throws CertStoreException
~~~

## Parámetros
* **CertSelector selector**,  {% include w3api/param_description.html metodo=_dato parametro="CertSelector selector" %}

## Excepciones
[CertStoreException](/Java/CertStoreException/)

## Clase Padre
[CertStoreSpi](/Java/CertStoreSpi/)

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
