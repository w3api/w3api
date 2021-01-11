---
title: CertStore.getCertificates()
permalink: Java/CertStore/getCertificates
date: 2021-01-11
key: JavaJava.C.CertStore
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertStore.metodos valor="getCertificates" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Collection<? extends Certificate> getCertificates(CertSelector selector) throws CertStoreException
~~~

## Parámetros
* **CertSelector selector**,  {% include w3api/param_description.html metodo=_dato parametro="CertSelector selector" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
