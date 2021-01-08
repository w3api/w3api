---
title: CertStore.getCRLs()
permalink: Java/CertStore/getCRLs
date: 2021-01-04
key: JavaJava.C.CertStore
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertStore.metodos valor="getCRLs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Collection<? extends CRL> getCRLs(CRLSelector selector) throws CertStoreException
~~~

## Parámetros
* **CRLSelector selector**,  {% include w3api/param_description.html metodo=_data parametro="CRLSelector selector" %}

## Excepciones
[CertStoreException](/Java/CertStoreException/)

## Clase Padre
[CertStore](/Java/CertStore/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertStore.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
