---
title: CertStoreSpi.engineGetCRLs()
permalink: Java/CertStoreSpi/engineGetCRLs
date: 2021-01-04
key: JavaJava.C.CertStoreSpi
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertStoreSpi.metodos valor="engineGetCRLs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Collection<? extends CRL> engineGetCRLs(CRLSelector selector) throws CertStoreException
~~~

## Parámetros
* **CRLSelector selector**,  {% include w3api/param_description.html metodo=_data parametro="CRLSelector selector" %}

## Excepciones
[CertStoreException](/Java/CertStoreException/)

## Clase Padre
[CertStoreSpi](/Java/CertStoreSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertStoreSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
