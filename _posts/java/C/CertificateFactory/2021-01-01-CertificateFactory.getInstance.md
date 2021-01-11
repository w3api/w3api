---
title: CertificateFactory.getInstance()
permalink: Java/CertificateFactory/getInstance
date: 2021-01-11
key: JavaJava.C.CertificateFactory
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertificateFactory.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static CertificateFactory getInstance(String type)
static CertificateFactory getInstance(String type, String provider)
static CertificateFactory getInstance(String type, Provider provider)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **String provider**,  {% include w3api/param_description.html metodo=_dato parametro="String provider" %}
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
