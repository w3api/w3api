---
title: CertStore.CertStore()
permalink: Java/CertStore/CertStore
date: 2021-01-11
key: JavaJava.C.CertStore
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertStore.constructores valor="CertStore" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CertStore(CertStoreSpi storeSpi, Provider provider, String type, CertStoreParameters params)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **CertStoreParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="CertStoreParameters params" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **CertStoreSpi storeSpi**,  {% include w3api/param_description.html metodo=_dato parametro="CertStoreSpi storeSpi" %}

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
