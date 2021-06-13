---
title: CertificateFactory.CertificateFactory()
permalink: /Java/CertificateFactory/CertificateFactory/
date: 2021-01-11
key: Java.C.CertificateFactory
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertificateFactory.constructores valor="CertificateFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CertificateFactory(CertificateFactorySpi certFacSpi, Provider provider, String type)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **CertificateFactorySpi certFacSpi**,  {% include w3api/param_description.html metodo=_dato parametro="CertificateFactorySpi certFacSpi" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

## Clase Padre
[CertificateFactory](/Java/CertificateFactory/)

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
