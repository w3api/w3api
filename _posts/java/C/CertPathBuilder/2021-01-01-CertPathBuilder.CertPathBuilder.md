---
title: CertPathBuilder.CertPathBuilder()
permalink: Java/CertPathBuilder/CertPathBuilder
date: 2021-01-11
key: JavaJava.C.CertPathBuilder
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertPathBuilder.constructores valor="CertPathBuilder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CertPathBuilder(CertPathBuilderSpi builderSpi, Provider provider, String algorithm)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **CertPathBuilderSpi builderSpi**,  {% include w3api/param_description.html metodo=_dato parametro="CertPathBuilderSpi builderSpi" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}

## Clase Padre
[CertPathBuilder](/Java/CertPathBuilder/)

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
